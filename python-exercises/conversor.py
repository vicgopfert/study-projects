# Funções para conversão de comprimento
def cm_to_m(cm):
    return cm / 100

def cm_to_km(cm):
    return cm / (100 * 1000)

def m_to_cm(m):
    return m * 100

def m_to_km(m):
    return m / 1000

def km_to_cm(km):
    return km * 100000

def km_to_m(km):
    return km * 1000

# Dicionário de conversões
conversoes = {
    1: ('cm', 'm', cm_to_m),
    2: ('cm', 'km', cm_to_km),
    3: ('m', 'cm', m_to_cm),
    4: ('m', 'km', m_to_km),
    5: ('km', 'cm', km_to_cm),
    6: ('km', 'm', km_to_m)
}

# Menu de opções para o usuário
print("Escolha a medida:")
print("1. Centímetros (cm)")
print("2. Metros (m)")
print("3. Quilômetros (km)")

medida_opcao = int(input("Digite o número da medida escolhida: "))

if medida_opcao == 1:
    medida = 'cm'
    number = float(input(f"Digite o valor em {medida}: "))
    # Opção de conversão
    print("Escolha a conversão:")
    print("1. cm para m")
    print("2. cm para km")
    convert_opcao = int(input("Digite a opção de conversão: "))
elif medida_opcao == 2:
    medida = 'm'
    number = float(input(f"Digite o valor em {medida}: "))
    # Opção de conversão
    print("Escolha a conversão:")
    print("3. m para cm")
    print("4. m para km")
    convert_opcao = int(input("Digite a opção de conversão: "))
elif medida_opcao == 3:
    medida = 'km'
    number = float(input(f"Digite o valor em {medida}: "))
    # Opção de conversão
    print("Escolha a conversão:")
    print("5. km para cm")
    print("6. km para m")
    convert_opcao = int(input("Digite a opção de conversão: "))
else:
    print("Opção inválida.")
    exit()

# Verifica e realiza a conversão
conversao = conversoes.get(convert_opcao)
if conversao: # Verifica se a busca no dicionário retornou um valor válido
    unidade_origem, unidade_destino, funcao = conversao # Associa cada variável ao valor da opção do dicionário respectivamente
    if medida == unidade_origem:
        result = funcao(number)
        print(f"Resultado da conversão: {result} {unidade_destino}")
    else:
        print(f'Conversão inválida para a medida {medida}')
else:
    print('Conversão inválida')


  