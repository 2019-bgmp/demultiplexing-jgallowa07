#!/usr/bin/env python3
"""
P2 Psuedo Code

This script 

"""
import argparse
from collections import defaultdict
import sys
import gzip
import numpy as np
from helpers import *

QUALITY_CUTOFF = 0

# TODO Create nice description
parser = argparse.ArgumentParser(description='This file is python code for')

parser.add_argument('-fq', type=str, nargs='+',
    help='gzipped fastq files to de-multiplex \
    (should be 4: 1 forward read, 2 forward index, \
    3 reverse index, 4 reverse read)')
parser.add_argument('-fi', type=str, help='number \
    of base pairs in each read (or max)')
args = parser.parse_args()

# 1:
# read in indices, and create a dictionary, 
# fp_dict defined by
# {R1/R2_INDEX : file pointer for that index}
"""
fp_dict = {}
ref_indices = []
demult_dir = "demultiplexed_files/"
indices = open(args.fi,"r")
header = indices.readline()
"""

# 2: 
# populate the dictionary by looping through the indices,
# and creating a file pointer for each file.
"""
for line in indices:
    index = line.strip().split()[4]
    ref_indices.append(index)
    r1_file_pointer = open(f"{demult_dir}R1_{index}.fastq","w")
    r2_file_pointer = open(f"{demult_dir}R2_{index}.fastq","w")
    fp_dict[f"R1_{index}"] = r1_file_pointer
    fp_dict[f"R2_{index}"] = r2_file_pointer
fp_dict["R1_hopped"] = open(f"{demult_dir}R1_hopped.fastq","w")
fp_dict["R2_hopped"] = open(f"{demult_dir}R2_hopped.fastq","w")
fp_dict["R1_undefined"] = open(f"{demult_dir}R1_undefined.fastq","w")
fp_dict["R2_undefined"] = open(f"{demult_dir}R2_undefined.fastq","w")
"""

# 3:
# create iterators in a list using function from helpers.py
# fi = [fastq_records_iterator(gzip.open(args.fq[i],"rt")) for i in range(4)]

# 4: 
# Now, lets iterate through fragments and determin which 
# file the record should be written to.
"""
for r1_read_r, r1_idx_r, r2_idx_r, r2_read_r in zip(fi[0],fi[1],fi[2],fi[3]):

    # grab the indices -- remembering that the reverse must be reverse complimented
    # so that we may compare/validate
    r1_idx = r1_idx_r[1]
    r1_idx_qs = r1_idx_r[3]
    r2_idx = reverse_compliment(r2_idx_r[1])
    r2_idx_qs = r2_idx_r[3]

    # first, find out if the indices are valid
    r1_idx_valid = is_valid(r1_idx, ref_indices, r1_idx_qs, QUALITY_CUTOFF)
    r2_idx_valid = is_valid(r2_idx, ref_indices, r2_idx_qs, QUALITY_CUTOFF)

    # modify the headers of both records to include the indices
    r1_read_r[0] = f"{r1_read_r[0]}_{r1_idx}_{r2_idx}"
    r2_read_r[0] = f"{r2_read_r[0]}_{r1_idx}_{r2_idx}"

    #If both indices are valid, then they're either index hopped of valid
    if r1_idx_valid & r2_idx_valid:
        # If the indices are valid and match, then they are good to de-multiplex
        if r1_idx == r2_idx:
            fp_dict[f"R1_{r1_idx}"].write("\n".join(r1_read_r)+"\n")
            fp_dict[f"R2_{r2_idx}"].write("\n".join(r2_read_r)+"\n")
        # if they don't match, and are valid, then they hopped 
        else:
            fp_dict["R1_hopped"].write("\n".join(r1_read_r)+"\n")
            fp_dict["R2_hopped"].write("\n".join(r2_read_r)+"\n")
    # If either of the indices are not valid, then we catagorize as undefined 
    else:
        fp_dict["R1_undefined"].write("\n".join(r1_read_r)+"\n")
        fp_dict["R2_undefined"].write("\n".join(r2_read_r)+"\n")
"""

