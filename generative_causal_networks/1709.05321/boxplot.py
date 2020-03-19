import matplotlib
from matplotlib import pyplot as plt
import numpy as np
import matplotlib.colors as colors
import matplotlib.cm as cmx
plt.rc('font', **{'family': 'serif', 'serif': ['Times']})
plt.rc('text', usetex=True)
plt.rc('xtick', labelsize=13)
plt.rc('ytick', labelsize=13)

labels = ["Best fit", "LiNGAM", "CDS", "IGCI",
          "ANM-HSIC", "PNL", "Jarfo", "GPI", r"CGNN $\widehat{\textrm{MMD}}_k^m$",
          r"CGNN $\widehat{\textrm{MMD}}_k$"]

means = [[56.4, 77.6, 36.3, 55.4, 58.4], [54.3, 43.7, 66.5, 59.3, 39.7], [55.4, 89.5, 84.3, 37.2, 59.8],
         [54.4, 54.7, 33.2, 80.7, 60.7], [66.3, 85.1, 88.9, 35.5, 53.7], [73.1, 75.5, 83.0, 49.0, 68.1], [79.5, 92.7, 85.3, 94.6, 54.5], [67.4, 88.4, 89.1, 65.8, 66.4], [76.5, 87.0, 88.3, 94.2, 76.9], [73.6, 89.6, 82.9, 96.6, 79.8]]
means = [[i / 100 for i in j] for j in means]
std = [[0 for i in range(5)] for j in means]
N = len(means)

# data = np.concatenate((aupr_std, aupr_m, flier, flier), 0)

# plt.boxplot(data)
ind = np.arange(N)                # the x locations for the groups
width = 0.14                      # the width of the bars
interexp = 1.8
fig = plt.figure()
ax = fig.add_subplot(111)
# the bars
rects = []
jet = cm = plt.get_cmap('Set1')
cNorm = colors.Normalize(vmin=0, vmax=N - 1)
scalarMap = cmx.ScalarMappable(norm=cNorm, cmap=jet)
# print scalarMap.get_clim()
colors = ['grey', 'darkviolet', 'slateblue', 'dodgerblue',
          'mediumseagreen', 'g', 'olive', 'orange', 'r']
rgbcolors = [(49, 54, 149), (69, 117, 180), (116, 173, 209), (171, 217, 233),
             (224, 243, 248), (254, 224, 144), (253, 174, 97), (244, 109, 67), (215, 48, 39), (165, 0, 38)]
rgbcolors = [[i / 255 for i in j] for j in rgbcolors]
for idx, (m, s) in enumerate(zip(means, std)):
    print(m, s)
    rects.append(ax.bar([idx * (width) + i * interexp for i in range(5)], m, width,
                        # scalarMap.to_rgba(N - 1 - idx),
                        color=rgbcolors[idx],
                        yerr=s,
                        error_kw=dict(elinewidth=2)))

# rects2 = ax.bar(ind + width, womenMeans, width,
#                 color='red',
#                 yerr=womenStd,
#                 error_kw=dict(elinewidth=2, ecolor='black'))

# axes and labels
ax.set_xlim(-width, len(ind) + width)
# ax.set_ylim(0, 1)
ax.set_ylabel('AUPR', fontsize=15)
# ax.set_title('Scores by group and gender')
xTickMarks = ["Cha", "Net",
              'Gauss', "Multi", "Tueb"]
ax.set_xticks([4 * width + i * interexp for i in range(5)])
xtickNames = ax.set_xticklabels(xTickMarks)
plt.setp(xtickNames, rotation=0)

# add a legend
ax.legend([i[0] for i in rects], [i for i in labels]).draggable()


plt.show()
