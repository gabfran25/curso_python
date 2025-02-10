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

if __name__ == '__main__':
    lista = carga_archivo_texto('curso_ds4\ahorcado\plantillas\plantilla-0.txt')
    for elemento in lista:
        print(elemento)
    