#!/usr/bin/env python
# Script by Jason Kwong
# Script to trim alignments

# Use modern print function from python 3.x
from __future__ import print_function

# Import modules
import argparse
from argparse import RawTextHelpFormatter
import os
import sys
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

# Usage
parser = argparse.ArgumentParser(
	formatter_class=RawTextHelpFormatter,
	description='Script to trim alignments',
	usage='\n  %(prog)s --start [POS] --end [POS] --out [OUTFILE] ALIGNMENT')
parser.add_argument('alignment', metavar='ALIGNMENT', nargs=1, help='Alignment in FASTA format (required)')
parser.add_argument('--start', metavar='POS', nargs=1, help='Start coordinate to trim alignment (default = start)')
parser.add_argument('--end', metavar='POS', nargs=1, help='End coordinate to trim alignment (default = end)')
parser.add_argument('--out', metavar='OUTFILE', nargs=1, required=True, help='Output file for trimmed alignment (required)')
parser.add_argument('--version', action='version', version=
	'=====================================\n'
	'%(prog)s v0.1\n'
	'Updated 1-June-2016 by Jason Kwong\n'
	'Dependencies: Python 2.x, BioPython\n'
	'=====================================')
args = parser.parse_args()

# Functions
# Log a message to stderr
def msg(*args, **kwargs):
	print(*args, file=sys.stderr, **kwargs)

# Log an error to stderr and quit with non-zero error code
def err(*args, **kwargs):
	msg(*args, **kwargs)
	sys.exit(1);

# Check file exists
def check_file(f):
	if os.path.isfile(f) == False:
		err('ERROR: Cannot find "{}". Check file exists in the specified directory.'.format(f))

# Check arguments
aln = args.alignment[0]
check_file(aln)
outfile = args.out[0]
if args.start:
	start = int(args.start[0]) - 1
else:
	start = None
if args.end:
	end = int(args.end[0])
else:
	end = None

# Parse masking regions
with open(aln, 'rb') as f:
	if f.read(1) != '>':
		msg('ERROR: "{}" does not appear to be in FASTA format.'.format(aln))

# Parse sequence
newALN = []
fa = open(aln, 'rU')
for record in SeqIO.parse(fa, 'fasta'):
	msg('Reading "{}" ... '.format(record.id))
	newseq = record.seq[start:end]
	newALN.append(SeqRecord(newseq, id=record.id, name=record.name, description=record.description))

# Write masked alignment to file
msg('Trimmed alignment saved to "{}" ... '.format(outfile))
SeqIO.write(newALN, outfile, 'fasta')

sys.exit(0)
