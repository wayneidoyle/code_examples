"""
Count nucelotide frequency from a provided DNA sequence
"""

# Import required packages
import argparse
from typing import NamedTuple, Tuple, Dict
from collections import defaultdict
import os


# Define classes
class Args(NamedTuple):
    """
    Tuple for command line arguments
    """
    # This is being done so that I
    #   1) Have passed arguments be immutable
    #   2) Specify types of inputs
    # In this definiton I am creating a class that has:
    #   1) a single field of type str
    dna: str


# Get command line arguments
def get_args() -> Args:
    """
    Parse command line arguments
    """
    # Set-up parser object, using default help format
    parser = argparse.ArgumentParser(
        description='Nucleotide frequency',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    # Add positional argument for passing in DNA sequences
    # metavar is a short description of the argument
    #   will appear in the help
    # help is the printed help message for the argument
    parser.add_argument(
        'dna',
        metavar='DNA',
        help='Input DNA sequence'
    )
    # Get arguments
    args = parser.parse_args()
    # Handle situations when input is a file rather than a str
    if os.path.isfile(args.dna):
        args.dna = open(args.dna).read().rstrip()
    # Return named tuple, also specified in function definition
    return Args(args.dna)


# Define main function
def main() -> None:
    """
    Main function
    """
    # No return in main so setting None as default returned value
    args = get_args()
    count_a, count_t, count_g, count_c, count_n = count(args.dna)
    print(f'A:{count_a} T:{count_t} G:{count_g} C:{count_c} N:{count_n}')


# Define subroutines
def count(dna: str) -> Tuple[int, int, int, int, int]:
    """
    Counts bases (A,T,C,G,N) from a DNA sequence
    Considers any base that is not an A,T,C,G as an N
    """

    # Initialize default dictionary
    counts: Dict[str, int] = defaultdict(int)

    # Loop over and make dictionary with bases
    for base in dna:
        counts[base.lower()] += 1

    # Get counts for each base
    # Defaults to 0 if not present
    count_a = counts.get('a', 0)
    count_t = counts.get('t', 0)
    count_g = counts.get('g', 0)
    count_c = counts.get('c', 0)
    count_n = len(dna) - count_a - count_t - count_g - count_c

    # Return counts
    return (count_a, count_t, count_g, count_c, count_n)


def test_count() -> None:
    """
    Perform unit test of count function
    """

    assert count('') == (0, 0, 0, 0, 0)
    assert count('123XYZ') == (0, 0, 0, 0, 6)
    assert count('A') == (1, 0, 0, 0, 0)
    assert count('T') == (0, 1, 0, 0, 0)
    assert count('G') == (0, 0, 1, 0, 0)
    assert count('C') == (0, 0, 0, 1, 0)
    assert count('ATGC') == (1, 1, 1, 1, 0)


# Execute main
# Typical idiom for when the program is being executed
if __name__ == '__main__':
    main()
