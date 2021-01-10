#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 16:38:44 2021

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

#os.makedirs(os.path.join('data','tBodyAcc-max'), exist_ok=True)
os.makedirs(os.path.join('data','tBodyAcc-max','graphs'), exist_ok=True)


if len(sys.argv) != 2:
    sys.stderr.write("Arguments error. Usage:\n")
    sys.stderr.write("\tpython tBodyAcc-max.py data-file\n")
    sys.exit(1)


samsungData = pd.read_csv(sys.argv[1])
samsungData = samsungData.drop(['Unnamed: 0'], axis=1)
subj1 = samsungData[samsungData['subject'] == 1]

numericActivity = subj1.groupby('activity')
cols = {'laying' : 'b',
        'sitting' : 'g',
        'standing' : 'r',
        'walk' : 'c',
        'walkdown' : 'm',
        'walkup' : 'y'}

f, (ax1, ax2) = plt.subplots(ncols=2)
f.set_size_inches(10, 5)

for act, df in numericActivity:
    ax1.scatter(df.index, df.iloc[:,9], c=cols[act], label=act)
    ax2.scatter(df.index, df.iloc[:,10], c=cols[act], label=act)

ax1.set_ylabel(samsungData.columns[9])
ax2.set_ylabel(samsungData.columns[10])
ax2.legend(loc='lower right')

f.tight_layout();
f.savefig(os.path.join('data/tBodyAcc-max/graphs/tBodyAcc-max.png'))

fig = plt.figure()
actlabels = pd.Categorical(subj1['activity'])
distanceMatrix = pdist(subj1.iloc[:,9:12])
dendrogram(linkage(distanceMatrix, method='complete'), 
           color_threshold=0.3, 
           leaf_label_func=lambda x: 'O' * (actlabels.codes[x] + 1),
           leaf_font_size=6)

fig.set_size_inches(8, 4);
fig.savefig(os.path.join('data/tBodyAcc-max/graphs/Dendogram.png'))