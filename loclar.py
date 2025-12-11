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
                articles = bs.find('section', {'class': 'row post-seven'}).find_all('a')
                for article in articles:
                    link = article.get('href')
                    response = requests.get("https://loclar.es" + link, headers={'User-Agent': 'Mozilla/5.0'})
                    if response.status_code == 200:
                        data = response._content
                        bs = BeautifulSoup(data, "html.parser")
                        if bs:
                            title = bs.find('h2', {'class': 'post-title'})
                            if title:
                                title = title.text.strip()

                            subtitle = bs.find('p', {'class': 'col s12 post-subtitle'})
                            if subtitle:
                                subtitle = subtitle.text.strip()
                            else:
                                subtitle = ""

                            date = bs.find('div', {'class': 'col s12 date-category'})
                            if date:
                                date = date.text.strip()

                            sections_body = bs.find('div', {'class': 'col s12 post-content'})
                            text = ""
                            if sections_body:
                                for element in sections_body:
                                    if isinstance(element, Tag):
                                        if 'div' == element.name:
                                            text += element.text + '\n'

                            noticias_val.append({"id": index, "url": link, "title": title, "subtitle": subtitle, "date": date, "content": text})

                            index += 1

            f = open(os.getcwd() + '/loclar-val.json', "w+", encoding='utf-8')
            f.write(json.dumps(noticias_val, indent=4, ensure_ascii=False))
            print("PÁGINA NÚMERO: " + str(index) + " DESCARGADA")

            return index

    index = 0
    title = subtitle = date = text = ""
    noticias_val = []
    noticias_es = []
    page = 0
    for i in range(1, 414):
        response = requests.get("https://loclar.es/va/ontinyent/?page=" + str(i), headers={'User-Agent': 'Mozilla/5.0'})
        index = print_noticias(index, response)
    for i in range(1, 133):
        response = requests.get("https://loclar.es/va/esports/?page=" + str(i), headers={'User-Agent': 'Mozilla/5.0'})
        index = print_noticias(index, response)
    for i in range(1, 125):
        response = requests.get("https://loclar.es/va/vall-dalbaida/?page=" + str(i), headers={'User-Agent': 'Mozilla/5.0'})
        index = print_noticias(index, response)
    for i in range(1, 62):
        response = requests.get("https://loclar.es/va/empreses/?page=" + str(i), headers={'User-Agent': 'Mozilla/5.0'})
        index = print_noticias(index, response)
    for i in range(1, 39):
        response = requests.get("https://loclar.es/va/valencia/?page=" + str(i), headers={'User-Agent': 'Mozilla/5.0'})
        index = print_noticias(index, response)
    for i in range(1, 45):
        response = requests.get("https://loclar.es/va/educacio/?page=" + str(i), headers={'User-Agent': 'Mozilla/5.0'})
        index = print_noticias(index, response)
    for i in range(1, 56):
        response = requests.get("https://loclar.es/va/cultura/?page=" + str(i), headers={'User-Agent': 'Mozilla/5.0'})
        index = print_noticias(index, response)
    for i in range(1, 23):
        response = requests.get("https://loclar.es/va/medi-ambient/?page=" + str(i), headers={'User-Agent': 'Mozilla/5.0'})
        index = print_noticias(index, response)
    for i in range(1, 33):
        response = requests.get("https://loclar.es/va/festes/?page=" + str(i), headers={'User-Agent': 'Mozilla/5.0'})
        index = print_noticias(index, response)
    for i in range(1, 20):
        response = requests.get("https://loclar.es/va/opinio/?page=" + str(i), headers={'User-Agent': 'Mozilla/5.0'})
        index = print_noticias(index, response)
