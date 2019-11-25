#!/usr/bin/python3
#
# For license details see LICENSE.
#
# Searches crossref.org's public REST API for DOIs given author and title of
# a publication. Takes input from stdin in format: author | title
#

import urllib.request
import urllib.parse
import json


def fetch_doi(author, title):
    """Fetches a DOI from crossref.org.
    Raises a NoMatchError if a different publication was the first hit for the
    query."""
    qauthor = urllib.parse.quote(author)
    qtitle = urllib.parse.quote(title)

    urlfmt = "http://api.crossref.org/works" + \
        "?query.bibliographic={0}&query.author={1}&rows=1"
    with urllib.request.urlopen(urlfmt.format(qtitle, qauthor)) as req:
        return json.loads(req.read())['message']['items'][0]['DOI']


if __name__ == "__main__":
    import sys
    for l in sys.stdin.readlines():
        sp = l.split("|")
        author = sp[0]
        title = sp[1][:-1]
        print(fetch_doi(author, title))
