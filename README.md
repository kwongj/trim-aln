# trim-aln
Performs basic alignment trimming

## Author

Jason Kwong (@kwongjc)

## Dependencies
* Python 2.7.x
* BioPython

## Usage

```
$ trim-aln.py -h
usage: 
  trim-aln.py --start [POS] --end [POS] ALIGNMENT > trimmed.aln

Script to trim alignments

positional arguments:
  ALIGNMENT      Alignment in FASTA format (required)

optional arguments:
  -h, --help     show this help message and exit
  --start POS    Start coordinate to trim alignment (default = start)
  --end POS      End coordinate to trim alignment (default = end)
  --out OUTFILE  Output file for trimmed alignment
  --version      show program's version number and exit
```

## Bugs

Please submit via the [GitHub issues page](https://github.com/kwongj/trim-aln/issues).  

## Software Licence

[GPLv3](https://github.com/kwongj/trim-aln/blob/master/LICENSE)
