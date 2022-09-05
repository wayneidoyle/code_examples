""""Tests transcribe_dna_test.py"""

import os #Used to interact with filesystem
from subprocess import getstatusoutput #Capture outputs
import random
import re
import shutil
import string

# Set program to be tested
PRG ="../transcribe_dna.py"

# Set method for invocation
RUN = f'python3 {PRG}' 

# Set tests
INPUT1 = './inputs/transcribe_dna_input_1.txt'
INPUT2 = './inputs/transcribe_dna_input_2.txt'
INPUT3 = './inputs/transcribe_dna_input_3.txt'


def test_exists() -> None:
    """
    Checks that the program exists
    """

    assert os.path.isfile(PRG)

def test_usage() -> None:
    """
    Checks that usage is printed
    """
    for flag in ['-h', '--help']:
        rv, out = getstatusoutput(f'{RUN} {flag}')
        assert rv == 0
        assert out.lower().startswith('usage:')


def test_no_args() -> None:
    """
    Check script dies with out arguments
    """

    rv, out = getstatusoutput(RUN)
    assert rv != 0
    assert out.lower().startswith('usage:')


def test_bad_file() -> None:
    """
    Check script dies if an existing filename is not passed
    """

    bad_file = random_filename()
    rv, out = getstatusoutput(f'{RUN} {bad_file}')
    assert rv != 0
    assert re.match('usage:', out, re.IGNORECASE)
    assert re.search(f"No such file or directory: '{bad_file}'", out)

def test_good_input1() -> None:
    """
    Check script runs on good input (test 1)
    """

    out_dir = 'out'
    try:
        # If testing output directory exists, delete it
        if os.path.isdir(out_dir):
            # Removes directory and contents
            shutil.rmtree(out_dir)
        # Run test
        rv, out = getstatusoutput(f'{RUN} {INPUT1}')
        assert rv == 0
        assert out == 'Done, wrote 1 sequence in 1 file to directory "out".'
        assert os.path.isdir(out_dir)
        out_file = os.path.join(out_dir, 'transcribe_dna_input_1.txt')
        assert os.path.isfile(out_file)
        assert open(out_file).read().rstrip() == 'GAUGGAACUUGACUACGUAAAUU'
    finally:
        # Clean up testing environment
        # Run no matter what
        if os.path.isdir(out_dir):
            shutil.rmtree(out_dir)

def test_good_input2() -> None:
    """
    Check script runs on good input (test 2)
    """

    out_dir = random_filename()
    try:
        if os.path.isdir(out_dir):
            shutil.rmtree(out_dir)
        rv, out = getstatusoutput(f'{RUN} -o {out_dir} {INPUT2}')
        assert rv == 0
        assert out == (f'Done, wrote 2 sequences in 1 file to '
                       f'directory "{out_dir}".')
        assert os.path.isdir(out_dir)
        out_file = os.path.join(out_dir, 'transcribe_dna_input_2.txt')
        assert os.path.isfile(out_file)
        assert open(out_file).read().rstrip() == '\n'.join(
            ['UUAGCCCAGACUAGGACUUU', 'AACUAGUCAAAGUACACC'])

    finally:
        if os.path.isdir(out_dir):
            shutil.rmtree(out_dir)


def test_good_multiple_inputs():
    """
    Check that script runs on multiple inputs
    """

    out_dir = random_filename()
    try:
        if os.path.isdir(out_dir):
            shutil.rmtree(out_dir)
        rv, out = getstatusoutput(
            f'{RUN} --out_dir {out_dir} {INPUT1} {INPUT2} {INPUT3}')
        assert rv == 0
        assert out == (f'Done, wrote 5 sequences in 3 files to '
                       f'directory "{out_dir}".')
        assert os.path.isdir(out_dir)
        out_file1 = os.path.join(out_dir, 
                                 'transcribe_dna_input_1.txt')
        out_file2 = os.path.join(out_dir, 
                                 'transcribe_dna_input_2.txt')
        out_file3 = os.path.join(out_dir, 
                                 'transcribe_dna_input_3.txt')
        assert os.path.isfile(out_file1)
        assert os.path.isfile(out_file2)
        assert os.path.isfile(out_file3)
        assert open(out_file1).read().rstrip() == 'GAUGGAACUUGACUACGUAAAUU'
        assert open(out_file2).read().rstrip() == '\n'.join(
            ['UUAGCCCAGACUAGGACUUU', 'AACUAGUCAAAGUACACC'])
        assert open(out_file3).read().rstrip() == output3().rstrip()

    finally:
        if os.path.isdir(out_dir):
            shutil.rmtree(out_dir)


# --------------------------------------------------
def output3() -> str:
    """ Output for 3rd input """

    return '\n'.join([('CUUAGGUCAGUGGUCUCUAAACUUUCGGUUCUGUCGUCUUCAUAGGCAAA'
                       'UUUUUGAACCGGCAGACAAGCUAAUCCCUGUGCGGUUAGCUCAAGCAACA'
                       'GAAUGUCCGAUCUUUGAACUUCCUAACGAACCGAACCUACUAUAAUUACA'
                       'UACGAAUAAUGUAUGGGCUAGCGUUGGCUCAUCAUCAAGUCUGCGGUGAA'
                       'AUGGGAACAUAUUCGCAUUGCAUAUAGGGCGUAUCUGACGAUCGAUUCGA'
                       'GUUGGCUAGUCGUACCAAAUGAUUAUGGGCUGGAGGGCCAAUGUAUACGU'
                       'CAGCCAGGCUAAACCACUGGACCGCUUGCAAUCCAUAGGAAGUAAAAUUA'
                       'CCCUUUUUAAACUCUCUAAGAUGUGGCGUCUCGUUCUUAAGGAGUAAUGA'
                       'GACUGUGACAACAUUGGCAAGCACAGCCUCAGUAUAGCUACAGCACCGGU'
                       'GCUAAUAGUAAAUGCAAACACCGUUUCAAGAGCCGAGCCUUUUUUUAAUG'
                       'CAAGGUGACUUCAGAGGGAGUAAAUCGUGGCCGGGGACUGUCCAGAGCAA'
                       'UGCAUUCCCGAGUGCGGGUACCCGUGGUGUGAGAGGAAUCGAUUUCGCGU'
                       'GUGAUACCAUUAAUGGUCCUGUACUACUGUCAGUCAGCUUGAUUUGAAGU'
                       'CGGCCGACAAGGUUGGUACAUAAUGGGCUUACUGGGAGCUUAGGUUAGCC'
                       'UCUGGAAAACUUUAGAAUUUAUAUGGGUGUUUCUGUGUUCGUACAGGCCC'
                       'CAGUCGGGCCAUCGUUGUUGAGCAUAGACCGGUGUAACCUUAAUUAUUCA'
                       'CAGGCCAAUCCCCGUAUACGCAUCUGAAAGGCACACCGCCUAUUACCAAU'
                       'UUGCGCUUCCUUACAUAGGAGGACCUGUUAUCGUCUUCUCAAUCGCUGAG'
                       'UUACCUUAAAACUAGGAUC'),
                      ('ACCGAGUAAAAGGCGACGGUUCGUUUCCGAACCUAUUUGCUCUUAUUUCU'
                       'ACGGGCUGCUAGUGUUGUAGGCUGCAAAACCUACGUAGUCCCAUCUAUCA'
                       'UGCUCGACCCUACGAGGCUAAUGUCUUGUCAGAGGCCCGUCAUGUGCCAC'
                       'GUACAUACACCAAUGUAUACCGCUCUAGCGGUUUGGUGUAGUAGGACUUG'
                       'UGUAUGCACGCUACAGCGAACAACGUUGAUCCCUAACUGAAGUCGGGCUC'
                       'CGCAGGCCUACUCACGCCGUUUCUAUAGGUUGAGCCGCAUCAAACAUUGG'
                       'GUUGAGUCUCGAGUAUAGAGGAAGGCUCUGGUGGCAGGCGCGACGUUGAU'
                       'CGGGAGGAGUAUGGAUGGUGAUCAAUCCCCGUGCCAAUCGCGAGUACUAC'
                       'AGGAGGAGGGGGCGGCUCUGUUCAAUCAUCACCCGUUCCAUCACACGGGC'
                       'AGCACAGUUGACCUCCCGAGCCGUCUCACGGACCUAGUGGCAACAGGUGU'
                       'AUUGAAGCGCCGGGAAUAGUCAUACCCGUGGGCUUGAUUGAGAGACCGAA'
                       'AUUCCGACCGCCAAAACUGCUGAUAUCGUACGCCUUACUACAAAACAAAU'
                       'GACGUCACUACCGGCCAGGGACAAGCUUAUUAAUUAAGUAGGAACCCUAU'
                       'ACCUUGCACAUCCUAAAUCUAGCAGCGGGUCCAGGAUUGGUUCCAGUCCA'
                       'ACGCGCGAUGCGCGUCAAGCUAGGCGAAUGACCACGGUCGAAACACCACU'
                       'UAUGUGACCCACCUUGGCCAACUCUCCCGAUUCUCCUCGCUACUAUCUUG'
                       'AAGGUCACUGAGAAUAUCCCUUAUGGGUCGCAUACGGAGACAGCCGCAGG'
                       'AGCCUUAACGGAGAAUACGCCAAUACUAUGUUCUGGGUCGGUGGGUGUAA'
                       'UGCGAUGCAAUCCGAUCGUGCGAACGUUCCCUUUGAUGACUAUAGGGUCU'
                       'AGUGAUCGUACAUGUGC')])


def random_filename() -> str:
    """
    Generate a random filename for testing
    """

    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))