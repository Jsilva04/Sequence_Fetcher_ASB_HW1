#!/usr/bin/python3

# Script to retrieve sequences using the Entrez API
# Authors: João Silva, Sandro Duarte, Mariana Raposo, Tiago Beja

import sys
import requests

# Base URL for Entrez API
URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"

# URLs for different API endpoints
URL_esearch = URL + "esearch.fcgi"
URL_efetch = URL + "efetch.fcgi"
URL_history = URL + "esummary.fcgi"

def esearch_sequence(database, search_term): 
    # Parameters for the search endpoint
    search_params = {
        "db": database,
        "term": search_term,
        "usehistory": "y",
        "retmode": "json"
    }

    # Performing the search to get the list of IDs
    search = requests.get(URL_esearch, params = search_params)
    search_data = search.json()
    id_list = search_data["esearchresult"]["idlist"]
    query_key = search_data["esearchresult"]["querykey"]
    webenv = search_data["esearchresult"]["webenv"]

    return (webenv, query_key)


def efetch_sequence(webenv, query_key):
    # Parameters for fetching the sequences
    fetch_params = {
        "db": database,
        "query_key": query_key,
        "webenv": webenv,
        "rettype": "fasta",
    }

    # Fetching the sequences
    fetch = requests.get(URL_efetch, params = fetch_params)
    fasta_data = fetch.text

    return fasta_data

if __name__== "__main__":
    # Checking command-line arguments
    if len(sys.argv) !=3:
        print("Usage: python sequences_retriever.py <database> <search_term>")
        sys.exit(1)

    # Retrieving command-line arguments
    database = sys.argv[1]
    search_term = sys.argv[2]
    #output_file = sys.argv[3]

    # Fetching sequences
    WEBENV, QK =  esearch_sequence(database, search_term)
    fasta_data = efetch_sequence(WEBENV, QK)

    print(fasta_data)

