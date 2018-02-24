import wikipedia as wp

print(wp.search("Barack Obama"))

print(wp.summary("GitHub"))

wiki = wp.page("Mark Zuckerberg")

print(wiki.title, wiki.url)
