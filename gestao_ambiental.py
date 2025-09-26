from nodo import Nodo

#Ambos os nós podem ser adicionados à árvore do paciente, permitindo rastrear impactos e soluções de forma estruturada.


#Cria um nó de impacto ambiental (aspecto + impacto + prioridade)
def registrar_aspecto():
    etapa = input("Etapa - clinica ou fabril: ")
    descricao = input("Descrição da ação: ")
    impacto = input("Impacto ambiental: ")
    
    nodo_impacto = Nodo(valor=f"{descricao} ({impacto})", tipo="impacto")
    print(f"Impacto registrado: {descricao}")
    return nodo_impacto

#Criar_plano(nodo_impacto) → cria um plano de mitigação e adiciona como filho do impacto
def criar_plano(nodo_impacto):
    plano = input(f"Crie um plano de mitigação para '{nodo_impacto.valor}': ")
    nodo_plano = Nodo(valor=plano, tipo="plano")
    nodo_impacto.adicionar_filho(nodo_plano)
    print(f"Plano criado e ligado ao impacto'{nodo_impacto.valor}")
