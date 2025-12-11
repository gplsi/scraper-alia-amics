import requests
from bs4 import BeautifulSoup, Tag
import os
import json

if __name__ == '__main__':

    def print_noticias(index, response):
        if response.status_code == 200:
            data = response._content
            bs = BeautifulSoup(data, "html.parser")
            if bs:
                articles = bs.find('div', {'class': 'main-content-left'}).find_all('div')[2].find_all('article')
                for article in articles:
                    link = article.find('a').get('href')
                    response = requests.get(link, headers={'User-Agent': 'Mozilla/5.0'})
                    if response.status_code == 200:
                        data = response._content
                        bs = BeautifulSoup(data, "html.parser")
                        if bs:
                            title = bs.find('h1', {'class': 'article-title'})
                            if title:
                                title = title.text.strip()

                            subtitle = bs.find('h2', {'class': 'article-subtitle'})
                            if subtitle:
                                subtitle = subtitle.text.strip()
                            else:
                                subtitle = ""

                            date = bs.find('div', {'class': 'calendar-date'})
                            if date:
                                date = date.text.strip()

                            sections_body = bs.find('div', {'class': 'shortcode-content'})
                            text = ""
                            if sections_body:
                                for element in sections_body:
                                    if isinstance(element, Tag):
                                        if 'p' == element.name:
                                            text += element.text + '\n'
                                        if 'h2' == element.name:
                                            text += element.text + '\n'

                            noticias.append({"id": index, "url": link, "title": title, "subtitle": subtitle, "date": date, "content": text})

                            index += 1

            f = open(os.getcwd() + '/castelloextra-val.json', "w+", encoding='utf-8')
            f.write(json.dumps(noticias, indent=4, ensure_ascii=False))
            print("PÁGINA NÚMERO: " + str(index) + " DESCARGADA")

            return index

    index = 0
    title = subtitle = date = text = ""
    noticias = []
    page = 0
    for i in range(1, 122):
        response = requests.get("https://castelloextra.com/castello/page/" + str(i) + "/", headers={'User-Agent': 'Mozilla/5.0'})
        index = print_noticias(index, response)
    for i in range(1, 33):
        response = requests.get("https://castelloextra.com/vila-real/page/" + str(i) + "/", headers={'User-Agent': 'Mozilla/5.0'})
        index = print_noticias(index, response)
    for i in range(1, 284):
        response = requests.get("https://castelloextra.com/comarcas/page/" + str(i) + "/", headers={'User-Agent': 'Mozilla/5.0'})
        index = print_noticias(index, response)
    for i in range(1, 9):
        response = requests.get("https://castelloextra.com/economia/page/" + str(i) + "/", headers={'User-Agent': 'Mozilla/5.0'})
        index = print_noticias(index, response)
    for i in range(1, 18):
        response = requests.get("https://castelloextra.com/cultura/page/" + str(i) + "/", headers={'User-Agent': 'Mozilla/5.0'})
        index = print_noticias(index, response)
    for i in range(1, 9):
        response = requests.get("https://castelloextra.com/sucesos/page/" + str(i) + "/", headers={'User-Agent': 'Mozilla/5.0'})
        index = print_noticias(index, response)
    for i in range(1, 35):
        response = requests.get("https://castelloextra.com/politica/page/" + str(i) + "/", headers={'User-Agent': 'Mozilla/5.0'})
        index = print_noticias(index, response)