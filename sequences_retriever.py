#!/usr/bin/python3

# Script to retrieve sequences using the Entrez API
# Authors: João Silva, Sandro Duarte, Mariana Raposo, Tiago Beja

import sys
import requests

def sequence_fetcher(database, search_term): 
    # Base URL for Entrez API
    url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
    
    # URLs for different API endpoints
    url_search = url + "esearch.fcgi"
    url_fetch = url + "efetch.fcgi"
    url_history = url + "esummary.fcgi"

    # Parameters for the search endpoint
    search_params = {
        "db": database,
        "term": search_term,
        "usehistory": "y",
        "retmode": "json"
    }

    # Performing the search to get the list of IDs
    search = requests.get(url_search, params = search_params)
    search_data = search.json()
    id_list = search_data["esearchresult"]["idlist"]
    query_key = search_data["esearchresult"]["querykey"]
    webenv = search_data["esearchresult"]["webenv"]

    # Parameters for fetching the sequences
    fetch_params = {
        "db": database,
        "query_key": query_key,
        "webenv": webenv,
        "rettype": "fasta",
    }

    # Fetching the sequences
    fetch = requests.get(url_fetch, params = fetch_params)
    fasta_data = fetch.text

    return fasta_data

if __name__== "__main__":
    # Checking command-line arguments
    if len(sys.argv) !=4:
        print("Usage: python sequences_retriever.py <database> <search_term> <output_file>")
        sys.exit(1)

    # Retrieving command-line arguments
    database = sys.argv[1]
    search_term = sys.argv[2]
    output_file = sys.argv[3]

    # Fetching sequences
    fasta_data = sequence_fetcher(database, search_term)

    # Writing sequences to the output file
    with open(output_file, "w") as fasta_file:
        fasta_file.write(fasta_data)

    print("Sequences retrieved and written to", output_file)
