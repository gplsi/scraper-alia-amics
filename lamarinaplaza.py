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
                articles = bs.find_all('div', {'class': 'col-md-6 col-sm-6 col-xs-12 pt-cv-content-item pt-cv-1-col'})
                for article in articles:
                    link = article.find('a')
                    if link:
                        link = link.get('href')
                        response = requests.get(link, headers={'User-Agent': 'Mozilla/5.0'})
                        if response.status_code == 200:
                            data = response._content
                            bs = BeautifulSoup(data, "html.parser")
                            if bs:
                                title = bs.find('h1', {'class': 'posttitle'})
                                if title:
                                    title = title.text.strip()

                                #subtitle = bs.find('h2', {'class': 'jeg_post_subtitle'})
                                #if subtitle:
                                #    subtitle = subtitle.text.strip()
                                #else:
                                #    subtitle = ""

                                date = bs.find('div', {'id': 'datemeta_l'})
                                if date:
                                    date = date.text.strip()

                                sections_body = bs.find('div', {'class': 'entry'})
                                text = ""
                                if sections_body:
                                    for element in sections_body:
                                        if isinstance(element, Tag):
                                            if 'p' == element.name:
                                                text += element.text + '\n'
                                            elif 'h5' == element.name:
                                                text += element.text + '\n'
                                            elif 'li' == element.name:
                                                text += element.text + '\n'

                                noticias_val.append({"id": index, "url": link, "title": title, "subtitle": "", "date": date, "content": text})

                                link_es = bs.find('li', {'class': 'icl-es wpml-ls-slot-shortcode_actions wpml-ls-item wpml-ls-item-es wpml-ls-first-item wpml-ls-item-legacy-list-horizontal'}).find('a').get('href')
                                response = requests.get(link_es, headers={'User-Agent': 'Mozilla/5.0'})
                                if response.status_code == 200:
                                    data = response._content
                                    bs = BeautifulSoup(data, "html.parser")
                                    if bs:
                                        title = bs.find('h1', {'class': 'posttitle'})
                                        if title:
                                            title = title.text.strip()

                                        # subtitle = bs.find('h2', {'class': 'jeg_post_subtitle'})
                                        # if subtitle:
                                        #    subtitle = subtitle.text.strip()
                                        # else:
                                        #    subtitle = ""

                                        date = bs.find('div', {'id': 'datemeta_l'})
                                        if date:
                                            date = date.text.strip()

                                        sections_body = bs.find('div', {'class': 'entry'})
                                        text = ""
                                        if sections_body:
                                            for element in sections_body:
                                                if isinstance(element, Tag):
                                                    if 'p' == element.name:
                                                        text += element.text + '\n'
                                                    elif 'h5' == element.name:
                                                        text += element.text + '\n'
                                                    elif 'li' == element.name:
                                                        text += element.text + '\n'

                                        noticias_es.append(
                                            {"id": index, "url": link, "title": title, "subtitle": "", "date": date,
                                             "content": text})
                            index += 1

            f = open(os.getcwd() + '/lamarinaplaza-val.json', "w+", encoding='utf-8')
            f.write(json.dumps(noticias_val, indent=4, ensure_ascii=False))
            f = open(os.getcwd() + '/lamarinaplaza-es.json', "w+", encoding='utf-8')
            f.write(json.dumps(noticias_es, indent=4, ensure_ascii=False))
            print("PÁGINA NÚMERO: " + str(index) + " DESCARGADA")

            return index

    index = 0
    title = subtitle = date = text = ""
    noticias_val = []
    noticias_es = []
    for i in range(1, 138):
        response = requests.get("https://lamarinaplaza.com/ca/economia-i-turisme-noticies/?_page=" + str(i), headers={'User-Agent': 'Mozilla/5.0'})
        index = print_noticias(index, response)
    for i in range(1, 182):
        response = requests.get("https://lamarinaplaza.com/ca/cultura-noticies/?_page=" + str(i), headers={'User-Agent': 'Mozilla/5.0'})
        index = print_noticias(index, response)
    for i in range(1, 105):
        response = requests.get("https://lamarinaplaza.com/ca/opinio-noticies/?_page=" + str(i), headers={'User-Agent': 'Mozilla/5.0'})
        index = print_noticias(index, response)
    for i in range(1, 8):
        response = requests.get("https://lamarinaplaza.com/ca/editorial-noticies/?_page=" + str(i), headers={'User-Agent': 'Mozilla/5.0'})
        index = print_noticias(index, response)
    for i in range(1, 17):
        response = requests.get("https://lamarinaplaza.com/ca/entrevistes-noticies/?_page=" + str(i), headers={'User-Agent': 'Mozilla/5.0'})
        index = print_noticias(index, response)
    for i in range(1, 98):
        response = requests.get("https://lamarinaplaza.com/ca/reportatge-noticies/?_page=" + str(i), headers={'User-Agent': 'Mozilla/5.0'})
        index = print_noticias(index, response)
    for i in range(1, 73):
        response = requests.get("https://lamarinaplaza.com/ca/educacio-noticies/?_page=" + str(i), headers={'User-Agent': 'Mozilla/5.0'})
        index = print_noticias(index, response)
    for i in range(1, 56):
        response = requests.get("https://lamarinaplaza.com/ca/noticies-gastronomia/?_page=" + str(i), headers={'User-Agent': 'Mozilla/5.0'})
        index = print_noticias(index, response)
    for i in range(1, 18):
        response = requests.get("https://lamarinaplaza.com/ca/la-marina-plaza-a-lescola-noticies/?_page=" + str(i), headers={'User-Agent': 'Mozilla/5.0'})
        index = print_noticias(index, response)