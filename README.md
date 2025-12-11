# 📄 Web Scraper para Portales de Noticias AMICS

Este repositorio incluye varios scripts de portales de noticias de [AMICS](https://www.amic.media/mitjans_digitals.php?sel_provincia=9&sel_comarca=0&txt_search=) diseñado para extraer información estructurada desde sitios web de noticias o blogs.  


## 🧠 Objetivo de los scripts

El script realiza automáticamente:

- Descarga de páginas de listado de artículos.
- Extracción de enlaces individuales a noticias.
- Scraping de cada noticia para obtener:
  - **Título**
  - **Subtítulo** (si existe)
  - **Fecha de publicación**
  - **Contenido textual** (párrafos)
- Normalización del contenido en un diccionario homogéneo.
- Almacenamiento final en un archivo JSON estructurado.

Este diseño permite usar el mismo esqueleto para varios medios simplemente modificando los selectores HTML.


## 🔧 Tecnologías Utilizadas

El script usa exclusivamente librerías ligeras y ampliamente compatibles:

| Librería | Uso |
|---------|------|
| `requests` | Realiza las peticiones HTTP |
| `BeautifulSoup4` | Parseo y navegación del HTML |
| `Tag` (bs4) | Validación de nodos HTML |
| `json` | Serialización del dataset |
| `os` | Gestión de rutas y archivos |

Instalación mínima:

```
pip install requests beautifulsoup4
``` 

## ⚙️ Funcionamiento General

### 1️⃣ Descarga del listado de artículos

Se accede a una o varias páginas de listado que contienen enlaces a artículos.

### 2️⃣ Extracción de enlaces

Se obtiene la URL de cada noticia mediante selectores configurables.

### 3️⃣ Scraping de cada noticia

Se extraen:

- Título

- Subtítulo (si existe)

- Fecha

- Contenido consolidado

### 4️⃣ Normalización

Cada noticia procesada se almacena como:

```
{
    "id": 0,
    "url": "...",
    "title": "...",
    "subtitle": "...",
    "date": "...",
    "content": "..."
}
```


### 5️⃣ Exportación a JSON

El script genera un archivo estructurado en la raíz del proyecto, p. ej.:

```
7diesactualitat.json
```

## 📁 Ejemplo de JSON

```
[
  {
    "id": 0,
    "url": "https://medio.com/noticia1",
    "title": "Ejemplo de noticia",
    "subtitle": "Subtítulo opcional",
    "date": "2025-01-15",
    "content": "Contenido completo del artículo..."
  }
]
```

## 💰 Financiación

Este recurso está financiado por el Ministerio para la Transformación Digital y de la Función Pública — Financiado por la UE – NextGenerationEU, en el marco del proyecto Desarrollo de Modelos ALIA.

## 🙏 Agradecimientos

Expresamos nuestro agradecimiento a todas las personas e instituciones que han contribuido al desarrollo de este recurso.

Agradecimientos especiales a:

[Proveedores de datos]

[Proveedores de soporte tecnológico]

Asimismo, reconocemos las contribuciones financieras, científicas y técnicas del Ministerio para la Transformación Digital y de la Función Pública – Financiado por la UE – NextGenerationEU dentro del marco del proyecto Desarrollo de Modelos ALIA.

## 📚 Referencia

Por favor, cita este conjunto de datos usando la siguiente entrada BibTeX:

```
@misc{scraper_alia_amics_2025,
  author       = {Espinosa Zaragoza, Sergio and Sep{\'u}lveda Torres, Robiert and Mu{\~n}oz Guillena, Rafael and Consuegra-Ayala, Juan Pablo},
  title        = {ALIA_AMICS Scraper}, 
  year         = {2025},
  institution  = {Language and Information Systems Group (GPLSI) and Centro de Inteligencia Digital (CENID), University of Alicante (UA)},
  howpublished = {\url{https://github.com/gplsi/scraper-alia-amics}}
}
```

## ⚠️ Aviso Legal

Este recurso puede contener sesgos o artefactos no intencionados.
Cualquier tercero que utilice o implemente sistemas basados en este recurso es el único responsable de garantizar un uso conforme, seguro y ético, incluyendo el cumplimiento de las normativas relevantes en materia de IA y protección de datos.

La Universidad de Alicante, como creadora y propietaria del recurso, no asume ninguna responsabilidad por los resultados derivados del uso por parte de terceros.

## 📜 Licencia

Licencia Apache, Versión 2.0

