def imprimir_arvore(nodo, nivel = 0):

    """
    Imprime recursivamente uma árvore de nós (paciente, impacto ou plano PDCA)
    de forma hierárquica, indentando os filhos de acordo com o nível.

    Parâmetros:
        nodo (Nodo): nó raiz da árvore ou sub-árvore a ser impressa
        nivel (int, opcional): nível de indentação (0 para raiz, incrementa nos filhos)

    Exemplo:
        - paciente: Felipe
            - impacto: Uso de reagente X (Contaminação química) - prioridade 1
                - plano: Coleta segura de resíduos químicos
    """

    # Imprime o nó atual com indentação proporcional ao nível.
    print(" "* nivel + f"-{nodo.tipo}: {nodo.valor}")
    for filho in nodo.filhos: # Percorre todos os filhos do nó e chama recursivamente a função.
        imprimir_arvore(filho, nivel + 1)