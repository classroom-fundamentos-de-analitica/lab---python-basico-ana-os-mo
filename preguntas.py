"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""

def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    with open('data.csv', mode='r') as datos:
        datos = datos.readlines()

    return sum([int(var.strip().split('\t')[1]) for var in datos])


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    with open('data.csv', mode='r') as datos:
        datos = datos.readlines()
    
    datos = list([(var.strip().split('\t')[0]) for var in datos])
    col1 = list(dict.fromkeys(datos))
    col1.sort()
    res = list()
    [res.append((x, datos.count(x))) for x in col1]
    return res


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    with open('data.csv', mode='r') as datos:
        datos = datos.readlines()
    
    datos = [(var.strip().split('\t')[0:2]) for var in datos]
    col1 = sorted((list(set([var[0] for var in datos]))))
    res = list()

    for letra in col1:
        sum = 0
        for camp in datos:
            if camp[0] == letra:
                sum += int(camp[1])
        res.append((letra, sum))
    return res


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    with open('data.csv', mode='r') as datos:
        datos = datos.readlines()

    datos = list([(var.strip().split('\t')[2][5:7]) for var in datos])
    col1 = list(dict.fromkeys(datos))
    col1.sort()
    res = list()
    [res.append((x, datos.count(x))) for x in col1]
    return res


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    with open('data.csv', mode='r') as datos:
        datos = datos.readlines()

    datos = [(var.strip().split('\t')[0:2]) for var in datos]
    col1 = sorted((list(set([var[0] for var in datos]))))
    res = list()

    for letra in col1:
        nums = list()
        for camp in datos:
            if camp[0] == letra:
                nums.append(int(camp[1]))
        res.append((letra, max(nums), min(nums)))

    return res


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    with open('data.csv', mode='r') as datos:
        datos = datos.readlines()

    datos = [(var.strip().split('\t')[4]) for var in datos]
    datos = ','.join(datos).split(',')
    datos = [var.split(':') for var in datos]
    keys = sorted((list(set([var[0] for var in datos]))))
    res = list()

    for key in keys:
        values = list()
        for camp in datos:
            if camp[0] == key:
                values.append(int(camp[1]))
        res.append((key, min(values), max(values)))
        
    return res


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    with open('data.csv', mode='r') as datos:
            datos = datos.readlines()

    datos = [(var.strip().split('\t')[0:2]) for var in datos]
    col2 = sorted(list(set([int(var[1]) for var in datos])))
    res = list()

    for num in col2:
        letras = list()
        for camp in datos:
            if int(camp[1]) == num:
                letras.append(camp[0])
        res.append((int(num), letras))
        
    return res


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    with open('data.csv', mode='r') as datos:
            datos = datos.readlines()

    datos = [(var.strip().split('\t')[0:2]) for var in datos]
    col2 = sorted(list(set([int(var[1]) for var in datos])))
    res = list()

    for num in col2:
        letras_uniq = list()
        for camp in datos:
            if int(camp[1]) == num:
                letras_uniq.append(camp[0])
        res.append((int(num), sorted(list(set(letras_uniq)))))

    return res


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    with open('data.csv', mode='r') as datos:
        datos = datos.readlines()

    datos = [(var.strip().split('\t')[4]) for var in datos]
    datos = ','.join(datos).split(',')
    datos = [var.split(':')[0] for var in datos]
    keys = sorted(list(set(datos)))
    res = dict()

    for key in keys:
        res[key] = datos.count(key)

    return res


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    with open('data.csv', mode='r') as datos:
        datos = datos.readlines()

    datos = [var.strip().split('\t') for var in datos]
    for elem in datos:
        del elem[1]
        del elem[1]
        elem[1] = len(elem[1].split(','))
        elem[2] = len(elem[2].split(','))
    res = [tuple(var) for var in datos]

    return res


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    with open('data.csv', mode='r') as datos:
        datos = datos.readlines()

    original = datos.copy()
    original = [var.strip().split('\t') for var in original]
    datos = [var.strip().split('\t')[3] for var in datos]
    datos = ','.join(datos).split(',')
    col4 = sorted(list(set(datos)))
    res = dict()

    for letra in col4:
        sum = 0
        for camp in original:
            if letra in camp[3]:
                sum += int(camp[1])
        res[letra] = sum
        
    return res


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    with open('data.csv', mode='r') as datos:
        datos = datos.readlines()

    datos = [var.strip().split('\t') for var in datos]

    res = {}

    for dato in datos:
        arr = []
        letra = dato[0]

        for sub in dato[4].split(','):

            if ':' in sub:
                arr.append(map(str.strip, sub.split(':', 1)))
        arr = dict(arr)
        arr = dict([x, int(y)] for x, y in arr.items())
        suma = sum(arr.values())
        if letra in res:
            res[letra] += suma
        else:
            res[letra] = suma

    res = dict(sorted(res.items()))
    return res
