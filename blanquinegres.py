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
                articles = bs.find('div', {'id': 'content'}).find_all('article')
                for article in articles:
                    link = article.find('a').get('href')
                    response = requests.get(link, headers={'User-Agent': 'Mozilla/5.0'})
                    if response.status_code == 200:
                        data = response._content
                        bs = BeautifulSoup(data, "html.parser")
                        if bs:
                            title = bs.find('h1')
                            if title:
                                title = title.text.strip()

                            #subtitle = bs.find('p', {'class': 'subtitle'})
                            #if subtitle:
                            #    subtitle = subtitle.text.strip()
                            #else:
                            #    subtitle = ""

                            date = bs.find('div', {'class': 'mt20 mb20'})
                            if date:
                                date = date.text.strip()
                                date = date.split(" · ")[1]

                            sections_body = bs.find('div', {'id': 'content'}).find_all('p')
                            sections_body.pop(0)
                            sections_body.pop(0)
                            text = ""
                            if sections_body:
                                for element in sections_body:
                                    text += element.text + '\n'

                            noticias.append({"id": index, "url": link, "title": title, "subtitle": "", "date": date, "content": text})

                            index += 1

            f = open(os.getcwd() + '/blanquinegres.json', "w+", encoding='utf-8')
            f.write(json.dumps(noticias, indent=4, ensure_ascii=False))
            print("PÁGINA NÚMERO: " + str(index) + " DESCARGADA")

        return index

    index = 0
    title = subtitle = date = text = ""
    noticias = []
    for i in range(1, 2125):
        response = requests.get("https://www.blanquinegres.com/category/actualitat/page/" + str(i) + "/", headers={'User-Agent': 'Mozilla/5.0'})
        index = print_noticias(index, response)
