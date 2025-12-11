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
                articles = bs.find('div', {'id': 'principal'}).find_all('div', {'class': 'col-sm-6 noticia-otra'})
                for article in articles:
                    link = article.find('a').get('href')
                    response = requests.get("https://www.noticiasmarinaalta.es" + link, headers={'User-Agent': 'Mozilla/5.0'})
                    if response.status_code == 200:
                        data = response._content
                        bs = BeautifulSoup(data, "html.parser")
                        if bs:
                            title = bs.find('div', {'class': 'title-home'})
                            if title:
                                title = title.text.strip()

                            subtitle = bs.find('h2', {'class': 'article-subtitle'})
                            if subtitle:
                                subtitle = subtitle.text.strip()
                            else:
                                subtitle = ""

                            date = bs.find('div', {'class': 'fecha-art'})
                            if date:
                                date = date.text.strip()
                                date = date.split(" - ")[0]

                            sections_body = bs.find('div', {'class': 'cuerpo-text'})
                            text = ""
                            if sections_body:
                                for element in sections_body:
                                    if isinstance(element, Tag):
                                        if 'p' == element.name:
                                            text += element.text + '\n'

                            noticias.append({"id": index, "url": link, "title": title, "subtitle": subtitle, "date": date, "content": text})

                            index += 1

            f = open(os.getcwd() + '/noticiasmarinaalta.json', "w+", encoding='utf-8')
            f.write(json.dumps(noticias, indent=4, ensure_ascii=False))
            print("PÁGINA NÚMERO: " + str(index) + " DESCARGADA")

            return index

    index = 0
    title = subtitle = date = text = ""
    noticias = []
    for i in range(1, 877):
        response = requests.get("https://www.noticiasmarinaalta.es/canfali/seccion/pol%C3%83%C6%92%C3%86%E2%80%99%C3%83%E2%80%9A%C3%82%C2%ADtica/pag" + str(i) + "/", headers={'User-Agent': 'Mozilla/5.0'})
        index = print_noticias(index, response)
    for i in range(1, 31):
        response = requests.get("https://www.noticiasmarinaalta.es/canfali/seccion/sociedad/pag/" + str(i) + "/", headers={'User-Agent': 'Mozilla/5.0'})
        index = print_noticias(index, response)
    for i in range(1, 49):
        response = requests.get("https://www.noticiasmarinaalta.es/canfali/seccion/salud/pag/" + str(i) + "/", headers={'User-Agent': 'Mozilla/5.0'})
        index = print_noticias(index, response)
    for i in range(1, 35):
        response = requests.get("https://www.noticiasmarinaalta.es/canfali/seccion/cultura/pag/" + str(i) + "/", headers={'User-Agent': 'Mozilla/5.0'})
        index = print_noticias(index, response)
    for i in range(1, 108):
        response = requests.get("https://www.noticiasmarinaalta.es/canfali/seccion/deportes/pag/" + str(i) + "/", headers={'User-Agent': 'Mozilla/5.0'})
        index = print_noticias(index, response)
    for i in range(1, 37):
        response = requests.get("https://www.noticiasmarinaalta.es/canfali/seccion/sucesos/pag/" + str(i) + "/", headers={'User-Agent': 'Mozilla/5.0'})
        index = print_noticias(index, response)
    for i in range(1, 16):
        response = requests.get("https://www.noticiasmarinaalta.es/canfali/seccion/fiestas/pag/" + str(i) + "/", headers={'User-Agent': 'Mozilla/5.0'})
        index = print_noticias(index, response)
    for i in range(1, 18):
        response = requests.get("https://www.noticiasmarinaalta.es/canfali/seccion/opinion/pag/" + str(i) + "/", headers={'User-Agent': 'Mozilla/5.0'})
        index = print_noticias(index, response)
    for i in range(1, 11):
        response = requests.get("https://www.noticiasmarinaalta.es/canfali/seccion/la-ultima/pag/" + str(i) + "/", headers={'User-Agent': 'Mozilla/5.0'})
        index = print_noticias(index, response)
