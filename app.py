import requests 
from bs4 import BeautifulSoup

url = 'https://es.wikipedia.org/wiki/Python' # URL de la página a scrapear

response = requests.get(url) # Realizar la petición GET

soup = BeautifulSoup(response.text, 'html.parser') # Parsear el contenido HTML

# obtener los links de la página
def obtener_links(soup):

    links = [] # lista para almacenar los links

    for link in soup.find_all('a'):
        if link.get('href') and link.get('href').startswith('https://'): # filtrar solo los links que empiezan con https://
            links.append(link) # añadir el link a la lista
    return links

# recorrer los links y obtener etiquetas h1 y p de cada uno
def obtener_datos(links):

    data = {}; # diccionario para almacenar los datos
    for link in links:
        data[link] = [] # añadir el link como clave del diccionario
        response = requests.get(link.get('href')) # realizar la petición GET
        soup = BeautifulSoup(response.text, 'html.parser') # parsear el contenido HTML
        h1 = soup.find('h1')
        p = soup.find('p')
        data[link] = [h1, p] # añadir las etiquetas h1 y p al diccionario
    return data

links = obtener_links(soup) # obtener los links de la página
data = obtener_datos(links) # obtener los datos de cada link

# guardar los datos en un archivo JSON
with open('./results/results.json', mode='w', encoding='utf-8') as file:
    file.write(str(data))