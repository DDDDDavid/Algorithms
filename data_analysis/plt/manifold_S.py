# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 16:27:02 2018

@author: madawei1
"""

from matplotlib.ticker import NullFormatter
from sklearn import manifold, datasets

n_points = 1000
X, color = datasets.samples_generator.make_s_curve(n_points, random_state=0)
n_neighbors = 10
n_components = 2
fig = pl.figure(figsize=(15, 8))
pl.suptitle("Manifold Learning with %i points, %i neighbors"
        % (1000, n_neighbors), fontsize=14)
ax = fig.add_subplot(241, projection='3d')
ax.scatter(X[:, 0], X[:, 1], X[:, 2], c=color, cmap=pl.cm.Spectral)
plt.draw()

#拟合线性的流形学习模型LLE, LTSA, Hessian LLE, 和Modified LLE
# Perform Locally Linear Embedding Manifold learning
methods = ['standard', 'ltsa', 'hessian', 'modified']
labels = ['LLE', 'LTSA', 'Hessian LLE', 'Modified LLE']
for i, method in enumerate(methods):
    t0 = time()
    trans_data = mds.fit_transform(X)
    
    t1 = time()
    print("%s: %.2g sec" % (methods[i], t1 - t0))
    ax = fig.add_subplot(242 + i)
    pl.scatter(trans_data[:,0], trans_data[:,1],  c=color, cmap=pl.cm.Spectral)
    pl.title("%s (%.2g sec)" % (labels[i], t1 - t0))
    ax.xaxis.set_major_formatter(NullFormatter())
    ax.yaxis.set_major_formatter(NullFormatter())
    pl.axis('tight')
plt.draw()