import requests
from bs4 import BeautifulSoup
import os
import urllib

LINK = "https://medium.com/textileio/five-projects-that-are-decentralizing-the-web-in-slightly-different-ways-debf0fda286a"
#LINK = "https://medium.com/@jimmysong/why-blockchain-is-hard-60416ea4c5c"

result = requests.get(LINK)

soup = BeautifulSoup(result.content, features="html.parser")
FILENAME = "./Articles/" + soup.title.string + ".md"
f = open(FILENAME, "w", encoding="utf-8")
samples = soup.find_all("div", "section-inner")
tags = samples[0].find_all(['h1','h2','h3','h4','ol','blockquote','figure','p'])

doc = ""

for i in tags:
    #print(i.name)
    if (i.name == "h1"):
        doc+=("# " + i.getText() + "\n")
    elif (i.name == "h2"):
        doc+=("## " + i.getText() + "\n")
    elif (i.name == "h3"):
        doc+=("### " + i.getText() + "\n")
    elif (i.name == "h4"):
        doc+=("#### " + i.getText() + "\n")
    elif (i.name == "h5"):
        doc+=("##### " + i.getText() + "\n")
    elif (i.name == "h6"):
        doc+=("###### " + i.getText() + "\n")
    elif (i.name == "p"):
        doc+=(i.getText() + "\n\n")
    elif (i.name == "blockquote"):
        doc+=(">" + i.getText() + "\n\n")
    elif (i.name == "figure"):
        im = i.find("img")
        #print(im)
        doc+=("![](" +im['src'] +")" + "\n\n")

f.write(doc)
f.close()