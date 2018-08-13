# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 16:35:13 2018

@author: madawei1
"""

from time import time
import numpy as np
import pylab as pl
from matplotlib import offsetbox
from sklearn import (manifold, datasets, decomposition, ensemble, lda,
                     random_projection)
 
digits = datasets.load_digits(n_class=6)
X = digits.data
y = digits.target
n_samples, n_features = X.shape
n_neighbors = 30
# Plot images of the digits
n_img_per_row = 20
img = np.zeros((10 * n_img_per_row, 10 * n_img_per_row))
for i in range(n_img_per_row):
    ix = 10 * i + 1
    for j in range(n_img_per_row):
        iy = 10 * j + 1
        img[ix:ix + 8, iy:iy + 8] = X[i * n_img_per_row + j].reshape((8, 8))
 
pl.imshow(img, cmap=pl.cm.binary)
pl.xticks([])
pl.yticks([])
pl.title('digits dataset')


# Scale and visualize the embedding vectors
def plot_embedding(X, title=None):
    x_min, x_max = np.min(X, 0), np.max(X, 0)
    X = (X - x_min) / (x_max - x_min)
    pl.figure()
    ax = pl.subplot(111)
    for i in range(X.shape[0]):
        pl.text(X[i, 0], X[i, 1], str(digits.target[i]),
                color=pl.cm.Set1(y[i] / 10.),
                fontdict={'weight': 'bold', 'size': 9})
    if hasattr(offsetbox, 'AnnotationBbox'):
        # only print thumbnails with matplotlib > 1.0
        shown_images = np.array([[1., 1.]])  # just something big
        for i in range(digits.data.shape[0]):
            dist = np.sum((X[i] - shown_images) ** 2, 1)
            if np.min(dist) < 4e-3:
                # don't show points that are too close
                continue
            shown_images = np.r_[shown_images, [X[i]]]
            imagebox = offsetbox.AnnotationBbox(
                offsetbox.OffsetImage(digits.images[i], cmap=pl.cm.gray_r),
                X[i])
            ax.add_artist(imagebox)
    pl.xticks([]), pl.yticks([])
    if title is not None:
        pl.title(title)
        
#1.Random 2D projection using a random unitary matrix
t0 = time()
rp = random_projection.SparseRandomProjection(n_components=2, random_state=42)
X_projected = rp.fit_transform(X)
plot_embedding(X_projected, "Random Projection (time %.2fs)" % (time() - t0))

#2.Projection on to the first 2 principal components
t0 = time()
X_pca = decomposition.TruncatedSVD(n_components=2).fit_transform(X)
plot_embedding(X_pca, "PCA (time %.2fs)" % (time() - t0))

#3.Projection on to the first 2 linear discriminant components
X2 = X.copy()
X2.flat[::X.shape[1] + 1] += 0.01  # Make X invertible
t0 = time()
X_lda = lda.LDA(n_components=2).fit_transform(X2, y)
plot_embedding(X_lda,"LDA (time %.2fs)" % (time() - t0))


#4.Isomap projection of the digits dataset
t0 = time()
X_iso = manifold.Isomap(n_neighbors, n_components=2).fit_transform(X)
plot_embedding(X_iso, "Isomap (time %.2fs)" %  (time() - t0))


#4.Locally linear embedding of the digits dataset
clf = manifold.LocallyLinearEmbedding(n_neighbors, n_components=2, method='standard')
t0 = time()
X_lle = clf.fit_transform(X)
plot_embedding(X_lle, "LLE (time %.2fs)" %    (time() - t0))


#5.Modified Locally linear embedding of the digits dataset
clf = manifold.LocallyLinearEmbedding(n_neighbors, n_components=2, method='modified')
t0 = time()
X_mlle = clf.fit_transform(X)
plot_embedding(X_mlle,  "MLLE (time %.2fs)" %   (time() - t0))


#6.HLLE embedding of the digits dataset
clf = manifold.LocallyLinearEmbedding(n_neighbors, n_components=2, method='hessian')
t0 = time()
X_hlle = clf.fit_transform(X)
plot_embedding(X_hlle,"HLLE (time %.2fs)" %   (time() - t0))


#7.LTSA embedding of the digits dataset
clf = manifold.LocallyLinearEmbedding(n_neighbors, n_components=2, method='ltsa')
t0 = time()
X_ltsa = clf.fit_transform(X)
plot_embedding(X_ltsa, "LTSA (time %.2fs)" % (time() - t0))


#8.MDS  embedding of the digits dataset
clf = manifold.MDS(n_components=2, n_init=1, max_iter=100)
t0 = time()
X_mds = clf.fit_transform(X)
plot_embedding(X_mds, "MDS embedding of the digits (time %.2fs)" %   (time() - t0))


#9. Random Trees embedding of the digits dataset
hasher = ensemble.RandomTreesEmbedding(n_estimators=200, random_state=0,   max_depth=5)
t0 = time()
X_transformed = hasher.fit_transform(X)
pca = decomposition.TruncatedSVD(n_components=2)
X_reduced = pca.fit_transform(X_transformed)
plot_embedding(X_reduced,  "RTE (time %.2fs)" %   (time() - t0))


#10. Spectral embedding of the digits dataset
embedder = manifold.SpectralEmbedding(n_components=2, random_state=0,  eigen_solver="arpack")
t0 = time()
X_se = embedder.fit_transform(X)
plot_embedding(X_se,  "SE (time %.2fs)" % (time() - t0))

