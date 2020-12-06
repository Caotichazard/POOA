
import requests
from bs4 import BeautifulSoup



def getSources():
    result = requests.get('https://g1.globo.com/')
    src = result.content
    soup = BeautifulSoup(src, 'lxml')
    all_news = soup.find_all("a")    
    return all_news

def getLink(source):
    return source.attrs["href"]

def getTitle(source):
    return source.text

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