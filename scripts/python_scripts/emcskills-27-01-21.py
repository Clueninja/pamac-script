import bs4, requests
res1=requests.get("https://en.wikipedia.org/")
soup1=bs4.BeautifulSoup(res1.text, features="html5lib")
links=soup1.select("p")
print(links)