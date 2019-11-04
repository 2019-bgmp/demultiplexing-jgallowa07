#!/usr/bin/env python3
from matplotlib import pyplot as plt
import sys

c = [0,1,1,0]
r = [0,1,0,1]

fig, ax = plt.subplots(nrows=2,ncols=2, sharey=True)

for i in range(len(sys.argv)-1):
    filep = open(sys.argv[i+1],"r")
    dist = filep.readline().strip().split()
    dist = [float(x) for x in dist]
    ax[c[i]][r[i]].bar(x=range(len(dist)),height=dist,color="purple")
    ax[c[i]][r[i]].grid()
    ax[c[i]][r[i]].set_title(f"R_{i+1}")
    if c[i] == 1:
        ax[c[i]][r[i]].set_xlabel("$N_{th}$ nucleotide read")
    if r[i] == 0:
        ax[c[i]][r[i]].set_ylabel("Mean quality score")

fig.tight_layout()
fig.savefig("position_mean_quality.pdf")

