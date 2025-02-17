'''
Programa principal del juego del ahorcado
'''

import string
import unicodedata
from random import choice
import funciones as fn 

def main(archivo_texto:str, nombre_plantilla='plantilla'):
    '''
    Programa principal del juego del ahorcado
    '''
    # Cargamos las plantillas
    plantillas = fn.carga_plantilla(nombre_plantilla)
    # Cargamos las oraciones
    oraciones = fn.carga_archivo_texto(archivo_texto)
    # Obtenemos las palabras
    palabras = fn.obten_palabras(oraciones)
    o = 5 # 5 oportunidades de fallar
    p = choice(palabras) # elegimos una palabra al azar
    abecedario = {letra:letra for letra in string.ascii_lowercase}
    letras_adivinadas = set()
    while o > 0:
        fn.despliega_plantilla(plantillas, o)
        fn.adivina_letra(abecedario, p, letras_adivinadas, o)
        if p == ''.join([letra if letra in letras_adivinadas else '_' for letra in p]):
            print(f'¡Felicidades! La palabra es {p}')
            break
    print(f'La palabra era {p}')
        
    
if __name__ == '__main__':
    archivo = './curso_ds4/ahorcado/datos/pg15532.txt'
    main(archivo)
    