'''
helpers.py

Author: Jared Galloway

This file contains some helpful functions to demultiplex a fastq file.
'''

def reverse_compliment(sequence):
    '''
    This function takes in a string representing a 
    sequence of DNA, and returns it's reverse compliment.
    '''
    map_nucleotide_dict = {"A":"T","T":"A","C":"G","G":"C","N":"N"}
    compliment = ""    
    for nucleotide in sequence:
        compliment += map_nucleotide_dict[nucleotide]
    return ''.join(list(reversed(compliment)))

def fastq_records_iterator(file_pointer):
    '''
    This function will take in a file pointer 
    and returns an iterator which yeilds four lines of a file
    (stripped of \n) in a list of strings. 
    '''
    while True:
        record = []
        for i in range(4):
            record.append(file_pointer.readline().strip())
        if record[0] == '':
            break
        else:
            yield record
    return None

def average_quality_score(phred_string):
    '''
    Take in a string of quality scores and compute the average.  
    '''
    average_score = 0
    for score in phred_string:
        average_score += convert_phred(score)
    return average_score/len(phred_string)

def convert_phred(letter):
    """Converts a single character into a phred score"""
    return ord(letter) - 33

def is_valid(index, indices, phred_string, quality_threshold):
    '''
    This function takes in a single index read,
    a list of indices, quality score string, 
    and a quality score threshold and returns 
    a boolean flag indicating whether or not that 
    '''
    index_exists = index in indices
    read_is_high_quality = average_quality_score(phred_string) > quality_threshold
    return index_exists & read_is_high_quality 
