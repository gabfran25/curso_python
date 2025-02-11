'''
Funciones auxiliares del juego ahorcado
'''

def carga_archivo_texto(archivo:str)->list:
    '''
    Carga un archivo de texto y lo devuelve como una lista de palabras
    '''
    with open(archivo, 'r', encoding='utf-8') as file:
        oraciones = file.readlines()
    return oraciones

def carga_plantilla(nombre_plantilla:str)->dict:
    '''
    Carga una plantilla de un archivo de texto y la devuelve como una lista de palabras.
    En este caso carga las plantillas del juego apartir de un archivo de texto
    '''
    plantillas = {}
    for i in range(6):
        plantillas[i] = carga_archivo_texto(f'./curso_ds4/ahorcado/plantillas/{nombre_plantilla}-{i}.txt')
    return plantillas

def despliega_plantilla(diccionario:dict, nivel:int):
    '''
    Despliega la plantilla del nivel correspondiente
    '''
    if nivel in diccionario:
        template = diccionario[nivel]
        for renglon in template:
            print(renglon)
    
def obten_palabras(lista:list)->list:
    '''
    Obtiene las palabras de un texto
    '''
    texto = ' '.join(lista[120:])
    palabras = texto.split()
    minusculas = [palabra.lower() for palabra in palabras]
    set_palabras = set(minusculas)
    return list(set_palabras)


if __name__ == '__main__':
    plantillas = carga_plantilla('plantilla')
    despliega_plantilla(plantillas, 5)
    lista_oraciones = carga_archivo_texto('./curso_ds4/ahorcado/datos/pg15532.txt')
    lista_palabras = obten_palabras(lista_oraciones)
    print(lista_palabras[:50])
