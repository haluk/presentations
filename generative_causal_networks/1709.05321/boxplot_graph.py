import matplotlib
from matplotlib import pyplot as plt
import numpy as np
import matplotlib.colors as colors
import matplotlib.cm as cmx
plt.rc('font', **{'family': 'serif', 'serif': ['Times']})
plt.rc('text', usetex=True)
plt.rc('xtick', labelsize=13)
plt.rc('ytick', labelsize=13)

labels = ["PC-Gauss", "PC-HSIC", "ANM", "Jarfo",
          "GES", "LiNGAM", "CAM", r"CGNN $\widehat{\textrm{MMD}}_k^m$",
          r"CGNN $\widehat{\textrm{MMD}}_k$"]

means = [[0.67, 0.42, 0.40, 0.22, 0.19], [0.80, 0.49, 0.38, 0, 0.18], [0.67, 0.52,0.36, 0.35, 0.34], [0.74, 0.58,0.42,
                                                                                                   0.45, 0.33], [
                                                                                                       0.48, 0.37, 0.44, 0.52, 0.26], [0.65, 0.53, 0.40, 0.37, 0.29], [0.69, 0.51,0.73, 0.69, 0.37], [0.77, 0.54, .8, 0.82,0.68], [0.89, 0.62, 0.79, 0.75, 0.74]]
std = [[0.11, 0.06, 0.16, 0.03, .07], [0.08, .06, .15, 0, .01], [0.11, .1,.17,.12, .05], [0.10, .09,.17,.13, .02],
       [0.13, .08,.17 ,.03, 0.01], [0.10, .1,0.22,0.28, .03], [0.13, .11,0.08,0.05, .1], [0.09, .08, .12, .1, .07], [0.09, .12,0.12, 0.09, .09]]
N = len(means)

# data = np.concatenate((aupr_std, aupr_m, flier, flier), 0)

# plt.boxplot(data)
ind = np.arange(N)                # the x locations for the groups
width = 0.35                      # the width of the bars
interexp = 4
fig = plt.figure()
ax = fig.add_subplot(111)
# the bars
rects = []
means = [[i for i in c[:2]] for c in means]
std = [[i for i in c[:2]] for c in std]
jet = cm = plt.get_cmap('Set1')
cNorm = colors.Normalize(vmin=0, vmax=N - 1)
scalarMap = cmx.ScalarMappable(norm=cNorm, cmap=jet)
# print scalarMap.get_clim()
colors = ['grey', 'darkviolet', 'slateblue', 'dodgerblue',
          'mediumseagreen', 'g', 'olive', 'orange', 'r']
rgbcolors = [(69, 117, 180), (116, 173, 209), (171, 217, 233), (224, 243, 248),
             (255, 255, 191), (254, 224, 144), (253, 174, 97), (244, 109, 67), (215, 48, 39)]
rgbcolors = [[i / 255 for i in j] for j in rgbcolors]
for idx, (m, s) in enumerate(zip(means, std)):
    print(m, s)
    rects.append(ax.bar([idx * (width) + i * interexp for i in range(2)], m, width,
                        # scalarMap.to_rgba(N - 1 - idx),
                        color=rgbcolors[idx],
                        yerr=s,
                        error_kw=dict(elinewidth=2, ecolor='black')))

# rects2 = ax.bar(ind + width, womenMeans, width,
#                 color='red',
#                 yerr=womenStd,
#                 error_kw=dict(elinewidth=2, ecolor='black'))

# axes and labels
ax.set_xlim(-width, len(ind) + width)
# ax.set_ylim(0, 1)
ax.set_ylabel('AUPR', fontsize=15)
# ax.set_title('Scores by group and gender')
xTickMarks = ["Skeleton without error", r"Skeleton with 20\% of error"]
#xTickMarks =[r"SynTReN 20 nodes", r"SynTReN 50 nodes" , r'Causal protein network']
ax.set_xticks([4 * width + i * interexp for i in range(2)])
xtickNames = ax.set_xticklabels(xTickMarks)
plt.setp(xtickNames, rotation=0)

# add a legend
ax.legend([i[0] for i in rects], [i for i in labels]).draggable()


plt.show()
