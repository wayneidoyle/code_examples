""""Tests nucelotide_freq.py"""

import os #Used to interact with filesystem
from subprocess import getstatusoutput #Capture outputs

# Set program to be tested
PRG ="../nucleotide_freq.py"

# Set method for invocation
RUN = f'python3 {PRG}' 

# Define tests and results
# Order of results is A T G C N
TEST1 = ('./inputs/nucleotide_freq_input_1.txt', 
    'A:3 T:4 G:2 C:2 N:0')
TEST2 = ('./inputs/nucleotide_freq_input_2.txt', 
    'A:1 T:0 G:3 C:0 N:0')
TEST3 = ('./inputs/nucleotide_freq_input_3.txt', 
    'A:0 T:21 G:0 C:0 N:1')

# Before proceeding make sure program actually exists
def test_exists() -> None:
    """
    Ensure program exists
    """

    assert os.path.exists(PRG)

# Next make sure that a help function exists
def test_usage() -> None:
    """
    Checks that a usage statement exists
    """

    for arg in ['-h', '--help']:
        # Tests both short and long forms of help
        rv, out = getstatusoutput(f'{RUN} {arg}')
        # Ensure that the program successfully ended (0 exit status)
        assert rv == 0
        # Ensure that the help output starts with usage
        assert out.lower().startswith('usage:')

# Ensure that the program dies with no inputs
def test_dies_no_args() -> None:
    """
    Confirm that the program dies if arguments are not passed
    """
    
    rv, out = getstatusoutput(RUN)
    # Ensure return value is not zero
    assert rv != 0
    # Ensure help is printed
    assert out.lower().startswith('usage:')

# Perform integration test
# Test to see if run as a user does correct output get generated
# Checks if all functions work together appropriately
# Does not check that each function works as expected (i.e., unit testing)
def test_arg():
    """
    Tests if program works with string input being passed
    """

    for file, expected in [TEST1, TEST2, TEST3]:
        # Read in sequence
        dna = open(file).read()
        # Run program on string
        rv, out = getstatusoutput(f'{RUN} {dna}')
        # Confirm that exit status is zero
        assert rv == 0
        # Confirm output matches expectation
        assert out == expected

def test_file():
    """
    Tests if program works with file inputs
    """
    
    for file, expected in [TEST1, TEST2, TEST3]:
        # Run program on string
        rv, out = getstatusoutput(f'{RUN} {file}')
        # Confirm that exit status is zero
        assert rv == 0
        # Confirm output matches expectation
        assert out == expected
