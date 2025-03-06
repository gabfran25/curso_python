'''Archivo con las funciones necesarias de la aplicación LIBRO WEB'''
import csv

def lee_archivo_csv(archivo:str)->list:
    '''Lee un archivo CSV y devuelve una lista de diccionarios'''
    with open(archivo, "r", encoding='utf8') as f:
        return [x for x in csv.DictReader(f)]
    
def crea_diccionario_titulos(lista:list)->dict:
    '''Crea un diccionario con los títulos como claves y el resto de los datos como valores'''
    return {x['title']:x for x in lista}

def busca_en_titulo(diccionario,palabra)->list:
    '''Busca una palabra en los títulos de la lista y devuelve una lista con los resultados'''
    lista = []
    for titulo, libro in diccionario.items():
        if palabra in titulo.lower():
            lista.append(libro)
    return lista

def crea_diccionario(lista:list, llave:str)->dict:
    '''Crea un diccionario con la llave indicada y el resto de los datos como valores'''
    return {x[llave]:x for x in lista}

def busca_en_diccionario(diccionario:dict, palabra:str)->list:
    '''Busca una palabra en los valores del diccionario y devuelve una lista con los resultados'''
    lista = []
    for llave, libro in diccionario.items():
        if palabra in llave.lower():
            lista.append(libro)
    return lista

def libros_empiezan_con(lista:list, letra:str)->list:
    '''Devuelve una lista con los libros que empiezan con la letra indicada'''
    lista_resultados = []
    for libro in lista:
        if libro['title'].lower().startswith(letra.lower()):
            lista_resultados.append(libro)
    return lista_resultados
    # return [x for x in lista if x['title'].lower().startswith(letra.lower())]

if __name__ == '__main__':
    archivo_csv = 'booklist2000.csv'
    lista_libros = lee_archivo_csv(archivo_csv)
    diccionario_libros = crea_diccionario(lista_libros,'title')
    resultado = busca_en_diccionario(diccionario_libros, 'rebels')
    print(resultado)
    diccionario_autores = crea_diccionario(lista_libros,'author')
    resultado = busca_en_diccionario(diccionario_autores, 'james')
    print(resultado)
    resultado = libros_empiezan_con(lista_libros, 't')
    # print(resultado)
    print(f'Libros que empiezan con "T" : {len(resultado)}')