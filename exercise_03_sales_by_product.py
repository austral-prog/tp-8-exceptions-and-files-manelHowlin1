# Ejercicio 3 - Ventas por producto


def read_sales(filename):
    """
    Lee un archivo con ventas en formato "producto:valor;producto:valor;..."
    (todo en una sola línea, los registros separados por ';') y agrupa los
    valores en una lista por producto.

    Reglas:
    - Los valores se convierten a float.
    - El orden de los montos dentro de la lista es el mismo en que aparecen
      en el archivo.
    - Los separadores ';' finales sin contenido se ignoran (es común que
      el archivo termine con ';').
    - Si el archivo no existe, propagar FileNotFoundError.

    Args:
        filename: str - nombre del archivo a leer.

    Returns:
        dict[str, list[float]] - montos de venta agrupados por producto.

    Raises:
        FileNotFoundError: si el archivo no existe.

    Ejemplo:
        # archivo contiene: "producto1:100;producto2:200;producto1:150;"
        read_sales("ventas.txt") -> {
            "producto1": [100.0, 150.0],
            "producto2": [200.0],
        }
    """
    diccionario = {}
    try:
        with open(filename, "r") as archivo:
            for linea in archivo:
                linea = linea.strip()
                ventas_sucias = linea.split(";")
                ventas = []
                for v in ventas_sucias:
                    if v != "":
                        ventas.append(v)
                for producto in ventas:
                    nombre, valor_str = producto.split(":")
                    valor = float(valor_str)
                    print(nombre, valor)
                    if nombre not in diccionario:
                        diccionario[nombre] = [valor]
                    else:
                        diccionario[nombre].append(valor)
    except FileNotFoundError:
        raise
    return diccionario

def process_sales(data):
    """
    Para cada producto del diccionario, imprime en el orden natural del dict:

        producto: ventas totales $X.XX, promedio $Y.YY

    Los valores de total y promedio deben mostrarse siempre con DOS
    decimales.

    Args:
        data: dict[str, list[float]] - salida de read_sales.

    Returns:
        None

    Ejemplo:
        process_sales({"producto1": [100.0, 150.0]})
        # imprime: "producto1: ventas totales $250.00, promedio $125.00"
    """
    for producto, lista_precios in data.items():
        total_precios = sum(lista_precios)
        cantidad = len(lista_precios)
        if cantidad > 0:
            promedio = total_precios / cantidad
        else:
            promedio = total_precios
        print(f"{producto}: ventas totales ${total_precios:.2f}, promedio ${promedio:.2f}")


    return
