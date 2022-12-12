"""
Reverse complements a DNA sequence
"""

# Import required packages
import argparse
from typing import NamedTuple, List, TextIO
import os


# Define argument class
class Args(NamedTuple):
    """
    Command-line arguments
    """
    dna: str


# Get command line arguments
def get_args() -> Args:
    """
    Parse command line arguments
    """
    # Set-up parser object, using default help format
    parser = argparse.ArgumentParser(
        description='Print the reverse complement of a DNA sequence,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    # Add flagged argument to get DNA sequence or file
    parser.add_argument(
        'dna',
        help='Input sequence or file',
        metavar='DNA',
        type=str,
        default='out'
    )
    # Get arguments
    args = parser.parse_args()

    # Handle file inputs
    if os.path.isfile(args.dna):
        args.dna = open(args.dna).read().rstrip()

    # Return named tuple, also specified in function definition
    return Args(files=args.dna)


# Define main function
def main() -> None:
    """
    Main function
    """
    # Get arguments
    args = get_args()

    # Create reverse complement lookup
    # Using dictionary solution as I think it is most clear as to what is occuring
    # Caveat is that the code is potentially slower than using builtins or external functions
    lookup = {'A':'T','C':'G'}
    
    # Add pair of bases
    for key in lookup.keys():
        lookup[lookup[key]] = key
    
    # Add lower case support
    for key in lookup.keys():
        lookup[key.lower()] = lookup[key].lower()
    
    # Get complement
    complement = []
    for base in args.dna:
        complement.append(lookup[key])
    
    # Reverse complement
    print(''.join(reverse(complement)))


# Execute main
# Typical idiom for when the program is being executed
if __name__ == '__main__':
    main()
