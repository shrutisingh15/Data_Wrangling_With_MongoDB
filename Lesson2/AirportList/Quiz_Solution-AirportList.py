
# coding: utf-8

# In[ ]:

#!/usr/bin/env python

"""
Complete the 'extract_airports' function so that it returns a list of airport
codes, excluding any combinations like "All".
"""

from bs4 import BeautifulSoup
html_page = "options.html"


def extract_airports(page):
    data = []
    with open(page, "r") as html:
        # do something here to find the necessary values
        soup = BeautifulSoup(html, "lxml")
        air=soup.find(id="AirportList")
        options=air.find_all("option")
        for options in options:
            if options['value'] =='All' or options['value'] =='AllMajors' or options['value'] =='AllOthers':
                pass
            else:
                data.append(options['value'])

    return data


def test():
    data = extract_airports(html_page)
    assert len(data) == 15
    assert "ATL" in data
    assert "ABR" in data

test()

