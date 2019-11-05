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


