#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 17:38:54 2021

@author: luca
"""

import io
import sys
import re
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.vq import kmeans, vq

#os.makedirs(os.path.join('data','kmeans'), exist_ok=True)
os.makedirs(os.path.join('data','kmeans','graphs'), exist_ok=True)


if len(sys.argv) != 2:
    sys.stderr.write("Arguments error. Usage:\n")
    sys.stderr.write("\tpython kmeans.py data-file\n")
    sys.exit(1)
    
samsungData = pd.read_csv(sys.argv[1])
samsungData = samsungData.drop(['Unnamed: 0'], axis=1)
subj1 = samsungData[samsungData['subject'] == 1]

data = np.matrix(subj1.iloc[:,:-2])
centers, _ = kmeans(data, 6, iter=100)
cluster, _ = vq(data, centers)

df = pd.crosstab(cluster, subj1['activity'])


fig = plt.figure()
idmax = np.argmax(np.array(df['laying']))
plt.plot(centers[idmax,:10], 'ok')
plt.ylabel('Cluster Center');
fig.savefig(os.path.join('data/kmeans/graphs/KmeansLaying.png'))

f = plt.figure()
idmax = np.argmax(np.array(df['walk']))

plt.plot(centers[idmax,:10], 'ok')
plt.ylabel('Cluster Center');
f.savefig(os.path.join('data/kmeans/graphs/KmeansWalk.png'))

