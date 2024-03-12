#!/usr/bin/python3

# João Silva <202200190@estudantes.ips.pt>
# Sandro Duarte <202200055@estudantes.ips.pt>
# Mariana Raposo <2022006422@estudantes.ips.pt>
# Tiago Beja <202000197@estudantes.ips.pt>

import sys
import requests

def sequence_fetcher(database, search_term): 
    url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
    url_search = url + "esearch.fcgi"
    url_fetch = url + "efetch.fcgi"
    url_history = url + "esummary.fcgi"

    search_params = {
        "db": database,
        "term": search_term,
        "usehistory": "y",
        "retmode": "json"
    }

    search = requests.get(url_search, params = search_params)
    search_data = search.json()
    id_list = search_data["esearchresult"]["idlist"]
    query_key = search_data["esearchresult"]["querykey"]
    webenv = search_data["esearchresult"]["webenv"]

    fetch_params = {
        "db": database,
        "query_key": query_key,
        "webenv": webenv,
        "rettype": "fasta",
        "retmode": "text",
    }

    fetch = requests.get(url_fetch, params = fetch_params)
    fasta_data = fetch.text

    return fasta_data

if __name__== "__main__":
    if len(sys.argv) !=4:
        print("Usage: python sequences_retriever.py <database> <search_term> <output_file>")
        sys.exit(1)

    database = sys.argv[1]
    search_term = sys.argv[2]
    output_file = sys.argv[3]

    fasta_data = sequence_fetcher(database, search_term)

    with open(output_file, "w") as fasta_file:
        fasta_file.write(fasta_data)

    print("Sequences retrieved and written to", output_file)
