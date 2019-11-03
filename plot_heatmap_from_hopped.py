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
