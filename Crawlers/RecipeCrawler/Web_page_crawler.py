import re
import urllib.request as urllib2

with open("Web_pages.txt", 'w') as outfile:
    for pagenumber in range(1, 666):
        pagenumber_str = str(pagenumber)
        page_address = "http://toidutare.ee/k%C3%B5ik_retseptid/?leht=" + \
            pagenumber_str + "&rv=1&undefined"
        print(page_address)
        page = urllib2.urlopen(page_address)
        page_content = page.read()
        with open(pagenumber_str + ".html", 'wb') as fid:
            fid.write(page_content)
