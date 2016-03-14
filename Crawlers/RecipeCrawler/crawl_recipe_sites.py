import re

with open("Recipe_links.txt", 'w', encoding="utf8") as outfile:
    for pagenumber in range(1, 666):
        pagenumber_str = str(pagenumber)
        with open(pagenumber_str + ".html", "r", encoding="utf8") as htmlfile:
            all_text = htmlfile.read()
            links = re.findall(
                "<td class=\"left title odd_gray\" onclick=\"redirect_prevent_default\('(http://toidutare.ee/[\s\S]*?)'\)",
                all_text)
            for web_link in links:
                outfile.write(web_link + "\n")
print("finished")
