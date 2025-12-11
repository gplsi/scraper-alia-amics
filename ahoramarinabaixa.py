import requests
from bs4 import BeautifulSoup, Tag
import os
import json
import time
from requests_html import HTMLSession

if __name__ == '__main__':

    def print_noticias(index, response):
        if response.status_code == 200:
            data = response._content
            bs = BeautifulSoup(data, "html.parser")
            if bs:
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
    for page in range(1, 31):
        HEADERS = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}
        response = requests.post('https://ahoramarinabaixa.es/wp-admin/admin-ajax.php', data={
            "action": "extra_blog_feed_content",
            "et_load_builder_modules": 1,
            "blog_feed_nonce": "4b87660141",
            "to_page": page,
            "post_per_page": 12,
            "order": "desc",
            "orderby": "date",
            "categories": 22,
            "show_featured_image": 1,
            "blog_feed_module_type": "masonry",
            "et_column_type": "",
            "show_autor": 1,
            "show_categories": 1,
            "show_date": 1,
            "show_rating": 1,
            "show_more": 1,
            "show_comments": 1,
            "date_format": "M j, Y",
            "content_length": "excerpt",
            "hover_overlay_icon": "",
            "use_tax_query": 1,
            "tax_query[0][taxonomy]": "category",
            "tax_query[0][terms][]": "altea",
            "tax_query[0][field]": "slug",
            "tax_query[0][operator]": "IN",
            "tax_query[0][include_children]": "true"
        }, headers=HEADERS)
        index = print_noticias(index, response)

