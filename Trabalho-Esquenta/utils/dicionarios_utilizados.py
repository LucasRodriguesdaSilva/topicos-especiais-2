def dicionarios_utilizados():
    dict_tipo_lista = {
        'o': 'lista_ordenada', 
        'no': 'lista_nao_ordenada'
    }

    dict_algoritmos = {
        'a': 'Busca Linear V1 O(n)',
        'b': 'Busca Linear V2 O(n)',
        'c': 'Busca Binária O(log n)',
        'd': 'Busca Quadrática O(n^2)',
        'e': 'Busca Ternária O(log n)',
        'f': 'Busca Cúbica - Tripla Checagem O(n^3)'
    }
    
    dict_instancias = {
        1: '100', 
        2: '200', 
        3: '1000', 
        4: '2000', 
        5: '5000', 
        6: '10000', 
        7: '50000', 
        8: '100000', 
        9: '500000', 
        10: '1000000', 
        11: '5000000', 
        12: '10000000', 
        13: '100000000'
    }

    dicionarios = {
        't': dict_tipo_lista,
        'a': dict_algoritmos,
        'i': dict_instancias
    }

    return dicionarios