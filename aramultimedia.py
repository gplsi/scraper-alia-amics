import requests
from bs4 import BeautifulSoup, Tag
import os
import json

if __name__ == '__main__':
    noticias = []
    index = 0
    title = subtitle = date = text = ""
    for i in range(1, 3):
        if i == 1:
            response = requests.get("https://www.aramultimedia.com/ca/noticies", headers={'User-Agent': 'Mozilla/5.0'})
        else:
            response = requests.get("https://www.aramultimedia.com/ca/opinio", headers={'User-Agent': 'Mozilla/5.0'})
        if response.status_code == 200:
            data = response._content
            bs = BeautifulSoup(data, "html.parser")
            if bs:
                articles = bs.find('ul', {'class': 'col-33'}).find_all('li')
                for article in articles:
                    link = article.find('a').get('href')
                    response = requests.get(link, headers={'User-Agent': 'Mozilla/5.0'})
                    if response.status_code == 200:
                        data = response._content
                        bs = BeautifulSoup(data, "html.parser")
                        if bs:
                            title = bs.find('h1')
                            if title:
                                title = title.text.strip()

                            subtitle = bs.find('div', {'class': 'editor_content resumen'})
                            if subtitle:
                                subtitle = subtitle.text.strip()
                            if i == 2:
                                subtitle = ""

                            date = bs.find('time', {'class': 'text'})
                            if date:
                                date = date.text.strip()

                            if i == 1:
                                sections_body = bs.find('div', {'class': 'content col-70'}).find_all('div', {'class': 'editor_content'})
                            else:
                                sections_body = bs.find('div', {'class': 'col-70'}).find('div', {'class': 'editor_content no_figure'})
                            text = ""
                            if sections_body:
                                if i == 1:
                                    for element in sections_body[1]:
                                        if isinstance(element, Tag):
                                            if 'p' == element.name:
                                                text += element.text + '\n'
                                else:
                                    for element in sections_body:
                                        if isinstance(element, Tag):
                                            if 'p' == element.name:
                                                text += element.text + '\n'

                            noticias.append({"id": index, "url": link, "title": title, "subtitle": subtitle, "date": date, "content": text})

                            index += 1

            f = open(os.getcwd() + '/aramultimedia.json', "w+", encoding='utf-8')
            f.write(json.dumps(noticias, indent=4, ensure_ascii=False))

