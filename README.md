# Demultiplexing

This repository contains source code to demultiplex four gzipped fastq files: 1 forward read, 2 forward index, reverse index, 4 reverse read, respectively.
The script also need a file which specifies the valid barcodes for which to demultiplex the biological reads in the following tab-seperated format

```
ample   group   treatment   index   index sequence
1   2A  control B1  GTAGCGTA
2   2B  control A5  CGATCGAT
3   2B  control C1  GATCAAGG
4   2C  mbnl    B9  AACAGCGA
6   2D  mbnl    C9  TAGCCATG
7   2E  fox C3  CGGTAATC
8   2F  fox B3  CTCTGGAT
10  2G  both    C4  TACCGGAT
11  2H  both    A11 CTAGCTCA
```

Given these, the script found in `scripts/demultiplex.py` has the following usage:

```bash
age: demultiplex.py [-h] [-fq FQ [FQ ...]] [-bar BAR] [-out OUT]

This file is python code for

optional arguments:
  -h, --help       show this help message and exit
  -fq FQ [FQ ...]  gzipped fastq files to de-multiplex (should be 4: 1 forward
                   read, 2 forward index, 3 reverse index, 4 reverse read)
  -bar BAR         properly formatted list of valid barcodes to demultiplex.
  -out OUT         output directory for which to write you files - must exist
                   before runtime.
```

An example run for this might look like:

```
/usr/bin/time -v ./demultiplex.py -fq ../emp_files/*.gz -bar ../emp_files/indexes.txt -out ../demultiplexed_files/
```

This output all demultiplexed files names with R1 and R2 followed by the barcode for the resepective file.
This script writes percentages and counts for each barcode to stdout like so:

```
Number of hopped reads = 707740
Number of undefined reads = 30783962
Number of valid reads = 331755033

Sample Barcode  Total # Records Percentage of Total
GTAGCGTA    8119243     2.447
CGATCGAT    5604966     1.689
GATCAAGG    6587100     1.986
AACAGCGA    8872034     2.674
TAGCCATG    10629633    3.204
CGGTAATC    5064906     1.527
CTCTGGAT    34976387    10.543
TACCGGAT    76363857    23.018
```

Once the files have been demultiplexed, you can visualize which barcode hopped the most with the script found in `scripts/plot_heatmap_from_hopped.py` like so

```
/usr/bin/time -v ./plot_heatmap_from_hopped.py -fq ../demultiplexed_files/R1_hopped.fastq -bar ../emp_files/indexes.txt
```

to produce a plot that looks like:

![alt text](https://github.com/2019-bgmp/demultiplexing-jgallowa07/blob/master/plots/heatmap.pdf)








