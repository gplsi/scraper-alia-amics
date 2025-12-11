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
                articles = bs.find('div', {'class': 'td-ss-main-content'}).find_all('div', {'class': 'td_module_10 td_module_wrap td-animation-stack td-cpt-post'})
                for article in articles:
                    link = article.find('a').get('href')
                    response = requests.get(link, headers={'User-Agent': 'Mozilla/5.0'})
                    if response.status_code == 200:
                        data = response._content
                        bs = BeautifulSoup(data, "html.parser")
                        if bs:
                            title = bs.find('h1', {'class': 'entry-title'})
                            if title:
                                title = title.text.strip()

                            #subtitle = bs.find('h2', {'class': 'c-mainarticle__subtitle'})
                            #if subtitle:
                            #    subtitle = subtitle.text.strip()
                            #else:
                            subtitle = ""

                            date = bs.find('time', {'class': 'entry-date updated td-module-date'})
                            if date:
                                date = date.text.strip()

                            sections_body = bs.find('div', {'class': 'td-post-content td-pb-padding-side'})
                            text = ""
                            if sections_body:
                                for element in sections_body:
                                    if isinstance(element, Tag):
                                        if 'p' == element.name:
                                            text += element.text + '\n'
                            if text == "":
                                sections_body = sections_body.find('div')
                                if sections_body:
                                    for element in sections_body:
                                        if isinstance(element, Tag):
                                            if 'p' == element.name:
                                                text += element.text + '\n'

                            noticias_val.append({"id": index, "url": link, "title": title, "subtitle": subtitle, "date": date, "content": text})

                            index += 1

            f = open(os.getcwd() + '/7diesactualitat.json', "w+", encoding='utf-8')
            f.write(json.dumps(noticias_val, indent=4, ensure_ascii=False))
            print("PÁGINA NÚMERO: " + str(index) + " DESCARGADA")

            return index

    index = 0
    title = subtitle = date = text = ""
    noticias_val = []
    noticias_es = []
    page = 0
    for i in range(1, 331):
        response = requests.get("https://7diesactualitat.com/category/vinaros/page/" + str(i) + "/", headers={'User-Agent': 'Mozilla/5.0'})
        index = print_noticias(index, response)
    for i in range(1, 239):
        response = requests.get("https://7diesactualitat.com/category/benicarlo/page/" + str(i) + "/", headers={'User-Agent': 'Mozilla/5.0'})
        index = print_noticias(index, response)
    for i in range(1, 110):
        response = requests.get("https://7diesactualitat.com/category/peniscola/page/" + str(i) + "/", headers={'User-Agent': 'Mozilla/5.0'})
        index = print_noticias(index, response)
    for i in range(1, 219):
        response = requests.get("https://7diesactualitat.com/category/comarques/page/" + str(i) + "/", headers={'User-Agent': 'Mozilla/5.0'})
        index = print_noticias(index, response)
    for i in range(1, 33):
        response = requests.get("https://7diesactualitat.com/category/altres/page/" + str(i) + "/", headers={'User-Agent': 'Mozilla/5.0'})
        index = print_noticias(index, response)
    for i in range(1, 144):
        response = requests.get("https://7diesactualitat.com/category/premsavalenciana/page/" + str(i) + "/", headers={'User-Agent': 'Mozilla/5.0'})
        index = print_noticias(index, response)



