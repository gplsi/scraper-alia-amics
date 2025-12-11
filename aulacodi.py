import requests
from bs4 import BeautifulSoup, Tag
import os
import json
import lxml.html
import lxml.html.clean

if __name__ == '__main__':
    noticias = []
    index = 0
    title = subtitle = date = text = ""
    for i in range(1, 4):
        response = requests.get("https://www.aulacodi.cat/actualitat/pagina/" + str(i), headers={'User-Agent': 'Mozilla/5.0'})
        if response.status_code == 200:
            data = response._content
            bs = BeautifulSoup(data, "html.parser")
            if bs:
                articles = bs.find_all('li', {'class': 'item article article_llistat article_noticia'})
                for article in articles:
                    link = article.find('a').get('href')
                    response = requests.get(link, headers={'User-Agent': 'Mozilla/5.0'})
                    if response.status_code == 200:
                        data = response._content
                        bs = BeautifulSoup(data, "html.parser")
                        if bs:
                            title = bs.find('h1', {'class': 'interior-header__title'})
                            if title:
                                title = title.text.strip()

                            subtitle = bs.find('h2', {'class': 'interior-header__subtitle'})
                            if subtitle:
                                subtitle = subtitle.text.strip()
                            else:
                                subtitle = ""

                            date = bs.find('time', {'class': 'interior-header__date'})
                            if date:
                                date = date.text.strip()

                            sections_body = bs.find('div', {'class': 'interior-main__content'})
                            if sections_body:
                                text = sections_body.text.strip()

                            noticias.append({"id": index, "url": link, "title": title, "subtitle": subtitle, "date": date, "content": text})

                            index += 1

            f = open(os.getcwd() + '/aulacodi.json', "w+", encoding='utf-8')
            f.write(json.dumps(noticias, indent=4, ensure_ascii=False))

