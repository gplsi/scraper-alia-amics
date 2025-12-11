import requests
from bs4 import BeautifulSoup, Tag
import os
import json

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException

import time

if __name__ == '__main__':
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Eliminamos la interfaz
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("window-size=1920,1080")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)

    # Añadir path de chromedirver a la configuracion
    # homedir = os.path.expanduser("~")
    webdriver_service = Service()

    # Eleccion de chrome como buscador
    browser = webdriver.Chrome(service=webdriver_service, options=chrome_options)
    browser.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    browser.delete_all_cookies()
    browser.implicitly_wait(10)

    noticias = []
    index = 0
    title = subtitle = date = text = ""
    for i in range(1, 6):
        if i == 1:
            browser.get("https://www.diarilaveu.cat/cultura")
        elif i == 2:
            browser.get("https://www.diarilaveu.cat/esports")
        elif i == 3:
            browser.get("https://www.diarilaveu.cat/opinio")
        elif i == 4:
            browser.get("https://www.diarilaveu.cat/politica")
        else:
            browser.get("https://www.diarilaveu.cat/sociedad")
        select = browser.find_element(By.ID, 'load_more_button')
        select.click()

        mas_noticias = True
        while mas_noticias:
            try:
                print("Searching more news...")
                time.sleep(1)
                browser.execute_script("arguments[0].scrollIntoView();", browser.find_element(By.ID, 'load_more_button'))
                button = browser.find_element(By.ID, 'load_more_button')
                button.click()

            except:
                more_comments = False

        bs = BeautifulSoup(browser.page_source, "html.parser")
        if bs:
            articles = bs.find_all('div', {'class': 'regular-article-block regular-article-block-27 homepage-block   '})
            print("Hay " + str(len(articles)) + " noticias")
            for article in articles:
                link = article.find('a').get('href')
                response = requests.get(link,  headers={'User-Agent': 'Mozilla/5.0'})
                if response.status_code == 200:
                    data = response._content
                    bs = BeautifulSoup(data, "html.parser")
                    if bs:
                        title = bs.find('div', {'class': 'content_title'})
                        if title:
                            title = title.text.strip()

                        subtitle = bs.find('div', {'class': 'content_subtitle'})
                        if subtitle:
                            subtitle = subtitle.text.strip()
                        else:
                            subtitle = ""

                        date = bs.find('span', {'class': 'post-date'})
                        if date:
                            date = date.text.strip()

                        sections_body = bs.find('div', {'class': 'content_text'})
                        text = ""
                        if sections_body:
                            for element in sections_body:
                                if isinstance(element, Tag):
                                    if 'p' == element.name:
                                        text += element.text + '\n'
                                    elif 'h2' == element.name:
                                        text += element.text + '\n'

                        noticias.append({"id": index, "url": link, "title": title, "subtitle": subtitle, "date": date, "content": text})

                        index += 1

            f = open(os.getcwd() + '/diarilaveu.json', "w+", encoding='utf-8')
            f.write(json.dumps(noticias, indent=4, ensure_ascii=False))
            print("NOTICIAS DESCARGADAS: " + str(index))

