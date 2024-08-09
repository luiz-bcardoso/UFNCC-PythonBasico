# Arquivo contendo métodos uteis para serem usados em qualquer projeto
# Luiz Batista Cardoso, 08 agosto 2024.

import random

def listarLista(list):
    """Dado uma lista, printa na tela cada elemento dela.

    Parameters:
    lista (lista): Lista com elementos dentro

    Returns:
    void: Apenas printa na tela
    """
    if list:
        for element in list:
            print(f"{element}")
    else:
        print('Lista nao contem nenhum elemento.')