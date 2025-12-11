import requests
from bs4 import BeautifulSoup, Tag
import os
import json
from tqdm import tqdm

if __name__ == '__main__':

    def print_noticias(index, response):
        #for categoria in categorias:
            # Ajustamos la url dependiendo de si es portada u otra categoria ya que portada tiene una url diferente
            #if categoria == "":
                #url_categoria = "https://cronica.es/"
                #categoria_nombre = "portada"  # Para usar en la descripción del tqdm
            #else:
                #url_categoria = f"https://cronica.es/sec/{categoria}"
                #categoria_nombre = categoria

        if response.status_code == 200:
            data = response.content
            bs = BeautifulSoup(data, "html.parser")

            articles = bs.find_all('div', class_=["NEWSITEMROWS", "NEWSITEMCOLUMNS", "mainnew", "newssection"])

            for article in tqdm(articles, desc=f"Extrayendo de cronica.es"):
                link_element = article.find('a')
                if link_element and link_element.has_attr('href'):
                    partial_link = link_element['href']
                    if not partial_link.startswith('http'):
                        full_link = f"https://cronica.es/{partial_link}" if not partial_link.startswith('/') else f"https://cronica.es{partial_link}"
                    else:
                        full_link = partial_link

                    article_response = requests.get(full_link, headers={'User-Agent': 'Mozilla/5.0'})
                    if article_response.status_code == 200:
                        article_data = article_response.content
                        article_bs = BeautifulSoup(article_data, "html.parser")

                        # Obtenemos el titulo, subtitulo y fecha, autor y el contenido de la noticia
                        title = article_bs.find('h1', class_="new_title").text.strip() if article_bs.find('h1', class_="new_title") else ""
                        subtitle = article_bs.find('h2', class_="new_subtitle").text.strip() if article_bs.find('h2', class_="new_subtitle") else ""
                        date = article_bs.find('span', class_="date").text.strip() if article_bs.find('span', class_="date") else ""
                        #author= article_bs.find('span', class_="signature").text.strip()


                        content_paragraphs = article_bs.find('div', class_="new_text").find_all('p') if article_bs.find('div', class_="new_text") else []
                        text = ' '.join(paragraph.get_text(strip=True) for paragraph in content_paragraphs)

                        noticias.append({
                            "id": index,
                            "url": full_link,
                            "title": title,
                            "subtitle": subtitle,
                            "date": date,
                            "content": text
                        })

                        index += 1

            # Guardar los resultados en un archivo JSON
            f = open(os.getcwd() + '/cronica.json', "w+", encoding='utf-8')
            f.write(json.dumps(noticias, indent=4, ensure_ascii=False))

            return index

    noticias = []
    index = 0
    headers = {'User-Agent': 'Mozilla/5.0'}
    categorias = [
    "",
    "internacional",
    "nacional",
    "regional",
    "provincial",
    "comarcal",
    "local",
    "temes"
    ]

    page = 0
    for i in range(1, 5):
        response = requests.get("https://cronica.es/sec/internacional/"+str(page), headers={'User-Agent': 'Mozilla/5.0'})
        page = page + 20
        index = print_noticias(index, response)
    page = 0
    for i in range(1, 9):
        response = requests.get("https://cronica.es/sec/nacional/"+str(page), headers={'User-Agent': 'Mozilla/5.0'})
        page = page + 20
        index = print_noticias(index, response)
    page = 0
    for i in range(1, 16):
        response = requests.get("https://cronica.es/sec/regional/"+str(page), headers={'User-Agent': 'Mozilla/5.0'})
        page = page + 20
        index = print_noticias(index, response)
    page = 0
    for i in range(1, 13):
        response = requests.get("https://cronica.es/sec/provincial/" + str(page), headers={'User-Agent': 'Mozilla/5.0'})
        page = page + 20
        index = print_noticias(index, response)
    page = 0
    for i in range(1, 16):
        response = requests.get("https://cronica.es/sec/comarcal/" + str(page), headers={'User-Agent': 'Mozilla/5.0'})
        page = page + 20
        index = print_noticias(index, response)
    page = 0
    for i in range(1, 77):
        response = requests.get("https://cronica.es/sec/local/" + str(page), headers={'User-Agent': 'Mozilla/5.0'})
        page = page + 20
        index = print_noticias(index, response)
