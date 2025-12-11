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
                articles = bs.find('div', {'id': 'content'}).find_all('div')
                articles.pop()
                articles.pop()
                dates = bs.find_all('span', {'class': 'meta_date'})
                id_date = 0
                for article in articles:
                    link = article.find('a').get('href')
                    response = requests.get(link, headers={'User-Agent': 'Mozilla/5.0'})
                    if response.status_code == 200:
                        data = response._content
                        bs = BeautifulSoup(data, "html.parser")
                        if bs:
                            title = bs.find('h1', {'class': 'entry_title'})
                            if title:
                                title = title.text.strip()

                            subtitle = bs.find('p', {'class': 'subtitle'})
                            if subtitle:
                                subtitle = subtitle.text.strip()
                            else:
                                subtitle = ""

                            date = dates[id_date]
                            if date:
                                date = date.text.strip()
                            id_date += 1

                            sections_body = bs.find('div', {'id': 'content'}).find('div')
                            text = ""
                            if sections_body:
                                for element in sections_body:
                                    if isinstance(element, Tag):
                                        if 'p' == element.name:
                                            text += element.text + '\n'

                            noticias.append({"id": index, "url": link, "title": title, "subtitle": subtitle, "date": date, "content": text})

                            index += 1

            f = open(os.getcwd() + '/lesmuntanyes.json', "w+", encoding='utf-8')
            f.write(json.dumps(noticias, indent=4, ensure_ascii=False))
            print("PÁGINA NÚMERO: " + str(index) + " DESCARGADA")

            return index

    index = 0
    title = subtitle = date = text = ""
    noticias = []
    for i in range(2, 577):
        response = requests.get("https://www.lesmuntanyes.com/category/alcoi/page/" + str(i) + "/", headers={'User-Agent': 'Mozilla/5.0'})
        index = print_noticias(index, response)
    for i in range(2, 242):
        response = requests.get("https://www.lesmuntanyes.com/category/activitats/page/" + str(i) + "/", headers={'User-Agent': 'Mozilla/5.0'})
        index = print_noticias(index, response)
    for i in range(2, 246):
        response = requests.get("https://www.lesmuntanyes.com/category/cultura/page/" + str(i) + "/", headers={'User-Agent': 'Mozilla/5.0'})
        index = print_noticias(index, response)
    for i in range(2, 351):
        response = requests.get("https://www.lesmuntanyes.com/category/societat/page/" + str(i) + "/", headers={'User-Agent': 'Mozilla/5.0'})
        index = print_noticias(index, response)
    for i in range(2, 403):
        response = requests.get("https://www.lesmuntanyes.com/category/comarques/page/" + str(i) + "/", headers={'User-Agent': 'Mozilla/5.0'})
        index = print_noticias(index, response)
    for i in range(2, 59):
        response = requests.get("https://www.lesmuntanyes.com/category/esport/page/" + str(i) + "/", headers={'User-Agent': 'Mozilla/5.0'})
        index = print_noticias(index, response)
