import requests
import bs4

def parse(LINK, OFFLINEMODE = False):
    result = requests.get(LINK)
    soup = bs4.BeautifulSoup(result.content, features="html.parser")
    title = soup.title.text
    author = soup.find("meta", attrs={'name':'author'})['content']
    sec = soup.find_all("div", "section-inner")
    doc = ""
    for secIndex in range(len(sec)):
        tags = sec[secIndex].find_all(['h1','h2','h3','h4','ol','ul','blockquote','figure','p', 'pre', 'hr'])

        for i in tags:
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
                if(im == None and i.find("iframe")!=None):
                    iframe  = i.find("iframe")
                    ifsrc = "medium.com"+ iframe['src']
                    doc += ("<iframe src='"+ifsrc+"'></iframe>")
                    continue
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

                    fileurl = "./"+ FOLDERNAME +"/OfflineData/" + NARTICLENAME + "/" + filen
                    if(os.path.exists("./"+ FOLDERNAME +"/OfflineData/") != True):
                        os.mkdir("./"+ FOLDERNAME +"/OfflineData/")
                        if(os.path.exists("./"+ FOLDERNAME +"/OfflineData/" + NARTICLENAME + "/") != True):
                            os.mkdir("./"+ FOLDERNAME +"/OfflineData/" + NARTICLENAME)

                    img = open(fileurl,'wb')
                    img.write(requests.get(im['src']).content)
                    img.close()
                    mdurl = "./OfflineData/" + NARTICLENAME + "/" + filen
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
    return (title, author, doc)

def test():
    print(parse("https://medium.com/javascript-in-plain-english/full-stack-mongodb-react-node-js-express-js-in-one-simple-app-6cc8ed6de274"))
