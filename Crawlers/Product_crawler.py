import urllib.request as urllib2
import re

with open("test.html", "w", encoding="utf8") as outfile:
    page = urllib2.urlopen(
        'https://www.e-maxima.ee/Products/sook-ja-jook.aspx')
    outfile.write(page.read())

with open("newfile.txt", 'w') as outfile, open("test.html", 'r') as infile:
    for line in infile:
        match = re.search("\/Products\/[^\"]+", line)
        if match is not None:
            outfile.write(match.group() + "\n")

with open("newfile2.txt", 'w') as outfile, open("newfile.txt", 'r') as infile:
    for line in infile:
        match = re.search("\/(.)*\/(.)*\/(.)*\/(.)*", line)
        if match is not None:
            outfile.write(match.group() + "\n")
        match is None

with open("newfile2.txt", 'r') as infile:
    for line in infile:
        page = urllib2.urlopen('https://www.e-maxima.ee/' + line)
        page_content = page.read()
        line = line.replace("/", "_")
        line = line.replace("\n", "")
        print(line)
        with open(line + ".html", 'wb') as fid:
            fid.write(page_content)

with open("newfile2.txt", 'r') as infile1, open("All_between_tr.txt", "w", encoding='utf8') as outfile:
    for line in infile1:
        line = line.replace("/", "_")
        line = line.replace("\n", "")
        with open(line + ".html", encoding='utf8') as infile2:
            line2 = infile2.read()
            for tr in re.findall("<tr>[\s\S]*?</tr>", line2):
                outfile.write(tr + "\n")

content = ""
with open("all_between_tr.txt", "r", encoding='utf8') as infile, open("product_info.txt", "w", encoding='utf8') as outfile:
    count = 0
    text = infile.read()
    for text1 in re.findall("<tr>[\s\S]*?</tr>", text):
        if "https://www.e-maxima.ee/SiteImages/" not in text1:
            continue
        count += 1
        #outfile.write += str(count) + ";"
        name = re.search(
            "height=\"108\" width=\"108\" alt=\"([\s\S]*?)\"",
            text1).group(1).replace(";", "")
        #outfile.write(name + ";")
        image_link = re.search(
            "img src=\"(https://www[\s\S]*?)\"",
            text1).group(1)
        #outfile.write(image_link + ";")
        price = re.search(
            "<strong>(.*?€)</strong>",
            text1).group(1).replace(
            ",",
            ".")
        #outfile.write(price + ";")
        price_kilograms = re.search(
            "<strong>[\s\S]*?</strong><br/>\(([\s\S]*?)\)", text1).group(1).replace(",", ".")
       # outfile.write(price_kilograms + "\n\n")

        measurement_unit = 0
        if price_kilograms[-2:].lower() == "tk":
            measurement_unit = 2
        elif price_kilograms[-2:].lower() == "kg":
            measurement_unit = 1
        else:
            measurement_unit = 3
        result = str(count) + ";" + name + ";" + image_link + \
            ";" + str(price[:-1]).strip() + ";" + \
            price_kilograms[0:4].strip() + ";" + str(measurement_unit)
        outfile.write(result + "\n")
print(count)
print("finished")
