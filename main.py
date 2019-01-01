'''
TEST DATA:

https://medium.com/textileio/five-projects-that-are-decentralizing-the-web-in-slightly-different-ways-debf0fda286a

https://medium.com/@jimmysong/why-blockchain-is-hard-60416ea4c5c"

'''

import requests
import bs4
from urllib.parse import urlparse
import os
import urllib
import re

def parseArticle(soup):
    sec = soup.find_all("div", "section-inner")
    doc = ""
    for secIndex in range(len(sec)):
        tags = sec[secIndex].find_all(['h1','h2','h3','h4','ol','ul','blockquote','figure','p', 'pre', 'hr'])
        for i in tags:
            #print(i.name)
            if (i.name == "h1"):
                doc+=("# " + i.getText() + "\n")
            elif (i.name == "h2"):
                doc+=("## " + i.getText() + "\n")
            elif (i.name == "h3"):
                doc+=("## " + i.getText() + "\n")
            elif (i.name == "h4"):
                doc+=("### " + i.getText() + "\n")
            elif (i.name == "h5"):
                doc+=("#### " + i.getText() + "\n")
            elif (i.name == "h6"):
                doc+=("##### " + i.getText() + "\n")
            elif (i.name == "p"):
                doc+=(i.getText() + "\n\n")
            elif (i.name == "blockquote"):
                doc+=(">" + i.getText() + "\n\n")
            elif (i.name == "figure"):
                im = i.find("img")
                doc+=("![](" +im['src'] +")" + "\n\n")
            elif (i.name == "ol"):
                doc+="\n"
                lilist = i.find_all('li')
                for t in range(len(lilist)):
                    doc+=(str(t+1) +". " + lilist[t].getText() + "\n")
                doc+="\n"
            elif (i.name == "ul"):
                doc+="\n"
                lilist = i.find_all('li')
                for t in range(len(lilist)):
                    doc+=("- " + lilist[t].getText() + "\n")
                doc+="\n"
            elif (i.name == "pre"):
                doc+="\n"
                doc+="```\n"
                for e in i.contents:
                    if(type(e) == bs4.element.NavigableString):
                        doc+=str(e)+"\n"
                doc+= "``` \n"
            elif (i.name == "hr"):
                doc+="\n---\n"
    return doc

LINK = input("Medium Article Link : ")

print("Checking Link")

r = requests.get(LINK)
if (r.status_code != 200):
    print("Invalid Link")
    exit()

parsed_uri = urlparse(LINK)
if (parsed_uri.netloc != "medium.com"):
    ans = input("Not a Medium Link, Continue? (Y/N) ")
    if (ans.lower() != "y"):
        exit()

print("Parsing Article")

result = requests.get(LINK)
soup = bs4.BeautifulSoup(result.content, features="html.parser")
fn  = soup.title.string
forb = '<>:/\|?*'
fn = ''.join(c for c in fn if c not in forb)
FILENAME = "./Articles/" + fn[0:252] + ".md"


if(os.path.exists("Articles") != True):
    os.mkdir("Articles")


if (os.path.exists(FILENAME) == True):
    ans = input("Article already exists, download again? (Y/N) ")
    if (ans.lower() == "y"):
        try:
            with open(FILENAME, "w", encoding="utf8") as file:     
                file.write(parseArticle(soup))
                print("Done, Happy Reading!")  
        except IOError:
            print("[File Error] Can't write to File.")
            exit()
    else:
        exit()
else:
    try:
        with open(FILENAME, "w", encoding="utf8") as file:     
            print("Parsing Article")
            file.write(parseArticle(soup))
            print("Done, Happy Reading!")  
    except IOError:
        print("[File Error] Can't write to File.")
        exit()