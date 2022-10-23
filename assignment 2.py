
def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    
    >>> get_length('ATCG')
    4
    """
    return len(dna)

def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """
    return len(dna1) > len(dna2)

def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    num_nucl = 0
    for letter in dna:
       if letter in nucleotide:
           num_nucl = num_nucl + 1
    return num_nucl

def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """
    return dna2 in dna1



def is_valid_sequence(dna):
    """(str) -> bool


    Return if the sequence dna is valid or not. The sequence should not be blank or in lower case.

    >>>is_valid_sequence('ATCH')
    False
    >>>is_valid_sequence('ATCG')
    True
    """
    nucl = ''
    for letter in dna:
        if letter in 'ATCG':
            nucl = nucl + letter
    return len(nucl) == len(dna)


def insert_sequence(dna1, dna2, index):
    """(str, str, int) -> str
​
    Return the DNA sequence obtained
    by inserting the dna2 into dna1 at the given index. 

    >>>insert_sequence('CCGG', 'AT', 2)
    CCATGG
    >>>insert_sequence('CGATC', 'AT', 4)
    CGATATC
    """
    return dna1[:index] + dna2 + dna1[index:]     

def get_complement(nucleotide):
    """ (str) -> str

    Return the complement of the nucleotide. Enter only nucleotides:A, T, C, G,one value.

    >>>get_complement('A')
    'T'
    >>>get_complement('C')
    'G'
    """
    if nucleotide in 'ATCG' and len(nucleotide) == 1:
        if nucleotide == 'A':
            return 'T'
        if nucleotide == 'T':
            return 'A'
        if nucleotide == 'C':
            return 'G'
        if nucleotide == 'G':
            return 'C'
    else:
        return 'Incorrect nucleotide input'

def get_complementary_sequence(dna):
    """(str) -> str

    Return the DNA sequence that is complementary to dna.

    >>> get_complementary_sequence('AT')
    'TA'tt
    >>> get_complementary_sequence('ATCG')
    'TAGC'
    """
    sequence = ''
    for letter in dna:
        if letter == 'A':
            sequence = sequence + 'T'
        elif letter == 'T':
            sequence = sequence + 'A'
        elif letter == 'C':
            sequence = sequence + 'G'
        elif letter == 'G':
            sequence = sequence + 'C'
    return sequence 	
        
