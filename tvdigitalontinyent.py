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
                articles = bs.find('div', {'id': 'tdi_114'}).find_all('div', {'class': 'td-module-thumb'})
                for article in articles:
                    link = article.find('a').get('href')
                    response = requests.get(link, headers={'User-Agent': 'Mozilla/5.0'})
                    if response.status_code == 200:
                        data = response._content
                        bs = BeautifulSoup(data, "html.parser")
                        if bs:
                            title = bs.find('h1', {'class': 'tdb-title-text'})
                            if title:
                                title = title.text.strip()

                            #subtitle = bs.find('p', {'class': 'col s12 post-subtitle'})
                            #if subtitle:
                            #    subtitle = subtitle.text.strip()
                            #else:
                                subtitle = ""

                            date = bs.find('time', {'class': 'entry-date updated td-module-date'})
                            if date:
                                date = date.text.strip()

                            text = ""
                            try:
                                sections_body = bs.find('div', {'class': 'td_block_wrap tdb_single_content tdi_139 td-pb-border-top td_block_template_1 td-post-content tagdiv-type'}).find('div')
                                if sections_body:
                                    for element in sections_body:
                                        if isinstance(element, Tag):
                                            if 'p' == element.name:
                                                text += element.text + '\n'
                            except:
                                pass

                            noticias_val.append({"id": index, "url": link, "title": title, "subtitle": subtitle, "date": date, "content": text})

                            index += 1

            f = open(os.getcwd() + '/tvdigitalontinyent.json', "w+", encoding='utf-8')
            f.write(json.dumps(noticias_val, indent=4, ensure_ascii=False))
            print("PÁGINA NÚMERO: " + str(index) + " DESCARGADA")

            return index

    index = 0
    title = subtitle = date = text = ""
    noticias_val = []
    noticias_es = []
    page = 0
    for i in range(1, 486):
        response = requests.get("https://tvdigitalontinyent.com/category/ontinyent/page/" + str(i), headers={'User-Agent': 'Mozilla/5.0'})
        index = print_noticias(index, response)
    for i in range(1, 53):
        response = requests.get("https://tvdigitalontinyent.com/category/salut/page/" + str(i), headers={'User-Agent': 'Mozilla/5.0'})
        index = print_noticias(index, response)
    for i in range(1, 279):
        response = requests.get("https://tvdigitalontinyent.com/category/economia/page/" + str(i), headers={'User-Agent': 'Mozilla/5.0'})
        index = print_noticias(index, response)
    for i in range(1, 204):
        response = requests.get("https://tvdigitalontinyent.com/category/esports/page/" + str(i), headers={'User-Agent': 'Mozilla/5.0'})
        index = print_noticias(index, response)
    for i in range(1, 118):
        response = requests.get("https://tvdigitalontinyent.com/category/medi-ambient/page/" + str(i), headers={'User-Agent': 'Mozilla/5.0'})
        index = print_noticias(index, response)
    for i in range(1, 264):
        response = requests.get("https://tvdigitalontinyent.com/category/politica/page/" + str(i), headers={'User-Agent': 'Mozilla/5.0'})
        index = print_noticias(index, response)
    for i in range(1, 424):
        response = requests.get("https://tvdigitalontinyent.com/category/cultura/page/" + str(i), headers={'User-Agent': 'Mozilla/5.0'})
        index = print_noticias(index, response)
    for i in range(1, 159):
        response = requests.get("https://tvdigitalontinyent.com/category/societat/page/" + str(i), headers={'User-Agent': 'Mozilla/5.0'})
        index = print_noticias(index, response)
    for i in range(1, 39):
        response = requests.get("https://tvdigitalontinyent.com/category/sucessos/page/" + str(i), headers={'User-Agent': 'Mozilla/5.0'})
        index = print_noticias(index, response)
    for i in range(1, 158):
        response = requests.get("https://tvdigitalontinyent.com/category/vall-dalbaida/page/" + str(i), headers={'User-Agent': 'Mozilla/5.0'})
        index = print_noticias(index, response)

