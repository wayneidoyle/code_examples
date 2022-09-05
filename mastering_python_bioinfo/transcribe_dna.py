"""
Transcribes a DNA sequence into an RNA sequence
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
    # List of open file handles
    files: List[TextIO]
    # Output directory stored as string
    out_dir: str


# Get command line arguments
def get_args() -> Args:
    """
    Parse command line arguments
    """
    # Set-up parser object, using default help format
    parser = argparse.ArgumentParser(
        description='Transcribe DNA into RNA',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    # Add flagged argument to get output directory
    parser.add_argument(
        '-o',
        '--out_dir',
        help='Output directory',
        metavar='DIR',
        type=str,
        default='out'
    )
    # Add positional argument to take n input files
    # For nargs:
    #   An integer value can be used to specify exact numbers
    #   ?: zero or one arguments
    #   *: zero or more arguments
    #   +: one or more arguments
    # rt indicates that input must be readable text
    parser.add_argument(
        'file',
        help='Input DNA file(s)',
        metavar='FILE',
        nargs='+',
        type=argparse.FileType('rt')
    )
    # Get arguments
    args = parser.parse_args()
    # Return named tuple, also specified in function definition
    return Args(files=args.file, out_dir=args.out_dir)


# Define main function
def main() -> None:
    """
    Main function
    """
    # Get arguments
    args = get_args()

    # Make output directory
    if not os.path.isdir(args.out_dir):
        os.makedirs(args.out_dir)

    # Initialize variables
    num_files, num_seqs = 0, 0

    # Loop over files and transcribe
    for input_fh in args.files:
        # Auto increment number of files processed
        num_files += 1
        # Determine output file name
        # Will use input file basename marged with output dir
        out_file = os.path.join(args.out_dir,
                                os.path.basename(input_fh.name))
        # Open output file for writing
        # Writing modes
        #   w: write (will overwrite existing file contents)
        #   r: read
        #   a: append (add to existing file contents)
        # Content modes:
        #   t: text
        #   b: bytes
        with open(out_file,
                  'wt',
                  encoding='utf-8') as out_fh:
            # Open input files and transcribe each line
            for raw_dna in input_fh:
                # Replace thymines with uracils
                # Not stripping new lines
                # This allows new lines to be transferred to new file
                out_fh.write(raw_dna.replace('T', 'U'))
                # Auto-increment number of sequences
                num_seqs += 1
    # Tell user we are done
    if num_files == 1:
        file_suffix = ''
    elif num_files > 1:
        file_suffix = 's'
    else:
        raise RuntimeError('No files found')
    if num_seqs == 1:
        seq_suffix = ''
    elif num_seqs > 1:
        seq_suffix = 's'
    else:
        raise RuntimeError('No sequences found')
    print(f'Done, wrote {num_seqs} sequence{seq_suffix}',
          f'in {num_files} file{file_suffix}',
          f'to directory "{args.out_dir}".')


# Execute main
# Typical idiom for when the program is being executed
if __name__ == '__main__':
    main()
