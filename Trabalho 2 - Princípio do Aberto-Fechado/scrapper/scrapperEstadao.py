import requests
from bs4 import BeautifulSoup


def getSources():
    result = requests.get('https://www.estadao.com.br/')
    src = result.content
    soup = BeautifulSoup(src, 'lxml')
    all_news = []
    container = soup.find_all("a")
    for news in container:
        parents = news.find_parents("div", attrs={"class":"intro"})
        for parent in parents:
            all_news.append(parent.find("a"))
    all_news = list(dict.fromkeys(all_news))
    
    
    return all_news

def getLink(source):
    return source.attrs["href"]

def getTitle(source):
    return source.attrs["title"]

def getNoticias(sources):
    all_news = []
    for source in sources:
        titulo = getTitle(source)
        link = getLink(source)
        noticia = {
            "titulo": titulo,
            "link":link,
        }
        all_news.append(noticia)
    return all_news