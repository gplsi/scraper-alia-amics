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
                articles = bs.find_all('div', {'class': 'isotope_container_wrap'})[1].find_all('article')
                for article in articles:
                    link = article.find('a').get('href')
                    response = requests.get(link, headers={'User-Agent': 'Mozilla/5.0'})
                    if response.status_code == 200:
                        data = response._content
                        bs = BeautifulSoup(data, "html.parser")
                        if bs:
                            title = bs.find('div', {'class': 'single_post_title'})
                            if title:
                                title = title.text.strip()

                            #subtitle = bs.find('h2')
                            #if subtitle:
                            #    subtitle = subtitle.text.strip()
                            #else:
                            #    subtitle = ""

                            date = bs.find('span', {'class': 'post_meta_date'})
                            if date:
                                date = date.text.strip()

                            sections_body = bs.find('div', {'class': 'single-post-content-wrap clearfix mb10'})
                            text = ""
                            if sections_body:
                                for element in sections_body:
                                    if isinstance(element, Tag):
                                        if 'p' == element.name:
                                            text += element.text + '\n'
                                        if 'ul' == element.name:
                                            text += element.text + '\n'

                            noticias.append({"id": index, "url": link, "title": title, "subtitle": subtitle, "date": date, "content": text})

                            index += 1

            f = open(os.getcwd() + '/latraca.json', "w+", encoding='utf-8')
            f.write(json.dumps(noticias, indent=4, ensure_ascii=False))
            print("PÁGINA NÚMERO: " + str(index) + " DESCARGADA")

            return index

    index = 0
    title = subtitle = date = text = ""
    noticias = []
    for i in range(1, 29):
        response = requests.get("https://latraca.net/page" + str(i) + "/", headers={'User-Agent': 'Mozilla/5.0'})
        index = print_noticias(index, response)
