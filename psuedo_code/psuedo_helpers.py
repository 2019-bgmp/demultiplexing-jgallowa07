'''
helpers.py

Author: Jared Galloway

This file contains some helpful functions to demultiplex a fastq file.
'''

def reverse_compliment_stub(sequence):
    '''
    This function takes in a string representing a 
    sequence of DNA, and returns it's reverse compliment.
    '''
    pass

def fastq_records_iterator_stub(file_pointer):
    '''
    This function will take in a file pointer 
    and returns an iterator which yeilds four lines of a file
    (stripped of \n) in a list of strings. 
    '''
    pass

def average_quality_score_stub(phred_string):
    '''
    Take in a string of quality scores and compute the average.  
    '''
    pass

def convert_phred_stub(letter):
    """Converts a single character into a phred score"""
    pass

def is_valid_stub(index, indices, phred_string, quality_threshold):
    '''
    This function takes in a single index read,
    a list of indices, quality score string, 
    and a quality score threshold and returns 
    a boolean flag indicating whether or not that 
    '''
    pass
