#!/usr/bin/env python3

import timeit

import numpy
import pyro
import torch

NUM_SAMPLES = 1000  # for both abduction and intervention/prediction
ROUND_DIGIT_APPR = (
    1  # discretisation to avoid 'infinite rejection sampling' for continuous variables
)
GUIDE_TO_USE = None
latent_procedure_sites = ["X", "Z", "Y_epsilon"]


def rounder(val):
    if ROUND_DIGIT_APPR is None:
        # Don't round:
        return torch.tensor(float(val))
    else:
        return torch.tensor(round(float(val), ROUND_DIGIT_APPR))


def extract_obs_if_any(data, var_name):
    if data is not None and var_name in data:
        return data[var_name]
    else:
        None


def model(data=None, posterior_distribution=None):
    if posterior_distribution is not None and "X" in posterior_distribution:
        # If we are re-using a sample from a posterior,
        # we just should use the value for this variable
        # directly:
        X = posterior_distribution["X"]
    else:
        X = pyro.sample(
            "X", pyro.distributions.Normal(0, 1), obs=extract_obs_if_any(data, "X")
        )
    if posterior_distribution is not None and "Z" in posterior_distribution:
        Z = posterior_distribution["Z"]
    else:
        Z = pyro.sample(
            "Z", pyro.distributions.Normal(0, 1), obs=extract_obs_if_any(data, "Z")
        )
    if posterior_distribution is not None and "Y_epsilon" in posterior_distribution:
        Y_epsilon = posterior_distribution["Y_epsilon"]
    else:
        Y_epsilon = pyro.sample("Y_epsilon", pyro.distributions.Normal(0, 2))
    discrete_Y = rounder(X + Z + Y_epsilon)
    # We must (re-)evaluate deterministic variables in any case:
    Y = pyro.sample(
        "Y",
        pyro.distributions.Delta(torch.tensor(discrete_Y)),
        obs=extract_obs_if_any(data, "Y"),
    )
    return X, Z, Y_epsilon, Y


data = {"Y": rounder(1.2342), "X": None, "Z": None}
start = timeit.default_timer()

# 1. Abduction
posterior = pyro.infer.Importance(
    model, guide=GUIDE_TO_USE, num_samples=NUM_SAMPLES
).run(data=data)
print("Abduction␣ESS:", posterior.get_ESS())
posterior = pyro.infer.EmpiricalMarginal(posterior, sites=latent_procedure_sites)

# 2. Intervention
intervention = {"Z": -2.5236}
intervened_posterior = pyro.do(model, intervention)

# 3. Prediction
predictions_Y = []
for sample_index in range(NUM_SAMPLES):
    # We are drawing a sample from the posterior world:
    posterior_sample_vector = posterior.sample()
    # We drew that sample in a vector form;
    # now we need to transform
    # it to a dictionary of variables.
    posterior_sample = {}
    for index, var_name in enumerate(latent_procedure_sites):
        if var_name in intervention:
            # We must ensure that we don't
            # use intervened variables
            # from its posterior:
            pass
        else:
            posterior_sample[var_name] = posterior_sample_vector[index]
    X, Z, Y_epsilon, Y = intervened_posterior(posterior_distribution=posterior_sample)
    predictions_Y.append(Y)

stop = timeit.default_timer()

print("Time:", stop - start)
expected_Y = numpy.mean(predictions_Y)
print("Prediction:", expected_Y)
