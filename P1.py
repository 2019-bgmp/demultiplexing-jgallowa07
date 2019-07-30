#!/usr/bin/env python3
import argparse
from collections import defaultdict
from matplotlib import pyplot as plt
import sys

parser = argparse.ArgumentParser(description='This file is python code for part one of the demultiplexing \
    assignment. This will read through a fastQ file, and get a distribution of quality scores for each bp position 
    in every read.')
parser = argparse.ArgumentParser()

parser.add_argument('-f', type=str, help='files to parse')
parser.add_argument('-mbp', type=str, help='where to output buckets')

args = parser.parse_args()



