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
                articles = bs.find('section', {'id': 'content'}).find_all('article')
                for article in articles:
                    link = article.find('a').get('href')
                    response = requests.get(link, headers={'User-Agent': 'Mozilla/5.0'})
                    if response.status_code == 200:
                        data = response._content
                        bs = BeautifulSoup(data, "html.parser")
                        if bs:
                            title = bs.find('h2', {'class': 'entry-title fusion-post-title'})
                            if title:
                                title = title.text.strip()

                            subtitle = bs.find('div', {'class': 'post-content'}).find('p')
                            if subtitle:
                                subtitle = subtitle.text.strip()
                            else:
                                subtitle = ""

                            dates = bs.find('div', {'class': 'fusion-meta-info-wrapper'}).find_all('span')
                            if dates:
                                    date = dates[2].text.strip()

                            sections_body = bs.find('div', {'class': 'post-content'}).find_all('p')
                            text = ""
                            sections_body.pop()
                            if sections_body:
                                for element in sections_body:
                                    text += element.text + '\n'

                            noticias.append({"id": index, "url": link, "title": title, "subtitle": subtitle, "date": date, "content": text})

                            index += 1

            f = open(os.getcwd() + '/laveudelgamesi.json', "w+", encoding='utf-8')
            f.write(json.dumps(noticias, indent=4, ensure_ascii=False))
            print("PÁGINA NÚMERO: " + str(index) + " DESCARGADA")

            return index

    index = 0
    title = subtitle = date = text = ""
    noticias = []
    for i in range(1, 136):
        response = requests.get("https://www.laveudalgemesi.es/category/act/page/" + str(i) + "/", headers={'User-Agent': 'Mozilla/5.0'})
        index = print_noticias(index, response)
    for i in range(1, 136):
        response = requests.get("https://www.laveudalgemesi.es/category/opi/page/" + str(i) + "/", headers={'User-Agent': 'Mozilla/5.0'})
        index = print_noticias(index, response)
    for i in range(1, 136):
        response = requests.get("https://www.laveudalgemesi.es/category/cul/page/" + str(i) + "/", headers={'User-Agent': 'Mozilla/5.0'})
        index = print_noticias(index, response)
    for i in range(1, 136):
        response = requests.get("https://www.laveudalgemesi.es/category/cam/page/" + str(i) + "/", headers={'User-Agent': 'Mozilla/5.0'})
        index = print_noticias(index, response)
    for i in range(1, 136):
        response = requests.get("https://www.laveudalgemesi.es/category/esports/page/" + str(i) + "/", headers={'User-Agent': 'Mozilla/5.0'})
        index = print_noticias(index, response)
    for i in range(1, 136):
        response = requests.get("https://www.laveudalgemesi.es/category/sal/page/" + str(i) + "/", headers={'User-Agent': 'Mozilla/5.0'})
        index = print_noticias(index, response)
    for i in range(1, 136):
        response = requests.get("https://www.laveudalgemesi.es/category/soc/page/" + str(i) + "/", headers={'User-Agent': 'Mozilla/5.0'})
        index = print_noticias(index, response)
