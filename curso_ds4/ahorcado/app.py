'''
Programa principal del juego del ahorcado
'''
import os
import string
import unicodedata
import argparse
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
            o = fn.adivina_letra(abecedario, p, letras_adivinadas, o)
            if p == ''.join([letra if letra in letras_adivinadas else '_' for letra in p]):
                print(f'¡Felicidades! La palabra es {p}')
                break
        fn.despliega_plantilla(plantillas, o)
        print(f'La palabra era {p}')
        
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Juego del ahorcado')
    parser.add_argument('-a', '--archivo', help='Archivo de texto con palabras a adibinar', default = './curso_ds4/ahorcado/datos/la_odisea.txt')
    args = parser.parse_args()
    archivo = args.archivo
    if os.stat(archivo) is False:
        print(f'El archivo {archivo} no existe o está vacío')
    else:
        main(archivo)
    
    