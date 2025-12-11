import requests
from bs4 import BeautifulSoup, Tag
import os
import json
from tqdm import tqdm

if __name__ == '__main__':
    noticias = []
    index = 0
    title = date = text = author = category = ""

    for i in range(1, 3):
        page_number = 1
        if i == 1:
            response = requests.get("https://www.tresdeu.com/category/cultura", headers={'User-Agent': 'Mozilla/5.0'})
        else:
            response = requests.get("https://www.tresdeu.com/category/tendencies", headers={'User-Agent': 'Mozilla/5.0'})
        if response.status_code == 200:
            data = response._content
            bs = BeautifulSoup(data, "html.parser")
            if bs:
                page_number_array = bs.find_all('a', {'class': 'page-numbers'})
                lol = [int(a.text) for a in page_number_array if a.text.isdigit()]
                page_number_max = max(lol)

        for page_number in range (1 , page_number_max + 1):
            if i == 1:
                response = requests.get("https://www.tresdeu.com/category/cultura" + f"/page/{page_number}" if page_number > 1 else "https://www.tresdeu.com/category/cultura", headers={'User-Agent': 'Mozilla/5.0'})
                category = "Cultura"
            else:
                response = requests.get("https://www.tresdeu.com/category/tendencies" + f"/page/{page_number}" if page_number > 1 else "https://www.tresdeu.com/category/tendencies", headers={'User-Agent': 'Mozilla/5.0'})
                category = "Tendencies"

            if response.status_code == 200:
                data = response._content
                bs = BeautifulSoup(data, "html.parser")
                if bs:
                    articles = bs.find('div', {'class': 'posts-list'}).find_all('div', {'class': 'card card--category'})
                    for article in tqdm(articles):
                        link = article.find('a').get('href')
                        response = requests.get(link, headers={'User-Agent': 'Mozilla/5.0'})
                        if response.status_code == 200:
                            data = response._content
                            bs = BeautifulSoup(data, "html.parser")
                            if bs:
                                title = bs.find('h1')
                                if title:
                                    title = title.text.strip()

                                date = bs.find('div', {'class': 'post-meta__date text-3'})
                                if date:
                                    date = date.text.strip()

                                author = bs.find('div', {'class': 'post-author__name text-3'})
                                if author:
                                    author = author.text.strip()
                                
                                sections_body = bs.find('div', {'class': 'post-entry__wrap'}).find_all('div', {'class': 'post-entry__content'})
                            
                                text = ""
                                if sections_body:
                                    for element in sections_body[0]:
                                        if isinstance(element, Tag):
                                            if 'p' == element.name:
                                                text += element.text + '\n'
                                            if 'h2' == element.name:
                                                text += element.text + '\n'
                                            if 'h3' == element.name:
                                                text += element.text + '\n'
                                            if 'h4' == element.name:
                                                text += element.text + '\n'   

                                noticias.append({"id": index, "url": link, "title": title, "category": category, "author": author, "date": date, "content": text, "page": page_number})

                                index += 1

                f = open(os.getcwd() + '/tresdeu.json', "w+", encoding='utf-8')
                f.write(json.dumps(noticias, indent=4, ensure_ascii=False))

