#!/usr/bin/python3
#
# For license details see LICENSE.
#
# doi2bibtex.py: Fetches bibtex entries for all DOIs on stdin. One DOI per line.
#

import urllib.request

def fetch_bibtex(doi):
    """Fetches bibtex from dx.doi.org given a DOI."""
    url = "http://dx.doi.org/{}".format(
        doi) if not doi.startswith("http") else doi
    req = urllib.request.Request(url, data=None, headers={
                                 "Accept": "text/bibliography; style=bibtex"})
    return urllib.request.urlopen(req).read().decode()


if __name__ == "__main__":
    import sys
    for l in sys.stdin.readlines():
        print(fetch_bibtex(l[:-1]))
