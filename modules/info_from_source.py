# File: info_from_source.py
# A simple module that helps getting info about top pages based on given source

import mwviews.api as mw
import datetime


def get_watchers_from_source(source="en.wikipedia", num=50):
    """
    :param source:
    :param num:
    :return: json
    """
    p = mw.PageviewsClient("hevorhyan@ucu.edu.ua")
    date = datetime.date.today()
    date = date.replace(day=date.day-2)

    info = p.top_articles(source, limit=num, day=date.day)

    '''
    services = ["en.wikipedia", "en.wiktionary", "en.wikibooks",
                "en.wikiquote", "commons.wikimedia", "en.wikinews",
                "en.wikivoyage", "species.wikimedia", "wikidata"]
    data = {}
    for serv in services:
        data[serv] = p.top_articles(serv, limit=5)

    f = open("watchers.json", "w+", encoding="utf-8")
    json.dump(data, f, ensure_ascii=False)
    f.close()
    '''

    return info, date


if __name__ == "__main__":
    get_watchers_from_source()
