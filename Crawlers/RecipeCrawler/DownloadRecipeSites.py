import re
import urllib.request as urllib2

with open("Recipe_links.txt", "r", encoding="utf8") as infile:
    for line in infile:
        page = urllib2.urlopen(line)
        page_contents = page.read()
        save_name
        with open
        