
import bs4,requests

def links_from_page(link):
    soup1=bs4.BeautifulSoup(requests.get("https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm").text)
    links=soup1.select("a")
    list_of_links=[]
    for L in links:
        string=L.get("href")
        lisk_of_links.append(string)
    return list_of_links


start=["https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm"]
target="https://en.wikipedia.org/wiki/Jesus"
while True:

