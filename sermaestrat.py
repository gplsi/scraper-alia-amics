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
                articles = bs.find('div', {'class': 'elementor-element elementor-element-be72dab elementor-posts--align-left elementor-widget__width-initial elementor-grid-3 elementor-grid-tablet-2 elementor-grid-mobile-1 elementor-posts--thumbnail-top elementor-widget elementor-widget-posts'}).find_all('article')
                for article in articles:
                    link = article.find('h3', {'class': 'elementor-post__title'}).find('a')
                    if "Podcast" not in link.text:
                        response = requests.get(link.get('href'), headers={'User-Agent': 'Mozilla/5.0'})
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

                                date = bs.find('time', {'class': 'entry-date published'})
                                if date:
                                    date = date.text.strip()

                                sections_body = bs.find('div', {'class': 'elementor-widget-wrap elementor-element-populated'}).find('div').find('div')
                                text = ""
                                if sections_body:
                                    for element in sections_body:
                                        if isinstance(element, Tag):
                                            if 'p' == element.name:
                                                text += element.text + '\n'
                                            if 'ul' == element.name:
                                                subtitle = element.text.strip()

                                noticias_val.append({"id": index, "url": link.get('href'), "title": title, "subtitle": subtitle, "date": date, "content": text})

                                index += 1

            f = open(os.getcwd() + '/sermaestrat.json', "w+", encoding='utf-8')
            f.write(json.dumps(noticias_val, indent=4, ensure_ascii=False))
            print("PÁGINA NÚMERO: " + str(index) + " DESCARGADA")

            return index

    index = 0
    title = subtitle = date = text = ""
    noticias_val = []
    noticias_es = []
    page = 0
    for i in range(1, 115):
        response = requests.get("https://sermaestrat.com/?e-page-be72dab=" + str(i), headers={'User-Agent': 'Mozilla/5.0'})
        index = print_noticias(index, response)



