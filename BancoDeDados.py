from queue import PriorityQueue
from nodo import Nodo
from utils import imprimir_arvore
class BancoDeDados:

    pacientes = []  # lista compartilhada entre todas as instâncias
    fila = PriorityQueue () # fila de prioridade de atendimento.

    def __init__(self, nome, idade):    # Cadastro de paciente não cadastrados
        self.nome = nome
        self.idade = int(idade)
        self.raiz = Nodo(valor=nome, tipo="paciente") # raiz da árvore
        self.historico = [] #lista de atendimentos

    def cadastrar(self):
        BancoDeDados.pacientes.append(self)
        print(f"Pronto {self.nome}, você foi cadastrado!\nIdade: {self.idade}")
        self.adicionar_fila() # Adiciona automaticamente à fila
    
    def registrar_atendimento(self, descricao):
        self.historico.append(descricao)
        print(f"Atendimento registrado: {descricao}")
    
    def adicionar_impacto(self, nodo_impacto):
        self.raiz.adicionar_filho(nodo_impacto)
        print(f"Impacto'{nodo_impacto.valor} associado ao paciente {self.nome}")
    
    def consultar_paciente(self):
        print(f"\nPaciente: {self.nome} | idade: {self.idade}")
        print("Historico clinico:")
        if self.historico:
            for h in self.historico:
                print(f"-{h}")
        else:
            print("Nenhum atendimento registrado.")
        print("\nImpactos Ambientais e Planos PDCA: ")
        imprimir_arvore(self.raiz)

    @classmethod
    def verificacao(cls, nome):   # verificação de participantes já cadastrados
        return nome in cls.pacientes

    def resultados(self, aprovados, reprovados):
        total = aprovados + reprovados
        if total == 0:
            print("Nenhum resultado disponível.")
            return
        eficacia_geral = (aprovados / total) * 100
        print(f"Eficácia geral: {eficacia_geral:.2f}%")
    
    def estrato(self):
        # Retorna um rótulo simples de risco baseado na idade.
        if self.idade < 30:
            return "baixo"
        elif self.idade < 60:
            return "medio"
        else:
            return "alto"
    
    def adicionar_fila(self):
        #Adicionando o paciente à fila com prioridade baseada no risco.
        prioridade = {"alto": 1, "medio": 2, "baixo":3} # Menor = mais urgente
        BancoDeDados.fila.put((prioridade[self.estrato()], self))
        print(f"{self.nome} adicionado à fila com risco {self.estrato()}")
    
    @classmethod
    def atender_fila(cls):
        #Atender os pacientes na ordem de prioridade.
        if cls.fila.empty():
            print("Nenhum paciente na fila.")
            return
        print("\nAtendendo Paciente: ")
        while not cls.fila.empty():
            prioridade, paciente = cls.fila.get()
            print(f"Atendendo {paciente.nome} (risco: {paciente.estrato()})")
    
