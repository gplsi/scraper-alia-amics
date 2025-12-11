import requests      
from bs4 import BeautifulSoup, Tag
import os
import json

from selenium.webdriver.common.by import By
from tqdm import tqdm
from selenium import webdriver

if __name__ == '__main__':

    def print_noticias(index, bs):
        #for i in range(1, 8):
            #categoria_actual = categorias[i]  # Obtenemor el nombre de la categoria en la que estamos
            #response = requests.get(f"https://suasesport.com/es/categoria/{categoria_actual}/", headers={'User-Agent': 'Mozilla/5.0'})
        if bs:
            articles = bs.find('div', {'class': 'paginated_content'}).find_all('article')
            for article in tqdm(articles, desc=f"Extrayendo de suasport"):
                link = article.find('a').get('href')
                response = requests.get(link, headers={'User-Agent': 'Mozilla/5.0'})
                if response.status_code == 200:
                    data = response._content
                    bs = BeautifulSoup(data, "html.parser")
                    if bs:
                        title = bs.find('h1')
                        if title:
                            title = title.text.strip()

                        subtitle = bs.find('div', {'class': 'editor_content resumen'})
                        if subtitle:
                            subtitle = subtitle.text.strip()
                        if i == 2:
                            subtitle = ""

                        date = bs.find('div', {'class': 'post-meta vcard'}).find('span', {'class': 'updated'})
                        if date:
                            date = date.text.strip()


                        categories_elements = bs.find('div', {'class': 'post-meta vcard'}).find_all('a', rel='tag')
                        categories = [cat.text for cat in categories_elements]

                        sections_body = bs.find('div', {'class': 'post-content entry-content'})
                        text = ""
                        if sections_body:
                            if i == 1:
                                for element in sections_body:
                                    if isinstance(element, Tag):
                                        if 'p' == element.name:
                                            text += element.text + '\n'
                            else:
                                for element in sections_body:
                                    if isinstance(element, Tag):
                                        if 'p' == element.name:
                                            text += element.text + '\n'

                        noticias.append({"id": index, "url": link, "title": title, "subtitle": subtitle, "date": date, "categories": categories, "content": text})

                        index += 1

            f = open(os.getcwd() + '/suasesport.json', "w+", encoding='utf-8')
            f.write(json.dumps(noticias, indent=4, ensure_ascii=False))

            return index

    noticias = []
    index = 0
    categorias = {
        1: "futbol",
        2: "f-sala",
        3: "baloncesto",
        4: "atletismo",
        5: "pilota",
        6: "acuaticos",
        7: "mas-deporte",
    }
    title = subtitle = date = text = ""
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--incognito')
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    driver = webdriver.Chrome(options=options)
    for i in range(1, 31):
        driver.get("https://suasesport.com/es/categoria/futbol/")
        bs = BeautifulSoup(driver.page_source, "html.parser")
        index = print_noticias(index, bs)
        driver.execute_script("arguments[0].scrollIntoView();", driver.find_element(By.CLASS_NAME, 'next arrow'))
        botones = driver.find_elements(By.CLASS_NAME, "next arrow")

