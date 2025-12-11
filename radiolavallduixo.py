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
                articles = bs.find('div', {'class': 'blog-featured'}).find_all('article', {'class': 'art-post'})
                for article in articles:
                    link = article.find('a').get('href')
                    response = requests.get("https://radiolavallduixo.com" + link, headers={'User-Agent': 'Mozilla/5.0'})
                    if response.status_code == 200:
                        data = response._content
                        bs = BeautifulSoup(data, "html.parser")
                        if bs:
                            title = bs.find('h2', {'class': 'art-postheader'})
                            if title:
                                title = title.text.strip()

                            subtitle = bs.find('div', {'class': 'art-article'}).find('strong')
                            if subtitle:
                                subtitle = subtitle.text.strip()
                            else:
                                subtitle = ""

                            date = bs.find('span', {'class': 'art-postdateicon'})
                            if date:
                                date = date.text.strip()

                            sections_body = bs.find('div', {'class': 'art-article'}).find_all('p')[1]
                            text = ""
                            if sections_body:
                                text = sections_body.text.strip()

                            noticias.append({"id": index, "url": link, "title": title, "subtitle": subtitle, "date": date, "content": text})

                            index += 1

            f = open(os.getcwd() + '/radiolavallduixo.json', "w+", encoding='utf-8')
            f.write(json.dumps(noticias, indent=4, ensure_ascii=False))
            print("PÁGINA NÚMERO: " + str(index) + " DESCARGADA")

            return index

    index = 0
    title = subtitle = date = text = ""
    noticias = []
    page = 0
    for i in range(1, 354):
        if i == 1:
            response = requests.get("https://radiolavallduixo.com/index.php", headers={'User-Agent': 'Mozilla/5.0'})
        else:
            response = requests.get("https://radiolavallduixo.com/index.php?start=" + str(page), headers={'User-Agent': 'Mozilla/5.0'})
        page += 11
        index = print_noticias(index, response)