import networkx as nx
from usuarios import login, cadastro, usuarios
from BancoDeDados import BancoDeDados
from gestao_ambiental import registrar_aspecto, criar_plano
from produção import Producao 


grafo = nx.DiGraph()  # Armazena conexões


def adicionar_no_grafo(usuario):
    """
    Adiciona um nó (usuário) ao grafo.
    Complexidade:
        - Inserção de nó em grafo: O(1)
    """
    grafo.add_node(usuario["nome"], tipo=usuario["tipo"])
    print(f"Nó adicionado no grafo: {usuario['nome']} ({usuario['tipo']})")


def adicionar_relacao(origem, destino, relacao):
    """
    Adiciona uma aresta (relação) entre dois usuários no grafo.
    Complexidade:
        - Inserção de aresta em grafo: O(1)
    """
    grafo.add_edge(origem, destino, relacao=relacao)
    print(f"Relação adicionada: {origem} -> {destino} ({relacao})")


def listar_pacientes_medico(nome_medico):
    """
    Lista os pacientes atendidos por um médico.
    Complexidade:
        - Busca de vizinhos em grafo: O(grau_saida(médico)) 
          (no pior caso O(n), onde n é o número de nós).
    """
    if nome_medico in grafo:
        pacientes = [
            dest for dest in grafo.successors(nome_medico)
            if grafo[nome_medico][dest]["relacao"] == "atende"
        ]
        print(f"Pacientes atendidos por {nome_medico}: {pacientes}")
    else:
        print("Médico não encontrado no grafo.")


def inicio():
    """
    Gerencia o login ou cadastro do usuário.
    Complexidade:
        - Login: O(1) médio (acesso direto em lista/array pequena de usuários).
        - Cadastro: O(1) para adicionar novo usuário.
    """
    usuario = None
    print("\nPossui login?\n1 - Sim\n2 - Ainda não\n")
    interacao = input("resposta: ")

    if interacao == "1":
        while not usuario:
            usuario = login()  # tenta logar até dar certo
    else:
        cadastro()
        usuario = login()
    
    return usuario

producao = Producao()
def menu(usuario):
    """
        - controle: O(1) por iteração.
        - busca de pacientes: O(n), onde n = número de pacientes.
        - fila (atendimento): O(log n), pois usa fila de prioridade.
    """
    while True:
        print("\n=== MENU ===")

        if usuario["tipo"] == "medico":
            print("1 - Cadastrar paciente")
            print("2 - Consultar paciente")
            print("3 - Atender paciente e registrar impacto")

        elif usuario["tipo"] == "admin":
            print("1 - Cadastrar usuário")
            print("2 - Consultar paciente")

        print("9 - Trocar de usuário")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "0":
            print("Saindo do sistema.")
            break

        elif opcao == "9":
            print("Voltando para a tela inicial...")
            usuario = inicio()  # chama a função de login/cadastro de novo
            continue

        # ----------------- ADMIN -----------------
        if usuario["tipo"] == "admin":
            if opcao == "1":
                nome = input("Nome do novo usuário: ")
                senha = input("Senha: ")
                tipo = input("Tipo (admin/medico/paciente): ").lower()
                if tipo not in ["admin", "medico", "paciente"]:
                    print("Tipo inválido!")
                else:
                    usuarios.append({"nome": nome, "senha": senha, "tipo": tipo})
                    adicionar_no_grafo({"nome": nome, "tipo": tipo})
                    print(f"Usuário {nome} ({tipo}) cadastrado!")
            elif opcao == "2":
                nome = input("Digite o nome do paciente: ")
                for p in BancoDeDados.pacientes:  # O(n)
                    if p.nome == nome:
                        p.consultar_paciente()
                        break
                else:
                    print("Paciente não encontrado!")
            
            elif opcao == "3":
                print("Coleta de colaboradores para predição de falha")
                qtd_pacientes = len(BancoDeDados.pacientes)
                materia = producao.calcular_materia_prima(qtd_pacientes)
                risco, ocorreu = producao.falhaAmbiental(qtd_pacientes)    

        # ----------------- MÉDICO -----------------
        elif usuario["tipo"] == "medico":
            if opcao == "1":
                nome = input("Nome do paciente: ")
                idade = int(input("Idade: "))
                paciente = BancoDeDados(nome, idade)
                paciente.cadastrar()
                adicionar_no_grafo({"nome": nome, "tipo": "paciente"})
                adicionar_relacao(usuario["nome"], nome, "atende")
            elif opcao == "2":
                nome = input("Digite o nome do paciente: ")
                for p in BancoDeDados.pacientes:  # O(n)
                    if p.nome == nome:
                        p.consultar_paciente()
                        break
                else:
                    print("Paciente não encontrado!")
            elif opcao == "3":
                if BancoDeDados.fila.empty():
                    print("Nenhum paciente na fila.")
                else:
                    prioridade, paciente = BancoDeDados.fila.get()  # O(log n)
                    print(f"\nAtendendo paciente: {paciente.nome} (risco: {paciente.estrato()})")
                    atendimento = input("Descrição do atendimento: ")
                    paciente.registrar_atendimento(atendimento)

                    nodo_impacto = registrar_aspecto()
                    paciente.adicionar_impacto(nodo_impacto)

                    criar_plano(nodo_impacto)

        # ----------------- PACIENTE -----------------
        elif usuario["tipo"] == "paciente":
            for p in BancoDeDados.pacientes:  # O(n)
                if p.nome == usuario["nome"]:
                    p.consultar_paciente()
                    break
            else:
                print("Cadastro não encontrado!")


if __name__ == "__main__":
    usuario = inicio()
    menu(usuario)
