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
                articles = bs.find('div', {'class': 'main-content-left'}).find_all('article')
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
                                date = date.split(" - ")[0]

                            sections_body = bs.find('div', {'class': 'shortcode-content'})
                            text = ""
                            if sections_body:
                                for element in sections_body:
                                    if isinstance(element, Tag):
                                        if 'p' == element.name:
                                            text += element.text + '\n'
                                        if 'h3' == element.name:
                                            text += element.text + '\n'
                                        if 'div' == element.name:
                                            text += element.text + '\n'

                            noticias_val.append({"id": index, "url": link, "title": title, "subtitle": subtitle, "date": date, "content": text})

                            link_es = bs.find('li', {'class': 'lang-es'})
                            response = requests.get(link_es.find('a').get('href'), headers={'User-Agent': 'Mozilla/5.0'})
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
                                        date = date.split(" - ")[0]

                                    sections_body = bs.find('div', {'class': 'shortcode-content'})
                                    text = ""
                                    if sections_body:
                                        for element in sections_body:
                                            if isinstance(element, Tag):
                                                if 'p' == element.name:
                                                    text += element.text + '\n'
                                                if 'h3' == element.name:
                                                    text += element.text + '\n'

                                    noticias_es.append(
                                        {"id": index, "url": link, "title": title, "subtitle": subtitle, "date": date,
                                         "content": text})

                            index += 1

            f = open(os.getcwd() + '/alicantextra-val.json', "w+", encoding='utf-8')
            f.write(json.dumps(noticias_val, indent=4, ensure_ascii=False))
            f = open(os.getcwd() + '/alicantextra-es.json', "w+", encoding='utf-8')
            f.write(json.dumps(noticias_es, indent=4, ensure_ascii=False))
            print("PÁGINA NÚMERO: " + str(index) + " DESCARGADA")

            return index

    index = 0
    title = subtitle = date = text = ""
    noticias_val = []
    noticias_es = []
    for i in range(1, 128):
        response = requests.get("https://alicantextra.com/alacant/page/" + str(i) + "/", headers={'User-Agent': 'Mozilla/5.0'})
        index = print_noticias(index, response)
    for i in range(1, 112):
        response = requests.get("https://alicantextra.com/comarcas/page/" + str(i) + "/", headers={'User-Agent': 'Mozilla/5.0'})
        index = print_noticias(index, response)
    for i in range(1, 4):
        response = requests.get("https://alicantextra.com/economia/page/" + str(i) + "/", headers={'User-Agent': 'Mozilla/5.0'})
        index = print_noticias(index, response)
    for i in range(1, 21):
        response = requests.get("https://alicantextra.com/cultura/page/" + str(i) + "/", headers={'User-Agent': 'Mozilla/5.0'})
        index = print_noticias(index, response)
    for i in range(1, 17):
        response = requests.get("https://alicantextra.com/sucesos/page/" + str(i) + "/", headers={'User-Agent': 'Mozilla/5.0'})
        index = print_noticias(index, response)
    for i in range(1, 25):
        response = requests.get("https://alicantextra.com/politica/page/" + str(i) + "/", headers={'User-Agent': 'Mozilla/5.0'})
        index = print_noticias(index, response)
