# File: categories.py
# A simple module showing how to get the categories of the wiki page

import wikipedia as wp


def wiki_categories(name):
    """(str) -> list
    Getting the list of categories"""
    return wp.WikipediaPage(name).categories


if __name__ == "__main__":
    page1 = "List of countries by number of Internet users"
    categories1 = wiki_categories(page1)
    print(f"Categories for {page1}: \n", categories1)

    page2 = "Barack Obama"
    categories2 = wiki_categories(page2)
    print(f"Categories for {page2}: \n", categories2)
