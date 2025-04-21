import csv
import sys

def buscar_frases_por_palabras(archivo_csv, palabras_busqueda):
    resultados = []
    try:
        with open(archivo_csv, mode='r', encoding='utf-8') as archivo:
            lector_csv = csv.reader(archivo)
            encabezado = next(lector_csv)  # Leer encabezado
            for fila in lector_csv:
                frase = fila[0]  # Suponiendo que la frase está en la primera columna
                if all(palabra.lower() in frase.lower() for palabra in palabras_busqueda):
                    resultados.append(frase)
    except FileNotFoundError:
        print(f"Error: El archivo '{archivo_csv}' no existe.")
    except Exception as e:
        print(f"Error: {e}")
    return resultados

if __name__ == "__main__":
    archivo_csv = 'frases_celebres.csv'
    palabras_busqueda = sys.argv[1:]  # Leer palabras de búsqueda desde los argumentos
    if not palabras_busqueda:
        print("Por favor, ingrese al menos una palabra para buscar.")
        sys.exit(1)

    resultados = buscar_frases_por_palabras(archivo_csv, palabras_busqueda)
    if resultados:
        print("Frases encontradas:")
        for frase in resultados:
            print(f"- {frase}")
    else:
        print("No se encontraron frases que coincidan con la búsqueda.")