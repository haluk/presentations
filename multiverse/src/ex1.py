#!/usr/bin/env python3

import timeit

from multiverse import (DeltaERP, NormalERP, ObservableNormalERP, do, observe,
                        predict, run_inference)
from utils import calculate_expectation

NUM_SAMPLES = 1000


def base_program():
    X = NormalERP(0, 1)
    Z = NormalERP(0, 1)
    Y = ObservableNormalERP(X.value + Z.value, 2, depends_on=[X, Z],)

    return X, Z, Y


def program_with_data():
    X, Z, Y = base_program()
    observe(Y, 1.2342)
    do(Z, -2.5236)

    predict(Y.value, predict_counterfactual=True)


start = timeit.default_timer()
results = run_inference(program_with_data, NUM_SAMPLES)
stop = timeit.default_timer()

print("Time:", stop - start)
result = calculate_expectation(results)
print("Prediction:", result)
