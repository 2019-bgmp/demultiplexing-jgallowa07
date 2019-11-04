#!/usr/bin/env python3
import argparse
from collections import defaultdict
from matplotlib import pyplot as plt
import sys
import gzip
import numpy as np
from helpers import *

parser = argparse.ArgumentParser(description='This file is python code for \
    part one of the demultiplexing \
    assignment. This will read through \
    a fastQ file, and get a distribution \
    of quality scores for each bp position \
    in every read.')
parser = argparse.ArgumentParser()

parser.add_argument('-fq', type=str, help='fastq files to parse')
parser.add_argument('-bar', type=str, help='valid barcodes')
args = parser.parse_args()

barcode_index = {} 
indices = open(args.bar,"r")
indices_ref = []
header = indices.readline()
for index,barcode in enumerate(indices):
    barcode = barcode.strip().split()[4]
    indices_ref.append(barcode)
    barcode_index[barcode] = index

hopped_file_iterator = fastq_records_iterator(open(args.fq,"r"))
hopped_matrix = np.zeros([len(barcode_index),len(barcode_index)])
for i,record in enumerate(hopped_file_iterator):
    header = record[0].strip().split("_")
    bar1 = header[-2]
    bar2_rc = reverse_compliment(header[-1])
    hopped_matrix[barcode_index[bar2_rc],barcode_index[bar1]] += 1

fig, ax = plt.subplots()
im = ax.imshow(hopped_matrix)

ax.set_xticks(np.arange(len(indices_ref)))
ax.set_yticks(np.arange(len(indices_ref)))
# ... and label them with the respective list entries
ax.set_xticklabels(indices_ref)
ax.set_yticklabels(indices_ref)

# Rotate the tick labels and set their alignment.
plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
         rotation_mode="anchor")

# Loop over data dimensions and create text annotations.
#for i in range(len(indices_ref)):
#    for j in range(len(indices_ref)):
#        text = ax.text(j, i, hopped_matrix[i, j],
#                       ha="center", va="center", color="w")

plt.show()
     




