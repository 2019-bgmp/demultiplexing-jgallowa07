#!/usr/bin/env python3
import argparse
from collections import defaultdict
from matplotlib import pyplot as plt
import matplotlib
import sys
import gzip
import numpy as np
from helpers import *
import os

parser = argparse.ArgumentParser(description='This file is python code for \
    part one of the demultiplexing \
    assignment. This will read through \
    a fastQ file, and get a distribution \
    of quality scores for each bp position \
    in every read.')
parser = argparse.ArgumentParser()

parser.add_argument('-fq', type=str, help='hopped fastq file to parse.')
parser.add_argument('-bar', type=str, help='valid barcodes')
args = parser.parse_args()

# https://matplotlib.org/3.1.1/gallery/images_contours_and_fields/image_annotated_heatmap.html
def heatmap(data, row_labels, col_labels, ax=None,
            cbar_kw={}, cbarlabel="", **kwargs):
    """
    Create a heatmap from a numpy array and two lists of labels.

    Parameters
    ----------
    data
        A 2D numpy array of shape (N, M).
    row_labels
        A list or array of length N with the labels for the rows.
    col_labels
        A list or array of length M with the labels for the columns.
    ax
        A `matplotlib.axes.Axes` instance to which the heatmap is plotted.  If
        not provided, use current axes or create a new one.  Optional.
    cbar_kw
        A dictionary with arguments to `matplotlib.Figure.colorbar`.  Optional.
    cbarlabel
        The label for the colorbar.  Optional.
    **kwargs
        All other arguments are forwarded to `imshow`.
    """

    if not ax:
        ax = plt.gca()

    # Plot the heatmap
    im = ax.imshow(data, **kwargs)

    # Create colorbar
    cbar = ax.figure.colorbar(im, ax=ax, **cbar_kw)
    cbar.ax.set_ylabel(cbarlabel, rotation=-90, va="bottom")

    # We want to show all ticks...
    ax.set_xticks(np.arange(data.shape[1]))
    ax.set_yticks(np.arange(data.shape[0]))
    # ... and label them with the respective list entries.
    ax.set_xticklabels(col_labels, fontsize = 5)
    ax.set_yticklabels(row_labels, fontsize = 5)

    # Let the horizontal axes labeling appear on top.
    ax.tick_params(top=True, bottom=False,
                   labeltop=True, labelbottom=False)

    # Rotate the tick labels and set their alignment.
    plt.setp(ax.get_xticklabels(), rotation=-30, ha="right",
             rotation_mode="anchor")

    # Turn spines off and create white grid.
    for edge, spine in ax.spines.items():
        spine.set_visible(False)

    ax.set_xticks(np.arange(data.shape[1]+1)-.5, minor=True)
    ax.set_yticks(np.arange(data.shape[0]+1)-.5, minor=True)
    ax.grid(which="minor", color="w", linestyle='-', linewidth=2)
    ax.tick_params(which="minor", bottom=False, left=False)

    return im, cbar


if __name__ == "__main__":

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

    hopped_matrix = np.log(hopped_matrix + 1.5)
    fig, ax = plt.subplots()
    im, cbar = heatmap(hopped_matrix, indices_ref, indices_ref, ax=ax,
                       cmap="YlGn", cbarlabel="log(number of hopped indices)")
    fig.tight_layout()
    fig.savefig("heatmap.pdf")


