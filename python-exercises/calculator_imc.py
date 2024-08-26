# Variáveis de peso, altura, imc e idades
cont_entrevistados = 1
cont_magro = 0
cont_saudavel = 0
cont_sobrepeso = 0
cont_obesidade1 = 0
cont_obesidade2 = 0
cont_obesidade3 = 0

idades_magro = []
idades_saudavel = []
idades_sobrepeso = []
idades_obesidade1 = []
idades_obesidade2 = []
idades_obesidade3 = []

# Função cálculo de IMC para cada entrevistado
def imc_calculator(idade):
    global cont_magro, cont_saudavel, cont_sobrepeso, cont_obesidade1, cont_obesidade2, cont_obesidade3
    peso = float(input("Digite seu Peso(kg): "))
    altura = float(input("Digite sua Altura(m): "))
    imc = peso / (altura * altura) 
    
    # Estrutura condicional para categorizar o IMC    
    if imc < 18.5:
        print("Abaixo do peso")
        cont_magro += 1
        idades_magro.append(idade)
    elif 18.5 <= imc < 24.9:
        print("Saudável")
        cont_saudavel += 1
        idades_saudavel.append(idade)
    elif 25 <= imc < 29.9:
        print("Levemente acima do peso")
        cont_sobrepeso += 1
        idades_sobrepeso.append(idade)
    elif 30 <= imc < 34.9:
        print("Moderadamente acima do peso")
        cont_obesidade1 += 1
        idades_obesidade1.append(idade)
    elif 35 <= imc < 39.9:
        print("Severamente acima do peso")
        cont_obesidade2 += 1
        idades_obesidade2.append(idade)
    elif imc >= 40:
        print("Obesidade máxima")
        cont_obesidade3 += 1
        idades_obesidade3.append(idade)                 

# Função cálculo da média de idade
def calcular_media(idades):
    return sum(idades) / len(idades) if idades else 0

while True:
    print(f"___Entrevistado Nº{cont_entrevistados}___")
    nome = input("Digite sua idade ou 'fim' para encerrar o formulário: ")
    if nome.lower() == "fim":
        break
    else: 
        idade = int(nome)
        imc_calculator(idade)
        cont_entrevistados += 1
        total_entrevistados = cont_entrevistados - 1
        
        
print("__________ RESULTADOS____________")
print("- Quantidade de pessoas entrevistadas:", total_entrevistados)
print("- Quantidade de pessoas Abaixo do Peso:", cont_magro, "| Média de Idade:", calcular_media(idades_magro))
print("- Quantidade de pessoas Saudáveis:", cont_saudavel, "| Média de Idade:", calcular_media(idades_saudavel))
print("- Quantidade de pessoas Levemente Acima do Peso:", cont_sobrepeso, "| Média de Idade:", calcular_media(idades_sobrepeso))
print("- Quantidade de pessoas Moderadamente Acima do Peso:", cont_obesidade1, "| Média de Idade:", calcular_media(idades_obesidade1))
print("- Quantidade de pessoas Severamente Acima do Peso:", cont_obesidade2, "| Média de Idade:", calcular_media(idades_obesidade2))
print("- Quantidade de pessoas com Obesidade Máxima:", cont_obesidade3, "| Média de Idade:", calcular_media(idades_obesidade3))




