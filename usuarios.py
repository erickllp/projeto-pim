usuarios = [
    {"nome": "admin", "senha": "1234", "tipo": "admin"},
    {"nome": "medico1", "senha": "abcd", "tipo": "medico"},
    {"nome": "paciente1", "senha": "0000", "tipo": "paciente"}
]

def login():
    print("\nLOGIN\n") 
    nome = input("Usuário: ")
    senha = input("Senha: ")

    for user in usuarios:
        if user["nome"] == nome and user["senha"] == senha:
            print(f"Login conluido! Tipo: {user['tipo']}\n")
            return user

    print("Usuário ou senha incorretos!")
    return None

def cadastro():
    
    print("\n=== Cadastro de Usuário ===")
    nome = input("Digite o nome do novo usuário: ")

    for u in usuarios:
        if u["nome"] == nome:
            print("Já existe um usuário com esse nome!")
            return
    
    senha = input("Digite a senha: ")
    tipo = input("Digite o tipo (medico/admin): ").lower()

    # append automático
    usuarios.append({"nome": nome, "senha": senha, "tipo": tipo})
    print(f"Usuário {nome} ({tipo}) cadastrado com sucesso!")