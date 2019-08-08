#!/usr/bin/env python3
import argparse
from collections import defaultdict
from matplotlib import pyplot as plt
import sys
import gzip
import numpy as np

parser = argparse.ArgumentParser(description='This file is python code for \
    part one of the demultiplexing \
    assignment. This will read through \
    a fastQ file, and get a distribution \
    of quality scores for each bp position \
    in every read.')
parser = argparse.ArgumentParser()

parser.add_argument('-f', type=str, help='fastq files to parse')
parser.add_argument('-nbp', type=int, help='number of base pairs in each read (or max)')

args = parser.parse_args()

def convert_phred(letter):
    """Converts a single character into a phred score"""
    return ord(letter) - 33

quality_score_sums = np.zeros(args.nbp)
num_records = 0
with gzip.open(args.f, 'rt') as fqfp:
    for LN,line in enumerate(fqfp):
        if(LN%4==3):
            num_records += 1 
            for nt,score in enumerate(line.strip()):
                quality_score_sums[nt] += convert_phred(score)

outfile = open(args.f + "_mps.tsv","w")
outfile.write("\t".join([str(x/num_records) for x in quality_score_sums]))

