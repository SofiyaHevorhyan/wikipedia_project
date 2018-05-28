# File: info_based_on_page.py
# Module getting, sorting and formatting top pages based on the category

from modules.arrays import Array2D

import mwviews.api as mw

import json
import requests
import datetime


# max num of pages from the category
MAX_NUM = 200
BASE_URL = "https://en.wikipedia.org/w/api.php"


def get_category_pages(category):
    pages = Array2D(MAX_NUM, 2)

    att = dict()
    att["action"] = "query"
    att["list"] = "categorymembers"
    att["cmtitle"] = f"Category:{category}"
    att["cmprop"] = "ids|title"
    att["cmlimit"] = str(MAX_NUM)
    att["cmtype"] = "page"
    att["format"] = "json"

    response = requests.get(BASE_URL, params=att)

    data = response.content
    data2 = json.loads(data)
    # print(data2)

    for i, el in enumerate(data2["query"]["categorymembers"]):
        pages[i, 0] = el["pageid"]
        pages[i, 1] = el["title"]
        # print(el["pageid"], el["title"])

    # f = open("pages_from_cat.json", "w+", encoding="utf-8")
    # json.dump(data2, f, ensure_ascii=False)
    # f.close()

    return pages


def get_date():
    end = datetime.date.today()
    start = end.replace(month=end.month-1, day=1)
    return str(start).replace("-", ""), str(end).replace("-", ""), end.month


def get_watchers_from_lst_pages(pages):
    # for further sorting-by-watchers, make dictionary to find quickly
    # id of the page
    title_ids = {pages[i, 1]: pages[i, 0] for i in range(pages.num_rows())
                 if pages[i, 1]}
    titles = list(title_ids.keys())
    first = titles[0].replace(" ", "_")
    # print(titles)

    start, end, current_month = get_date()

    # info always will contain data about two months - previous and current
    p = mw.PageviewsClient("hevorhyan@ucu.edu.ua")
    info = p.article_views("en.wikipedia", titles,
                           granularity="monthly", start=start,
                           end=end)

    # print(list(info.items()))
    data = list(info.items())

    # first case - there is data about current month - choose it
    if data[0][1][first] is not None and data[1][1][first] is not None:
        if data[0][0].month == current_month:
            watchers, date = data[0][1], data[0][0]
        else:
            watchers, date = data[1][1], data[1][0]

    # second case - there is no data about current month - pick previous
    else:
        if data[0][1][first] is not None:
            watchers, date = data[0][1], data[0][0]
        else:
            watchers, date = data[1][1], data[1][0]

    watchers = sorted(list(watchers.items()), key=lambda x: x[1], reverse=True)
    # print(watchers)

    sorted_pages = list()
    for i, el in enumerate(watchers):
        name = el[0].replace("_", " ")
        page = dict([("article", name), ("views", el[1]), ("rank", i+1),
                     ("ids", title_ids[name])])
        sorted_pages.append(page)

    # print(sorted_pages)

    return sorted_pages, date
