# File: info.py
# A simple module getting info from wiki by given name of the page

import modules.info_based_on_page as info_page
import modules.info_from_source as info_source

import wikipedia as wp
import wikipediaapi as wpapi
import mwviews.api as mw
import json
import requests
import datetime


NUM_PAGES = 30  # if there is no parameter of max num of pages should be shown


def get_content_for_all(array):
    """

    :param array:
    :return: ARRAY??
    """
    pass


def get_content_for_page(page):
    # content = wp.WikipediaPage(page).content
    summary = wp.WikipediaPage(page).summary
    url = wp.WikipediaPage(page).url
    print(summary)
    return summary


def get_main_info(choice=1, resource="Wikipedia", num=NUM_PAGES):

    # get the info based on page
    if choice == 1:
        categories = wp.WikipediaPage(resource).categories
        print(categories)
        print(categories[2])
        pages = info_page.get_category_pages("19th-century French newspaper "
                                             "publishers (people)")
        sorted_pages, date = info_page.get_watchers_from_lst_pages(pages)
        return sorted_pages

    # get the info based on source
    elif choice == 0:
        sorted_pages, date = info_source.get_watchers_from_source(resource)
        return sorted_pages

    else:
        # get_category_pages("19th-century French newspaper publishers (people)")
        get_content_for_page("Cat")

    # get_content_for_all(info, num)


def main():
    get_main_info(1, "Claude Monet", 3)


if __name__ == "__main__":
    main()
