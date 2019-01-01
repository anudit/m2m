'''
TEST DATA:

https://medium.com/textileio/five-projects-that-are-decentralizing-the-web-in-slightly-different-ways-debf0fda286a

https://medium.com/@jimmysong/why-blockchain-is-hard-60416ea4c5c"

'''

import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import os
import urllib

def parseArticle(soup):
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

    return doc

LINK = input("Medium Article Link : ")

print("Checking Link")

r = requests.get(LINK)
if (r.status_code != 200):
    print("Invalid Link")
    exit()

parsed_uri = urlparse(LINK)
if (parsed_uri.netloc != "medium.com"):
    print("Not a Medium Link")
    exit()

result = requests.get(LINK)
soup = BeautifulSoup(result.content, features="html.parser")
FILENAME = "./Articles/" + soup.title.string + ".md"

if(os.path.exists("Articles") != True):
    os.mkdir("Articles")

if (os.path.exists(FILENAME) == True):
    ans = input("Article already exists, download again? (Y/N) ")
    if (ans.lower() == "y"):
        try:
            with open(FILENAME, "w", encoding="utf8") as file:     
                print("Parsing Article")
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