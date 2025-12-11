import requests
from bs4 import BeautifulSoup, Tag
import os
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

if __name__ == '__main__':

    def print_noticias(index, driver):
        data = driver.page_source
        bs = BeautifulSoup(data, "html.parser")
        if bs:
            page = bs.find('li', {'class': 'last'}).text.strip()
            for i in range(1, int(page)):
                if i != 1:
                    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                    driver.find_element(By.CLASS_NAME, 'next arrow').click()
                    time.sleep(0.5)
                    data = driver.page_source
                    bs = BeautifulSoup(data, "html.parser")
                articles = bs.find('div', {'class': 'paginated_content'}).find_all('article')
                for article in articles:
                    link = article.find('a').get('href')
                    response = requests.get(link, headers={'User-Agent': 'Mozilla/5.0'})
                    if response.status_code == 200:
                        data = response._content
                        bs = BeautifulSoup(data, "html.parser")
                        if bs:
                            title = bs.find('h1', {'class': 'entry-title'})
                            if title:
                                title = title.text.strip()

                            #subtitle = bs.find('p', {'class': 'col s12 post-subtitle'})
                            #if subtitle:
                            #    subtitle = subtitle.text.strip()
                            #else:
                                subtitle = ""

                            date = bs.find('span', {'class': 'updated'})
                            if date:
                                date = date.text.strip()

                            sections_body = bs.find('div', {'class': 'post-content entry-content'})
                            text = ""
                            if sections_body:
                                for element in sections_body:
                                    if isinstance(element, Tag):
                                        if 'p' == element.name:
                                            text += element.text + '\n'

                            noticias_val.append({"id": index, "url": link, "title": title, "subtitle": subtitle, "date": date, "content": text})

                            index += 1

                f = open(os.getcwd() + '/ahoramarinabaixa.json', "w+", encoding='utf-8')
                f.write(json.dumps(noticias_val, indent=4, ensure_ascii=False))
                print("PÁGINA NÚMERO: " + str(index) + " DESCARGADA")

            return index

    index = 0
    title = subtitle = date = text = ""
    noticias_val = []
    noticias_es = []
    page = 0
    for i in range(1, 6):
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--incognito')
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        driver = webdriver.Chrome(options=options)
        if i == 1:
            driver.get('https://ahoramarinabaixa.es/category/altea/')
        if i == 2:
            driver.get('https://ahoramarinabaixa.es/category/benidorm/')
        if i == 3:
            driver.get('https://ahoramarinabaixa.es/category/lalfas-del-pi/')
        if i == 4:
            driver.get('https://ahoramarinabaixa.es/category/la-nucia/')
        if i == 5:
            driver.get('https://ahoramarinabaixa.es/category/la-vila-joiosa/')
        index = print_noticias(index, driver)

