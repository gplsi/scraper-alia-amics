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
                articles = bs.find('div', {'class': 'uael-post-grid__inner uael-post__columns-2 uael-post__columns-tablet-3 uael-post__columns-mobile-1'}).find_all('div', {'class': 'uael-post__thumbnail'})
                for article in articles:
                    link = article.find('a').get('href')
                    response = requests.get(link, headers={'User-Agent': 'Mozilla/5.0'})
                    if response.status_code == 200:
                        data = response._content
                        bs = BeautifulSoup(data, "html.parser")
                        if bs:
                            title = bs.find('h1', {'class': 'elementor-heading-title elementor-size-default'})
                            if title:
                                title = title.text.strip()

                            #subtitle = bs.find('h2', {'class': 'article-subtitle'})
                            #if subtitle:
                            #    subtitle = subtitle.text.strip()
                            #else:
                                subtitle = ""

                            date = bs.find('span', {'class': 'elementor-icon-list-text elementor-post-info__item elementor-post-info__item--type-date'})
                            if date:
                                date = date.text.strip()

                            sections_body = bs.find('div', {'class': 'elementor-element elementor-element-16fd573a elementor-widget elementor-widget-theme-post-content'}).find('div')
                            text = ""
                            if sections_body:
                                for element in sections_body:
                                    if isinstance(element, Tag):
                                        if 'p' == element.name:
                                            text += element.text + '\n'
                                        if 'h2' == element.name:
                                            text += element.text + '\n'

                            noticias.append({"id": index, "url": link, "title": title, "subtitle": subtitle, "date": date, "content": text})

                            index += 1

            f = open(os.getcwd() + '/diaridelmaestrat.json', "w+", encoding='utf-8')
            f.write(json.dumps(noticias, indent=4, ensure_ascii=False))
            print("PÁGINA NÚMERO: " + str(index) + " DESCARGADA")

            return index

    index = 0
    title = subtitle = date = text = ""
    noticias = []
    page = 0
    for i in range(1, 101):
        response = requests.get("https://diaridelmaestrat.com/categoria/benicarlo/page" + str(i) + "/", headers={'User-Agent': 'Mozilla/5.0'})
        index = print_noticias(index, response)
    for i in range(1, 101):
        response = requests.get("https://diaridelmaestrat.com/categoria/vianaros/page" + str(i) + "/", headers={'User-Agent': 'Mozilla/5.0'})
        index = print_noticias(index, response)
    for i in range(1, 101):
        response = requests.get("https://diaridelmaestrat.com/categoria/peniscola/page" + str(i) + "/", headers={'User-Agent': 'Mozilla/5.0'})
        index = print_noticias(index, response)
    for i in range(1, 101):
        response = requests.get("https://diaridelmaestrat.com/categoria/comarques/page" + str(i) + "/", headers={'User-Agent': 'Mozilla/5.0'})
        index = print_noticias(index, response)
    for i in range(1, 101):
        response = requests.get("https://diaridelmaestrat.com/categoria/successos/page" + str(i) + "/", headers={'User-Agent': 'Mozilla/5.0'})
        index = print_noticias(index, response)
    for i in range(1, 101):
        response = requests.get("https://diaridelmaestrat.com/categoria/diputacio/page" + str(i) + "/", headers={'User-Agent': 'Mozilla/5.0'})
        index = print_noticias(index, response)
    for i in range(1, 101):
        response = requests.get("https://diaridelmaestrat.com/categoria/politica/page" + str(i) + "/", headers={'User-Agent': 'Mozilla/5.0'})
        index = print_noticias(index, response)
    for i in range(1, 101):
        response = requests.get("https://diaridelmaestrat.com/categoria/societat/page" + str(i) + "/", headers={'User-Agent': 'Mozilla/5.0'})
        index = print_noticias(index, response)
    for i in range(1, 101):
        response = requests.get("https://diaridelmaestrat.com/categoria/cultura/page" + str(i) + "/", headers={'User-Agent': 'Mozilla/5.0'})
        index = print_noticias(index, response)
    for i in range(1, 101):
        response = requests.get("https://diaridelmaestrat.com/categoria/esports/page" + str(i) + "/", headers={'User-Agent': 'Mozilla/5.0'})
        index = print_noticias(index, response)