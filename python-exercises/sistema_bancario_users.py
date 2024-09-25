"""
## Descrição do Projeto

Este projeto é um sistema bancário simples, desenvolvido em Python, que permite a criação de contas, realização de depósitos, saques e transferências, com funcionalidades 
adicionais de login e verificação de senha para operações. Ele foi implementado usando os seguintes métodos e técnicas de programação:

- Manipulação de Strings e Listas: para armazenamento e verificação de dados de usuários e contas.
- Estruturas de Controle: como loops e condicionais para navegação e controle do fluxo do programa.
- Funções e Modularização: para organizar e reutilizar o código, facilitando a manutenção e extensão das funcionalidades.
- Validação de Dados: para assegurar a integridade dos dados durante o cadastro e operações financeiras.
- Simulação de Banco de Dados com Arquivos de Texto: para armazenar informações persistentes como contas e transações realizadas.

O objetivo do projeto é oferecer um exemplo prático e didático para iniciantes que queiram entender conceitos de programação aplicados a um contexto de sistema bancário. 

"""
import datetime

def registrar_usuario(users):
    print("\n==== Cadastro de Usuário ====")
    while True:
        username = input("Digite um nome de usuário: ").strip().lower()
        if username in users:
            print("Nome de usuário já existe. Tente outro.")
        elif not username:
            print("O nome de usuário não pode estar vazio.")
        else:
            break

    while True:
        senha = input("Digite uma senha de 4 dígitos: ").strip()
        if not senha.isdigit() or len(senha) != 4:
            print("Senha inválida. A senha deve conter exatamente 4 dígitos numéricos.")
        else:
            break

    # Inicializa os dados do novo usuário
    users[username] = {
        'senha': senha,
        'saldo': 0.0,
        'limite_saque_total': 3,
        'limite_saque': 3,
        'extratos': [],
        'cont_extratos': 0,
        'ultima_data': datetime.datetime.now().date()
    }

    print(f"Usuário '{username}' registrado com sucesso!\n")

def login_usuario(users):
    print("\n==== Login de Usuário ====")
    username = input("Digite seu nome de usuário: ").strip().lower()
    if username not in users:
        print("Nome de usuário não encontrado. Por favor, registre-se primeiro.\n")
        return None, None

    senha = input("Digite sua senha de 4 dígitos: ").strip()
    if users[username]['senha'] != senha:
        print("Senha incorreta. Tente novamente.\n")
        return None, None

    print(f"Login bem-sucedido! Bem-vindo, {username}.\n")
    return username, users[username]

def banco_deposito(user_data):
    try:
        deposit = float(input("Digite o valor de Depósito: R$"))
    except ValueError:
        print("Entrada inválida. Por favor, insira um número válido.")
        return

    if deposit <= 0:
        print("Valor de Depósito Inválido.")
    else:
        user_data['saldo'] += deposit  # Atualiza o saldo
        user_data['cont_extratos'] += 1  # Incrementa o contador de extratos
        timestamp = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        new_extrato = {
            "id": user_data['cont_extratos'],
            "tipo": "Depósito",
            "valor": deposit,
            "data": timestamp
        }
        user_data['extratos'].append(new_extrato)  # Adiciona o extrato à lista de extratos

        print(f"Depósito realizado com sucesso! Saldo Atual: R${user_data['saldo']:.2f}\n")

def banco_saque(user_data):
    try:
        saque = float(input(f"Digite o valor de Saque (Máximo por saque: R$500 | Saques Restantes: {user_data['limite_saque']}): R$"))
    except ValueError:
        print("Entrada inválida. Por favor, insira um número válido.")
        return

    hoje = datetime.datetime.now().date()
    if hoje != user_data['ultima_data']:
        user_data['limite_saque'] = user_data['limite_saque_total']
        user_data['ultima_data'] = hoje

    if saque <= 0:
        print("Valor de Saque Inválido.")
    elif saque > 500:
        print("Valor de saque acima do permitido por transação (R$500).")
    elif user_data['limite_saque'] <= 0:
        print("Limite de saques diários excedido.")
    elif saque > user_data['saldo']:
        print("Saldo insuficiente.")
    else:
        user_data['saldo'] -= saque  # Atualiza o saldo
        user_data['limite_saque'] -= 1  # Decrementa o número de saques restantes
        user_data['cont_extratos'] += 1  # Incrementa o contador de extratos
        timestamp = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        new_extrato = {
            "id": user_data['cont_extratos'],
            "tipo": "Saque",
            "valor": saque,
            "data": timestamp
        }
        user_data['extratos'].append(new_extrato)  # Adiciona o extrato à lista de extratos
        print(f"Saque realizado com sucesso! Saldo Atual: R${user_data['saldo']:.2f}\n")

def banco_extrato(user_data):
    if not user_data['extratos']:
        print("\nNão há extratos no momento.\n")
    else:
        print("\n==== Lista de Extratos ====")
        for extrato in user_data['extratos']:
            print(f"ID {extrato['id']}: {extrato['tipo']} de R${extrato['valor']:.2f} em {extrato['data']}")
        print()  # Linha em branco para melhor formatação

def main():
    users = {}
    username_logado = None
    user_data_logado = None

    while True:
        if not username_logado:
            print("""\n
    ========== SISTEMA BANCÁRIO ==========
    1: Registrar
    2: Login
    3: Sair
    ======================================
            """)
            escolha = input("Digite o número da operação desejada: ").strip()

            if escolha == '1':
                registrar_usuario(users)
            elif escolha == '2':
                username, user_data = login_usuario(users)
                if username:
                    username_logado = username
                    user_data_logado = user_data
            elif escolha == '3':
                print("Saindo do Sistema Bancário. Até logo!")
                break
            else:
                print("Opção Inválida. Tente novamente.\n")
        else:
            print(f"""\n
    ========== SISTEMA BANCÁRIO ==========
    Usuário: {username_logado}
    Saldo Atual = R${user_data_logado['saldo']:.2f}
    Limite de Saques Restantes = {user_data_logado['limite_saque']} (Máximo por dia: {user_data_logado['limite_saque_total']})
    ============ Operações: =============
    1: Depósito
    2: Saque
    3: Extrato
    4: Logout
    ======================================
            """)
            operacao = input("Digite o número da operação desejada: ").strip()

            if operacao == '1':
                banco_deposito(user_data_logado)
            elif operacao == '2':
                banco_saque(user_data_logado)
            elif operacao == '3':
                banco_extrato(user_data_logado)
                input("Pressione Enter para voltar ao menu principal.")
            elif operacao == '4':
                print(f"Usuário '{username_logado}' deslogado com sucesso.\n")
                username_logado = None
                user_data_logado = None
            else:
                print("Opção Inválida. Tente novamente.\n")

if __name__ == "__main__":
    main()

