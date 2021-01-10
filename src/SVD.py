#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 16:49:51 2021

@author: luca
"""

import io
import sys
import re
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.distance import pdist, squareform
from scipy.cluster.hierarchy import linkage, dendrogram

#os.makedirs(os.path.join('data','svd'), exist_ok=True)
os.makedirs(os.path.join('data','svd','graphs'), exist_ok=True)


if len(sys.argv) != 2:
    sys.stderr.write("Arguments error. Usage:\n")
    sys.stderr.write("\tpython SVD.py data-file\n")
    sys.exit(1)
    
    
samsungData = pd.read_csv(sys.argv[1])
samsungData = samsungData.drop(['Unnamed: 0'], axis=1)
subj1 = samsungData[samsungData['subject'] == 1]
actlabels = pd.Categorical(subj1['activity'])


# a simple scale function to normalize a matrix
def scale(matrix):
    return (matrix - np.mean(matrix, axis=0)) / np.std(matrix, axis=0)



U, D, Vt = np.linalg.svd(subj1.iloc[:,:-2].apply(scale), full_matrices=False)

f, (ax1, ax2) = plt.subplots(ncols=2)
f.set_size_inches(10, 5)

for lb, cl in zip(list(actlabels.categories), 'b g r c m y k'.split()):
    idx = subj1['activity'] == lb
    ax1.scatter(subj1.index[idx], U[idx,0], c=cl, label=lb)
    ax2.scatter(subj1.index[idx], U[idx,1], c=cl, label=lb)
    
ax1.set_ylabel('U[:,0]')
ax2.set_ylabel('U[:,1]')
ax2.legend(loc='lower right')

f.tight_layout();
f.savefig(os.path.join('data/svd/graphs/SVD.png'))

fig = plt.figure()
maxContrib = np.argmax(Vt[1,:])

distanceMatrix = pdist(subj1.take(list(range(9,12)) + [maxContrib], axis=1))
dendrogram(linkage(distanceMatrix, method='complete'), 
           color_threshold=0.3, 
           leaf_label_func=lambda x: 'O' * (actlabels.codes[x] + 1),
           leaf_font_size=6)
fig.set_size_inches(8, 4);
fig.savefig(os.path.join('data/svd/graphs/Dendogram.png'))
