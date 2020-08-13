from lxml import html
import requests
import re
import urllib.request
import shutil


url = "https://www.gutenberg.org/ebooks/14591"
mainWebsite = "https://www.gutenberg.org/"

page = requests.get(url)
tree = html.fromstring(page.content)

section = tree.xpath('//a[@charset="utf-8"]/text()')

if 'Plain Text UTF-8' in section:
    r = requests.get(url, allow_redirects=True)
    links = re.findall('a href="(.*txt)"', r.text)
    for l in links:
        fileurl = mainWebsite+l
        with urllib.request.urlopen(fileurl) as response, open("training_texts.txt", "wb") as out_file:
            shutil.copyfileobj(response, out_file)
            break
