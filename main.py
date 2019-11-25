#!/usr/bin/python3
#
# For license details see LICENSE.
#
# Example script how to use doi2bibtex.py and search_doi.py.
#

import search_doi
import doi2bibtex

author = input("Author: ")
title = input("Title: ")

doi = search_doi.fetch_doi(author, title)
print("\nDOI:", doi)
print("Bibtex:")
print(doi2bibtex.fetch_bibtex(doi))
