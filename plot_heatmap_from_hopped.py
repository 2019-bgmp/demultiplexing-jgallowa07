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
header = indices.readline()
for index,barcode in enumerate(indices):
    barcode = barcode.strip().split()[4]
    barcode_index[barcode] = index


#print(len(barcode_index)) 

hopped_file_iterator = fastq_records_iterator(open(args.fq,"r"))
hopped_matrix = np.zeros([len(barcode_index),len(barcode_index)])
for i,record in enumerate(hopped_file_iterator):
    header = record[0].strip().split("_")
    bar1 = header[-2]
    bar2 = header[-1]
    
    bar2_rc = reverse_compliment(header[-1])
    print(bar2, bar2_rc)
    break
    hopped_matrix[barcode_index[bar2],barcode_index[bar1]] += 1

#plt.imshow(hopped_matrix)
#plt.show()
     




