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
                articles = bs.find('div', {'id': 'content'}).find_all('article')
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

                            subtitle = bs.find('h2')
                            if subtitle:
                                subtitle = subtitle.text.strip()
                            else:
                                subtitle = ""

                            date = bs.find('span', {'class': 'meta-date'})
                            if date:
                                date = date.text.strip()

                            sections_body = bs.find('div', {'class': 'entry-content clearfix'})
                            text = ""
                            if sections_body:
                                for element in sections_body:
                                    if isinstance(element, Tag):
                                        if 'p' == element.name:
                                            text += element.text + '\n'

                            noticias.append({"id": index, "url": link, "title": title, "subtitle": subtitle, "date": date, "content": text})

                            index += 1

            f = open(os.getcwd() + '/elnostreciutat.json', "w+", encoding='utf-8')
            f.write(json.dumps(noticias, indent=4, ensure_ascii=False))
            print("PÁGINA NÚMERO: " + str(index) + " DESCARGADA")

            return index

    index = 0
    title = subtitle = date = text = ""
    noticias = []
    for i in range(1, 1052):
        response = requests.get("https://www.elnostreciutat.com/categoria/actualidad/page" + str(i) + "/", headers={'User-Agent': 'Mozilla/5.0'})
        index = print_noticias(index, response)
    for i in range(1, 183):
        response = requests.get("https://www.elnostreciutat.com/categoria/cultura/page/" + str(i) + "/", headers={'User-Agent': 'Mozilla/5.0'})
        index = print_noticias(index, response)
    for i in range(1, 41):
        response = requests.get("https://www.elnostreciutat.com/categoria/educacio/page/" + str(i) + "/", headers={'User-Agent': 'Mozilla/5.0'})
        index = print_noticias(index, response)
    for i in range(1, 263):
        response = requests.get("https://www.elnostreciutat.com/categoria/comarca/page/" + str(i) + "/", headers={'User-Agent': 'Mozilla/5.0'})
        index = print_noticias(index, response)
    for i in range(1, 359):
        response = requests.get("https://www.elnostreciutat.com/categoria/deportes/page/" + str(i) + "/", headers={'User-Agent': 'Mozilla/5.0'})
        index = print_noticias(index, response)
    for i in range(1, 136):
        response = requests.get("https://www.elnostreciutat.com/categoria/economia/page/" + str(i) + "/", headers={'User-Agent': 'Mozilla/5.0'})
        index = print_noticias(index, response)
    for i in range(1, 120):
        response = requests.get("https://www.elnostreciutat.com/categoria/opinion/page/" + str(i) + "/", headers={'User-Agent': 'Mozilla/5.0'})
        index = print_noticias(index, response)
