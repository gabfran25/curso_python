'''
Prueba de BeautifulSoup para extraer información de una página web.
'''

from bs4 import BeautifulSoup

html = "<html><body><h1>Titulo</h1><p>Texto</p></body></html>"
soup = BeautifulSoup(html, 'html.parser')
print(soup.prettify()) # Imprime el HTML formateado
print(soup.h1.text) # Imprime el texto dentro de la etiqueta h1
soup.p.string = "Hola Mundo" # Cambia el texto dentro de la etiqueta p
soup.h1.string = "Hola Mundo de Beautiful Soup" # Cambia el texto dentro de la etiqueta h1
nueva_etiqueta = soup.new_tag("p") # Crea una nueva etiqueta p
nueva_etiqueta.string = "Soy una nueva etiqueta"
soup.body.append(nueva_etiqueta) # Agrega la nueva etiqueta al body
nueva_liga = soup.new_tag("a", href="http://google.com")
nueva_liga.string = "Google"
soup.body.append(nueva_liga) # Agrega la nueva etiqueta al body
print(soup.prettify()) # Imprime el HTML formateado
print("......................................")
print(soup.find("h1")) # Encuentra la primera etiqueta h1
print(soup.find_all("p")) # Encuentra todas las etiquetas p
parrafos = soup.find_all("p") # Encuentra todas las etiquetas p
lista_parrafos = []
for p in parrafos:
    lista_parrafos.append(p.string) # Agrega el texto de cada etiqueta p a la lista
print(lista_parrafos) # Imprime la lista de textos de los párrafos
# print(soup.prettify()) # Imprime el HTML formateado
