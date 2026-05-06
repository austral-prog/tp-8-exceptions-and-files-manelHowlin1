# Ejercicio 5 - CSV a lista de diccionarios


def csv_to_dict(filename):
    """
    Lee un archivo CSV con header "name,age,city" y retorna una lista de
    diccionarios, uno por fila.

    Reglas:
    - La primera línea es siempre el header.
    - Las claves del diccionario se toman del header.
    - El campo "age" se convierte a int. "name" y "city" quedan como str.
    - Se deben hacer strip a los valores para eliminar espacios sobrantes.
    - Si el archivo está vacío o solo tiene header, retornar [].
    - Si el archivo no existe, propagar FileNotFoundError.
    - No se permite usar el módulo csv.

    Args:
        filename: str - nombre del archivo a leer.

    Returns:
        list[dict] - lista de diccionarios por fila del CSV.

    Raises:
        FileNotFoundError: si el archivo no existe.

    Ejemplo:
        # archivo contiene:
        # name,age,city
        # Alice,30,Buenos Aires
        # Bob,25,Rosario
        csv_to_dict("people.csv") -> [
            {"name": "Alice", "age": 30, "city": "Buenos Aires"},
            {"name": "Bob", "age": 25, "city": "Rosario"},
        ]
    """
    try:
        with open(filename, mode='r') as archivo:
            lista = []
            lineas = []
            for l in archivo:
                lineas.append(l)
            if len(lineas) == 0:
                return []
            header_linea = lineas[0].strip()
            if header_linea == "":
                return []
            header = header_linea.split(",")
            for i in range(1, len(lineas)):
                fila_texto = lineas[i].strip()
                valores = fila_texto.split(",")
                registro = {}
                for j in range(len(header)):
                    clave = header[j].strip()
                    valor = valores[j].strip()
                    if clave == "age":
                        registro[clave] = int(valor)
                    else:
                        registro[clave] = valor
                lista.append(registro)
    except FileNotFoundError:
        raise
    return lista
