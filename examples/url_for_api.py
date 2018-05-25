# File: url_for_api.py
# A simple program getting the num of watchers of wiki page

import urllib.error
import urllib.request
import json


def use_url(name):
    wiki_url = "https://en.wikipedia.org/w/api.php?" \
               "action=query&" \
               "titles={0}&" \
               "prop=info&" \
               "inprop=watchers&" \
               "format=json&formatversion=2".format(name.replace(" ", "%20"))
    connection = urllib.request.urlopen(wiki_url)
    data = connection.read().decode()

    js = json.loads(data)

    f = open("data_pages_example.json", "w+", encoding="utf-8")
    json.dump(js, f, ensure_ascii=False)
    f.close()

    try:
        print("Page {0} has {1} "
              "watchers".format(name, str(js["query"]["pages"][0]["watchers"])))
    except KeyError:
        print("Sorry. We have no access to the num of watchers of ", name)


if __name__ == "__main__":
    use_url("Wikipedia")
    use_url("API:Main page")
    use_url("Google")
    use_url("Programming language")
