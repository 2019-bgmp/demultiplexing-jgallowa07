#!/usr/bin/env python3
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

# read in indices, and create a dictionary, 
# fp_dict defined by
# {FW/RV_INDEX : file pointer for that index}
fp_dict = {}
ref_indices = []
demult_dir = "demultiplexed_files/"
indices = open(args.fi,"r")
header = indices.readline()
for line in indices:
    index = line.strip().split()[4]
    ref_indices.append(index)
    fw_file_pointer = open(f"{demult_dir}FW_{index}.fastq","w")
    rv_file_pointer = open(f"{demult_dir}RV_{index}.fastq","w")
    fp_dict[f"FW_{index}"] = fw_file_pointer
    fp_dict[f"RV_{index}"] = rv_file_pointer
fp_dict["FW_hopped"] = open(f"{demult_dir}FW_hopped.fastq","w")
fp_dict["RV_hopped"] = open(f"{demult_dir}RV_hopped.fastq","w")
fp_dict["FW_undefined"] = open(f"{demult_dir}FW_undefined.fastq","w")
fp_dict["RV_undefined"] = open(f"{demult_dir}RV_undefined.fastq","w")

# Put record iterators in a list using function from helpers.py
fi = [fastq_records_iterator(gzip.open(args.fq[i],"rt")) for i in range(4)]

# Now, lets iterate through fragments
for fw_read_r, fw_idx_r, rv_idx_r, rv_read_r in zip(fi[0],fi[1],fi[2],fi[3]):

    # grab the indices -- remembering that the reverse must be reverse complimented
    # so that we may compare/validate
    fw_idx = fw_idx_r[1]
    fw_idx_qs = fw_idx_r[3]
    rv_idx = reverse_compliment(rv_idx_r[1])
    rv_idx_qs = rv_idx_r[3]

    # first, find out if the indices are valid
    fw_idx_valid = is_valid(fw_idx, ref_indices, fw_idx_qs, QUALITY_CUTOFF)
    rv_idx_valid = is_valid(rv_idx, ref_indices, rv_idx_qs, QUALITY_CUTOFF)

    # modify the headers of both records to include the indices
    fw_read_r[0] = f"{fw_read_r[0]}_{fw_idx}_{rv_idx}"
    rv_read_r[0] = f"{rv_read_r[0]}_{fw_idx}_{rv_idx}"

    #If both indices are valid, then they're either index hopped of valid
    if fw_idx_valid & rv_idx_valid:
        # If the indices are valid and match, then they are good to de-multiplex
        if fw_idx == rv_idx:
            fp_dict[f"FW_{fw_idx}"].write("\n".join(fw_read_r)+"\n")
            fp_dict[f"RV_{rv_idx}"].write("\n".join(rv_read_r)+"\n")
        # if they don't match, and are valid, write to 
        else:
            fp_dict["FW_hopped"].write("\n".join(fw_read_r)+"\n")
            fp_dict["RV_hopped"].write("\n".join(rv_read_r)+"\n")
    # If either of the indices are not valid, then we catagorize as undefined 
    else:
        fp_dict["FW_undefined"].write("\n".join(fw_read_r)+"\n")
        fp_dict["RV_undefined"].write("\n".join(rv_read_r)+"\n")

