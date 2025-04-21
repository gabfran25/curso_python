'''
Scrapper para wikipedia
'''
import os
import argparse
import requests
from bs4 import BeautifulSoup
 
def scrap(url:str):
    ''' Obtiene página desde Internet'''
    pagina = requests.get(url,timeout=10)
    if pagina.status_code != 200:
        raise Exception(f'Error {pagina.status_code} en la página {url}')
    return pagina

def guardar_pagina(pagina, nombre_archivo:str):
    ''' Guarda la página en un archivo '''
    with open(nombre_archivo, 'wb') as f:
        f.write(pagina.content)
    print(f'Página guardada en {nombre_archivo}')

def main(url:str, archivo_salida:str):
    ''' Función principal '''
    if not os.path.exists(archivo_salida):
        pagina = scrap(url)
        guardar_pagina(pagina, archivo_salida)
        pagina = pagina.content
        pagina= str(pagina, 'utf-8')
    else:
        print(f'El archivo {archivo_salida} ya existe. Leyendo de él.')
        with open(archivo_salida, 'rb') as f:
            pagina = f.read()
        pagina= str(pagina, 'utf-8')
    soup = BeautifulSoup(pagina,"html.parser")
    #main_content = soup.find('div', class_='mw-body-content')
    # main_content = soup.find('div', id='mw-pages')
    main_content = soup.find('table', id='dllsTable')
    if main_content:
        trs = main_content.find_all('tr')
        diccionario_trs = {}
        print(f"Encontré {len(trs)} elementos <tr> en la tabla")
        for tr in trs:
            #print(f"{li.a.get('href')} : {li.a.text.strip()}")
            print("-------------")
            tds = tr.find_all('td')
            if len(tds) == 4:
                print(f"0: {tds[0].text.strip()}")
                print(f"1: {tds[1].text.strip()}")
                print(f"2: {tds[2].text.strip()}")
                print(f"3: {tds[3].text.strip()}")
            elif len(tds) == 5:
                print(f"0: {tds[0].text.strip()}")
                print(f"1: {tds[1].text.strip()}")
                print(f"2: {tds[2].text.strip()}")
                print(f"3: {tds[3].text.strip()}")
                print(f"4: {tds[4].text.strip()}")
            if tr.a is not None:
                diccionario_trs[tr.a.text.strip(tds[0])] = tr.a.get(tds[3])
                lista = [{'pelicula':k,'registro':{'compra' : v, 'venta': v}} for k,v in diccionario_trs.items()]
                print(lista)
      
    '''  # lis = main_content.find_all('table id')
        lis = main_content.find_all('tr')
        diccionario_lis = {}
        # print(f"Encontré {len(lis)} elementos <li> en la página")
        print (f"Encontré {len(lis)} elementos <tr> en la página")
        for li in lis:
            #print(f"{li.a.get('href')} : {li.a.text.strip()}")
            if li.a is not None:
                diccionario_lis[li.a.text.strip()] = li.a.get('td.xTimes')
        # lista = [{'pelicula':k,'link:':v} for k,v in diccionario_lis.items()]
        lista = [{'banco':k, 'registro':{'compra' : v, 'venta': v}} for k,v in diccionario_lis.items()]
        print(lista)
        
    archivo_salida = archivo_salida.replace('.html', '.json')
    with open(archivo_salida, 'w', encoding='utf8') as f:
        f.write(str(lista))'''
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Scrapper para dólar')
    parser.add_argument('--url', type=str, help='URL de la página del dólar')
    parser.add_argument('--output', type=str, default='eldolar.html')
    parser.add_argument('--output_json', type=str, default='eldolar.json')
    args = parser.parse_args()
    url = args.url
    output = args.output
    if not url:
        #url = "https://es.wikipedia.org/wiki/Anexo:Pel%C3%ADculas_de_ciencia_ficci%C3%B3n"
        url = "https://www.eldolar.info/es-MX/mexico/dia/hoy"
    if not output:
        output = 'precio_dolar.html'
    main(url, output)