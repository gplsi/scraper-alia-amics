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
                articles = bs.find('section').find_all('div')[1].find_all('div')[2].find_all('figure')
                for article in articles:
                    link = article.find('a').get('href')
                    response = requests.get(link, headers={'User-Agent': 'Mozilla/5.0'})
                    if response.status_code == 200:
                        data = response._content
                        bs = BeautifulSoup(data, "html.parser")
                        if bs:
                            title = bs.find('h1', {'class': 'intro-below'})
                            if title:
                                title = title.text.strip()

                            subtitle = bs.find('p', {'class': 'intro-noticia'})
                            if subtitle:
                                subtitle = subtitle.text.strip()
                            else:
                                subtitle = ""

                            date = bs.find('span', {'class': 'sublist-title text-uppercase'})
                            if date:
                                date = date.text.strip()

                            sections_body = bs.find('div', {'class': 'new-body  '})
                            text = ""
                            if sections_body:
                                    text += sections_body.text

                            noticias_val.append({"id": index, "url": link, "title": title, "subtitle": subtitle, "date": date, "content": text})

                            link_cas = bs.find('p', {'class': 'wpml-ls-statics-post_translations wpml-ls'}).find('a').get('href')
                            response = requests.get(link_cas, headers={'User-Agent': 'Mozilla/5.0'})
                            if response.status_code == 200:
                                data = response._content
                                bs = BeautifulSoup(data, "html.parser")
                                if bs:
                                    title = bs.find('h1', {'class': 'entry-title'})
                                    if title:
                                        title = title.text.strip()

                                        # subtitle = bs.find('div', {'class': 'art-article'}).find('strong')
                                        # if subtitle:
                                        #    subtitle = subtitle.text.strip()
                                        # else:
                                        subtitle = ""

                                    date = bs.find('span', {'class': 'entry-meta-date updated'})
                                    if date:
                                        date = date.text.strip()

                                    sections_body = bs.find('div', {'class': 'entry-content clearfix'}).find_all('p')
                                    sections_body.pop(0)
                                    text = ""
                                    if sections_body:
                                        for element in sections_body:
                                            text += element.text + '\n'

                                    noticias_es.append(
                                        {"id": index, "url": link, "title": title, "subtitle": subtitle, "date": date,
                                         "content": text})

                            index += 1

            f = open(os.getcwd() + '/tucomarca-val.json', "w+", encoding='utf-8')
            f.write(json.dumps(noticias_val, indent=4, ensure_ascii=False))
            f = open(os.getcwd() + '/tucomarca-es.json', "w+", encoding='utf-8')
            f.write(json.dumps(noticias_es, indent=4, ensure_ascii=False))
            print("PÁGINA NÚMERO: " + str(index) + " DESCARGADA")

            return index

    index = 0
    title = subtitle = date = text = ""
    noticias_val = []
    noticias_es = []
    page = 0
    for i in range(1, 194):
        if i == 1:
            response = requests.get("https://comarquesnord.cat/comarques-i-pobles/els-ports/", headers={'User-Agent': 'Mozilla/5.0'})
        else:
            response = requests.get("https://comarquesnord.cat/comarques-i-pobles/els-ports/pagina/" + str(i) + "/", headers={'User-Agent': 'Mozilla/5.0'})
        index = print_noticias(index, response)
    for i in range(1, 94):
        if i == 1:
            response = requests.get("https://comarquesnord.cat/comarques-i-pobles/maestrat/", headers={'User-Agent': 'Mozilla/5.0'})
        else:
            response = requests.get("https://comarquesnord.cat/comarques-i-pobles/maestrat/pagina/" + str(i) + "/", headers={'User-Agent': 'Mozilla/5.0'})
        index = print_noticias(index, response)
    for i in range(1, 4):
        if i == 1:
            response = requests.get("https://comarquesnord.cat/comarques-i-pobles/maestrazgo/", headers={'User-Agent': 'Mozilla/5.0'})
        else:
            response = requests.get("https://comarquesnord.cat/comarques-i-pobles/maestrazgo/pagina/" + str(i) + "/", headers={'User-Agent': 'Mozilla/5.0'})
        index = print_noticias(index, response)