def pesquisa_preferencia_clientes():
    # Declaração de variáveis
    clientes = 5
    idades = [0] * clientes
    sexos = [0] * clientes
    pratos_principais = [0] * clientes
    sobremesas = [0] * clientes
    bebidas = [0] * clientes

    cal_pratos = [180, 250, 350, 230]  # Calorias: Vegetariano, Frango, Carne, Peixe
    cal_sobremesas = [260, 110, 200, 170]  # Calorias: Fatia de Torta, Sorvete Diet, Mousse de Chocolate, Mousse Diet
    cal_bebidas = [90, 149, 140, 94]  # Calorias: Suco de Laranja, Refrigerante, Cerveja, Limonada

    # Contadores
    cont_pratos_femininos = [0] * 4
    cont_sobremesas_diet = 0
    cont_pratos = [0] * 4
    cont_sobremesas = [0] * 4
    cont_bebidas = [0] * 4
    total_calorias = 0

    # Entrada de dados
    print("----------- PESQUISA DE PREFERÊNCIA DOS CLIENTES ------------\n")

    for i in range(clientes):
        print(f"\n-------- Cliente {i + 1} --------")
        idades[i] = int(input("Qual a sua idade? "))

        sexos[i] = int(input("Qual o seu sexo? 1- Masculino, 2- Feminino: "))

        pratos_principais[i] = int(input("Qual tipo de prato principal consumiu? 1- Vegetariano, 2- Frango, 3- Carne, 4- Peixe: ")) - 1
        total_calorias += cal_pratos[pratos_principais[i]]
        cont_pratos[pratos_principais[i]] += 1

        sobremesa = int(input("Consumiu alguma sobremesa? 1- Fatia de Torta, 2- Sorvete Diet, 3- Mousse de Chocolate, 4- Mousse Diet (0 para nenhuma): "))
        if sobremesa != 0:
            sobremesas[i] = sobremesa - 1
            total_calorias += cal_sobremesas[sobremesas[i]]
            cont_sobremesas[sobremesas[i]] += 1
            if 30 <= idades[i] <= 50 and (sobremesas[i] == 1 or sobremesas[i] == 3):
                cont_sobremesas_diet += 1
        else:
            sobremesas[i] = -1

        bebida = int(input("Consumiu alguma bebida? 1- Suco de Laranja, 2- Refrigerante, 3- Cerveja, 4- Limonada (0 para nenhuma): "))
        if bebida != 0:
            bebidas[i] = bebida - 1
            total_calorias += cal_bebidas[bebidas[i]]
            cont_bebidas[bebidas[i]] += 1
        else:
            bebidas[i] = -1

        if sexos[i] == 2:
            cont_pratos_femininos[pratos_principais[i]] += 1

    # Cálculo da média de calorias consumidas
    media_calorias = total_calorias / clientes

    # Prato principal mais consumido pelas mulheres
    max_prato_feminino = max(cont_pratos_femininos)
    tipo_prato_mais_consumido_feminino = cont_pratos_femininos.index(max_prato_feminino)

    # Combo mais consumido
    max_prato = max(cont_pratos)
    tipo_prato_mais_consumido = cont_pratos.index(max_prato)

    max_sobremesa = max(cont_sobremesas)
    tipo_sobremesa_mais_consumida = cont_sobremesas.index(max_sobremesa)

    max_bebida = max(cont_bebidas)
    tipo_bebida_mais_consumida = cont_bebidas.index(max_bebida)

    # Resultados
    print(f"\n\n1. A média de calorias consumidas pelo grupo: {media_calorias:.2f}")
    print(f"2. O tipo de prato principal mais consumido pelas mulheres: {['Vegetariano', 'Frango', 'Carne', 'Peixe'][tipo_prato_mais_consumido_feminino]}")
    print(f"3. Quantas pessoas entre 30 e 50 anos consumiram algum tipo de sobremesa Diet: {cont_sobremesas_diet}")
    print(f"4. O combo mais consumido: {['Vegetariano', 'Frango', 'Carne', 'Peixe'][tipo_prato_mais_consumido]}, "
          f"{['Fatia de Torta', 'Sorvete Diet', 'Mousse de Chocolate', 'Mousse Diet'][tipo_sobremesa_mais_consumida]}, "
          f"{['Suco de Laranja', 'Refrigerante', 'Cerveja', 'Limonada'][tipo_bebida_mais_consumida]}")

# Executa a função
pesquisa_preferencia_clientes()
