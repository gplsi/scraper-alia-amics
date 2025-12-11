import requests
from bs4 import BeautifulSoup, Tag
import os
import json

if __name__ == '__main__':
    noticias = []
    index = 0
    title = subtitle = date = text = ""
    for i in range(1, 761):
        response = requests.get("https://www.lasbandasdemusica.com/category/noticies/page/" + str(i) + "/", headers={'User-Agent': 'Mozilla/5.0'})
        if response.status_code == 200:
            data = response._content
            bs = BeautifulSoup(data, "html.parser")
            if bs:
                articles = bs.find_all('article', {'class': 'jeg_post jeg_pl_lg_2 format-standard'})
                for article in articles:
                    link = article.find('a').get('href')
                    response = requests.get(link, headers={'User-Agent': 'Mozilla/5.0'})
                    if response.status_code == 200:
                        data = response._content
                        bs = BeautifulSoup(data, "html.parser")
                        if bs:
                            title = bs.find('h1', {'class': 'jeg_post_title'})
                            if title:
                                title = title.text.strip()

                            subtitle = bs.find('h2', {'class': 'jeg_post_subtitle'})
                            if subtitle:
                                subtitle = subtitle.text.strip()
                            else:
                                subtitle = ""

                            date = bs.find('div', {'class': 'jeg_meta_date'})
                            if date:
                                date = date.text.strip()

                            sections_body = bs.find('div', {'class': 'content-inner'})
                            text = ""
                            if sections_body:
                                for element in sections_body:
                                    if isinstance(element, Tag):
                                        if 'p' == element.name:
                                            text += element.text + '\n'
                                        elif 'h1' == element.name:
                                            text += element.text + '\n'

                            noticias.append({"id": index, "url": link, "title": title, "subtitle": subtitle, "date": date, "content": text})

                            index += 1

            f = open(os.getcwd() + '/lesbandesdemusica.json', "w+", encoding='utf-8')
            f.write(json.dumps(noticias, indent=4, ensure_ascii=False))
            print("PÁGINA NÚMERO: " + str(index) + " DESCARGADA")

