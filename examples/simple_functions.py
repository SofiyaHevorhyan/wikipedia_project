# File: simple_functions.py
# A simple module with few functions from wikipedia lib

import wikipedia as wp

if __name__ == "__main__":
    print(wp.search("Barack Obama"), "\n")
    print(wp.summary("GitHub"), "\n")

    wiki = wp.page("Mark Zuckerberg")
    print(wiki.title, wiki.url)
