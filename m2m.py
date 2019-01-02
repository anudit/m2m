import requests
import bs4
import os
import urllib
import argparse
import time

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
                for e in i.contents:
                    if(type(e) == bs4.element.NavigableString):
                        doc+=str(e)
                    elif (type(e) == bs4.element.Tag and e.name == "a"):
                        doc+="["+ e.getText() +"]("+ e['href'] +")"
                    elif ((type(e) == bs4.element.Tag) and (e.name == "b" or e.name == "strong")):
                            temptext = str(e.getText())
                            temptext = temptext.strip()
                            doc+="**"+ temptext +"** "
                    elif ((type(e) == bs4.element.Tag) and (e.name == "i" or e.name == "em")):
                        temptext = str(e.getText())
                        temptext = temptext.strip()
                        doc+="*"+ temptext +"* "
                doc+=("\n\n")
            elif (i.name == "blockquote"):
                doc+=(">" + i.getText() + "\n\n")
            elif (i.name == "figure"):
                im = i.find("img")
                cap = i.find("figcaption")
                if (OFFLINEMODE != True):
                    if(cap!= None and cap.find("a")!= None):
                        doc+=("[!["+ cap.getText() +"](" +im['src'] +")]("+ cap.find("a")['href'] +")" + "\n\n")
                    else:
                        doc+=("![](" +im['src'] +")\n\n")
                else:
                    filen = str(time.time()*10000) + ".jpg"

                    NARTICLENAME  = ARTICLENAME
                    NARTICLENAME = ''.join(c for c in NARTICLENAME if c not in " ")

                    fileurl = "./"+ FOLDERNAME +"/" + NARTICLENAME + "/" + filen
                    if(os.path.exists("./"+ FOLDERNAME +"/" + NARTICLENAME + "/") != True):
                        os.mkdir("./"+ FOLDERNAME +"/" + NARTICLENAME)

                    img = open(fileurl,'wb')
                    img.write(requests.get(im['src']).content)
                    img.close()
                    mdurl = "./" + NARTICLENAME + "/" + filen
                    if(cap!= None and cap.find("a")!= None):
                        doc+=("[!["+ cap.getText() +"](" + mdurl +")]("+ cap.find("a")['href'] +")" + "\n\n")
                    else:
                        doc+=("![](" +mdurl +")\n\n")

            elif (i.name == "ol"):
                doc+="\n"
                lilist = i.find_all('li')
                for t in range(len(lilist)):
                    doc+=str(t+1) +". "
                    for e in lilist[t].contents:
                        if(type(e) == bs4.element.NavigableString):
                            doc+=str(e)
                        elif (type(e) == bs4.element.Tag and e.name == "a"):
                            doc+="["+ e.getText() +"]("+ e['href'] +")"
                        elif ((type(e) == bs4.element.Tag) and (e.name == "b" or e.name == "strong")):
                            temptext = str(e.getText())
                            temptext = temptext.strip()
                            doc+="**"+ temptext +"** "
                        elif ((type(e) == bs4.element.Tag) and (e.name == "i" or e.name == "em")):
                            temptext = str(e.getText())
                            temptext = temptext.strip()
                            doc+="*"+ temptext +"* "
                    doc+= "\n"
                doc+="\n"
            elif (i.name == "ul"):
                doc+="\n"
                lilist = i.find_all('li')
                for t in range(len(lilist)):
                    doc+="- "
                    for e in lilist[t].contents:
                        if(type(e) == bs4.element.NavigableString):
                            doc+=str(e)
                        elif (type(e) == bs4.element.Tag and e.name == "a"):
                            doc+="["+ e.getText() +"]("+ e['href'] +")"
                        elif ((type(e) == bs4.element.Tag) and (e.name == "b" or e.name == "strong")):
                            temptext = str(e.getText())
                            temptext = temptext.strip()
                            doc+="**"+ temptext +"** "
                        elif ((type(e) == bs4.element.Tag) and (e.name == "i" or e.name == "em")):
                            temptext = str(e.getText())
                            temptext = temptext.strip()
                            doc+="*"+ temptext +"* "
                doc+= "\n\n"
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

ENDINGQUOTE = "Done, Happy Reading!"
FOLDERNAME = "Articles"
ARTICLENAME = ""
FORCECONTINUE = False
OFFLINEMODE = False

parser = argparse.ArgumentParser()
parser.add_argument('-y', action='store_true')
parser.add_argument('-o', action='store_true')
options = parser.parse_args()

if(options.y == True):
    FORCECONTINUE = True
if(options.o == True):
    OFFLINEMODE = True

LINK = input("Medium Article Link : ")

print("Checking Link")

r = requests.get(LINK)
if (r.status_code != 200):
    print("Invalid Link")
    exit()

parsed_uri = urllib.parse.urlparse(LINK)
if (parsed_uri.netloc != "medium.com" and FORCECONTINUE != True):
    ans = input("Not a Medium Domain, Continue? (Y/N) ")
    if (ans.lower() != "y"):
        exit()

print("Parsing Article")

result = requests.get(LINK)
soup = bs4.BeautifulSoup(result.content, features="html.parser")
fn  = soup.title.string
forb = '<>:/\|?*'
fn = ''.join(c for c in fn if c not in forb)
FILENAME = "./Articles/" + fn[0:252] + ".md"
ARTICLENAME = fn[0:252]

if(os.path.exists(FOLDERNAME) != True):
    os.mkdir(FOLDERNAME)

if (os.path.exists(FILENAME) == True and FORCECONTINUE != True):
    ans = input("Article already exists, Continue? (Y/N) ")
    if (ans.lower() == "y"):
        try:
            with open(FILENAME, "w", encoding="utf8") as file:     
                file.write(parseArticle(soup))
                print(ENDINGQUOTE)  
                exit()
        except IOError:
            print("[File Error] Can't write to File. -1")
            exit()
    else:
        exit()
else:
    try:
        with open(FILENAME, "w", encoding="utf8") as file:
            file.write(parseArticle(soup))
            print(ENDINGQUOTE)
            exit()
    except IOError:
        print("[File Error] Can't write to File. -2")
        exit()