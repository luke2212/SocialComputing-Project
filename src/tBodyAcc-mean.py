#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 15:16:34 2021

@author: luca
"""

import io
import sys
import re
import os
import yaml
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from scipy.spatial.distance import pdist, squareform
from scipy.cluster.hierarchy import linkage, dendrogram

#os.makedirs(os.path.join('data','tBodyAcc-mean'), exist_ok=True)
os.makedirs(os.path.join('data','tBodyAcc-mean','graphs'), exist_ok=True)

if len(sys.argv) != 2:
    sys.stderr.write("Arguments error. Usage:\n")
    sys.stderr.write("\tpython tBodyAcc-mean.py data-file\n")
    sys.exit(1)

'''
For each record in the dataset it is provided:
    - Triaxial acceleration from the accelerometer (total acceleration) and the estimated body acceleration.
    - Triaxial Angular velocity from the gyroscope. 
    - A 561-feature vector with time and frequency domain variables. 
    - Its activity label. 
    - An identifier of the subject who carried out the experiment.
'''
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
    ax1.scatter(df.index, df.iloc[:,0], c=cols[act], label=act)
    ax2.scatter(df.index, df.iloc[:,1], c=cols[act], label=act)

ax1.set_ylabel(samsungData.columns[0])
ax2.set_ylabel(samsungData.columns[1])
ax2.legend(loc='lower right')

f.tight_layout();
f.savefig(os.path.join('data/tBodyAcc-mean/graphs/tBodyAcc-mean.png'))

fig = plt.figure()
subj1 = samsungData[samsungData['subject'] == 1]
actlabels = pd.Categorical(subj1['activity'])

distanceMatrix = pdist(subj1.iloc[:,:3])
dendrogram(linkage(distanceMatrix, method='complete'), 
           color_threshold=0.3, 
           leaf_label_func=lambda x: 'O' * (actlabels.codes[x] + 1),
           leaf_font_size=6)

fig.set_size_inches(8, 4);
fig.savefig(os.path.join('data/tBodyAcc-mean/graphs/Dendogram.png'))

