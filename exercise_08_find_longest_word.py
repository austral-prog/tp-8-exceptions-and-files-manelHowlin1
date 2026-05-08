# Ejercicio 8 - Palabra más larga de un archivo


def find_longest_word(filename):
    """
    Lee el archivo, lo divide en palabras (separadas por cualquier tipo
    de whitespace) y retorna la palabra más larga.

    Reglas:
    - Si hay varias palabras con la misma longitud máxima, retornar la
      PRIMERA en aparecer.
    - Si el archivo no existe, propagar FileNotFoundError.
    - Si el archivo no tiene ninguna palabra (está vacío o solo tiene
      espacios/saltos de línea), lanzar ValueError("file has no words").

    Args:
        filename: str - nombre del archivo a leer.

    Returns:
        str - la palabra más larga del archivo.

    Raises:
        FileNotFoundError: si el archivo no existe.
        ValueError: si el archivo no tiene palabras.

    Ejemplo:
        # archivo contiene: "el gato corre rapido\npor el jardin\n"
        find_longest_word("texto.txt") -> "rapido"
    """
    try:
        with open(filename, "r") as archivo:
            palabra_mas_larga = ""
            palabra_larga = ""
            palabras_largas_fila = []
            encontre_palabras = False
            for linea in archivo:
                lista_palabras = (linea.strip()).split()
                for p in lista_palabras:
                    encontre_palabras = True
                    if len(p) > len(palabra_larga):
                        palabra_larga = p
                palabras_largas_fila.append(palabra_larga)
            for i in range(len(palabras_largas_fila)):
                if len(palabras_largas_fila[i]) > len(palabra_mas_larga):
                    palabra_mas_larga = palabras_largas_fila[i]
            if not encontre_palabras:
                raise ValueError("archivo no existe")

            return palabra_mas_larga
        
    except FileNotFoundError:
        raise
