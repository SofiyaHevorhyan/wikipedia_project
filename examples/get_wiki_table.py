# File: get_wiki_table.py
# A simple program getting some table from wiki page

import wikipedia
import pandas as pd


def table_wiki(name):
    """
    (str) -> pandas.core.frame.DataFrame
    the function looks for table on wiki page and returns the info in it

    name: the name of wiki page
    return: the data frame of info
    """
    # Get the info from html page
    html = wikipedia.page(name).html().encode("UTF-8")
    df = pd.read_html(html)[5]
    return df


print(table_wiki("List of countries by number of Internet users"))
