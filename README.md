## Sequence_Fetcher_ASB_HW1.
This is a small script to retrieve sequences from a database, using 'history' API feature (Bio.Entrez library).

## Usage
```bash
python sequences_retriever.py [database] [search term]
```
Example: python sequences_retriever.py nucleotide "Psammodromus algirus" 
Note: You can add "> output file" so that the output goes to a file; otherwise, it will be written to STDOUT.

## Requisites 
* Python
* Bio.Entrez library
