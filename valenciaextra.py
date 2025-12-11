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
                articles = bs.find_all('div', {'class': 'csl-inner csl-hot'})[3].find_all('article')
                for article in articles:
                    link = article.find('a').get('href')
                    response = requests.get(link, headers={'User-Agent': 'Mozilla/5.0'})
                    if response.status_code == 200:
                        data = response._content
                        bs = BeautifulSoup(data, "html.parser")
                        if bs:
                            title = bs.find('h1', {'class': 'c-mainarticle__title'})
                            if title:
                                title = title.text.strip()

                            subtitle = bs.find('h2', {'class': 'c-mainarticle__subtitle'})
                            if subtitle:
                                subtitle = subtitle.text.strip()
                            else:
                                subtitle = ""

                            date = bs.find('time', {'class': 'c-mainarticle__time'})
                            if date:
                                date = date.text.strip()

                            sections_body = bs.find('div', {'class': 'c-mainarticle__body'})
                            text = ""
                            if sections_body:
                                for element in sections_body:
                                    if isinstance(element, Tag):
                                        if 'p' == element.name:
                                            text += element.text + '\n'

                            noticias_val.append({"id": index, "url": link, "title": title, "subtitle": subtitle, "date": date, "content": text})

                            index += 1

            f = open(os.getcwd() + '/valenciaextra-val.json', "w+", encoding='utf-8')
            f.write(json.dumps(noticias_val, indent=4, ensure_ascii=False))
            print("PÁGINA NÚMERO: " + str(index) + " DESCARGADA")

            return index

    index = 0
    title = subtitle = date = text = ""
    noticias_val = []
    noticias_es = []
    page = 0
    for i in range(1, 6):
        response = requests.get("https://www.valenciaextra.com/valencia?_page=" + str(i), headers={'User-Agent': 'Mozilla/5.0'})
        index = print_noticias(index, response)
    for i in range(1, 6):
        response = requests.get("https://www.valenciaextra.com/politica?_page=" + str(i), headers={'User-Agent': 'Mozilla/5.0'})
        index = print_noticias(index, response)
    for i in range(1, 6):
        response = requests.get("https://www.valenciaextra.com/economia?_page=" + str(i), headers={'User-Agent': 'Mozilla/5.0'})
        index = print_noticias(index, response)
    for i in range(1, 6):
        response = requests.get("https://www.valenciaextra.com/societat?_page=" + str(i), headers={'User-Agent': 'Mozilla/5.0'})
        index = print_noticias(index, response)
    for i in range(1, 6):
        response = requests.get("https://www.valenciaextra.com/innovacio?_page=" + str(i), headers={'User-Agent': 'Mozilla/5.0'})
        index = print_noticias(index, response)
    for i in range(1, 6):
        response = requests.get("https://www.valenciaextra.com/cultura?_page=" + str(i), headers={'User-Agent': 'Mozilla/5.0'})
        index = print_noticias(index, response)
    for i in range(1, 6):
        response = requests.get("https://www.valenciaextra.com/successos?_page=" + str(i), headers={'User-Agent': 'Mozilla/5.0'})
        index = print_noticias(index, response)
    for i in range(1, 6):
        response = requests.get("https://www.valenciaextra.com/oci?_page=" + str(i), headers={'User-Agent': 'Mozilla/5.0'})
        index = print_noticias(index, response)
    for i in range(1, 5):
        response = requests.get("https://www.valenciaextra.com/volea?_page=" + str(i), headers={'User-Agent': 'Mozilla/5.0'})
        index = print_noticias(index, response)


