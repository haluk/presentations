import numpy as np

from matplotlib import pyplot as plt
import matplotlib
plt.rc('font', **{'family': 'serif', 'serif': ['Times']})
plt.rc('text', usetex=True)
plt.rc('xtick', labelsize=18)
plt.rc('ytick', labelsize=18)

data_orig = np.genfromtxt("TruePair.csv", delimiter=",", skip_header=1)

data_ab_2 = np.genfromtxt("AcausesB-hdim2.csv", delimiter=",", skip_header=1)
data_ab_5 = np.genfromtxt("AcausesB-hdim5.csv", delimiter=",", skip_header=1)
data_ab_20 = np.genfromtxt("AcausesB-hdim20.csv", delimiter=",", skip_header=1)
data_ab_100 = np.genfromtxt("AcausesB-hdim100.csv", delimiter=",", skip_header=1)

data_ba_2 = np.genfromtxt("BcausesA-hdim2.csv", delimiter=",", skip_header=1)
data_ba_5 = np.genfromtxt("BcausesA-hdim5.csv", delimiter=",", skip_header=1)
data_ba_20 = np.genfromtxt("BcausesA-hdim20.csv", delimiter=",", skip_header=1)
data_ba_100 = np.genfromtxt("BcausesA-hdim100.csv", delimiter=",", skip_header=1)


def make_ticklabels_invisible(fig):
    for i, ax in enumerate(fig.axes):
        ax.get_yaxis().set_label_position("right")
        ax.get_xaxis().set_tick_params(which='both', bottom='off', top='off', labelbottom='off')
        ax.get_yaxis().set_tick_params(which='both', bottom='off', top='off', labelbottom='off')
        for tl in ax.get_xticklabels() + ax.get_yticklabels():
            tl.set_visible(False)


plt.locator_params(axis='y', nticks=6)
plt.locator_params(axis='x', nticks=10)

plt.figure(figsize=(6.5, 2))
plt.subplot2grid((2, 6), (0, 0), rowspan=2, colspan=2)
plt.plot(data_orig[:, 0], data_orig[:, 1], ",", alpha=.8)
plt.title("original data, $X \\to Y$")

plt.subplot2grid((2, 6), (0, 2), colspan=1)
plt.plot(data_ab_2[:, 0], data_ab_2[:, 1], ",", alpha=.5)
plt.title("$n_h = 2$")
plt.subplot2grid((2, 6), (0, 3), colspan=1)
plt.plot(data_ab_5[:, 0], data_ab_5[:, 1], ",", alpha=.5)
plt.title("$n_h = 5$")
plt.subplot2grid((2, 6), (0, 4), colspan=1)
plt.plot(data_ab_20[:, 0], data_ab_20[:, 1], ",", alpha=.5)
plt.title("$n_h = 20$")
plt.subplot2grid((2, 6), (0, 5), colspan=1)
plt.plot(data_ab_100[:, 0], data_ab_100[:, 1], ",", alpha=.5)
plt.title("$n_h = 100$")
plt.ylabel('CGNNs $X \\to Y$', fontsize=8, rotation=270, labelpad=12)

plt.subplot2grid((2, 6), (1, 2), colspan=1)
plt.plot(data_ba_2[:, 0], data_ba_2[:, 1], ",", alpha=.5)
plt.subplot2grid((2, 6), (1, 3), colspan=1)
plt.plot(data_ba_5[:, 0], data_ba_5[:, 1], ",", alpha=.5)
plt.subplot2grid((2, 6), (1, 4), colspan=1)
plt.plot(data_ba_20[:, 0], data_ba_20[:, 1], ",", alpha=.5)
plt.subplot2grid((2, 6), (1, 5), colspan=1)
plt.plot(data_ba_100[:, 0], data_ba_100[:, 1], ",", alpha=.5)
plt.ylabel('CGNNs $X \\leftarrow Y$', fontsize=8, rotation=270, labelpad=12)

make_ticklabels_invisible(plt.gcf())
plt.savefig("parallelogram.pdf", bbox_inches='tight')
