import requests
import bs4

result = requests.get("https://onezero.medium.com/lets-not-put-the-government-in-charge-of-moderating-facebook-954562b62635")
soup = bs4.BeautifulSoup(result.content, features="html.parser")
print(soup.find("meta", attrs={'name':'author'})['content'])
