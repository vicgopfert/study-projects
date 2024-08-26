#include <stdio.h>

int main() {
    // Declaração de variáveis
    int clientes = 45;
    int idades[clientes], sexos[clientes], pratos_principais[clientes], sobremesas[clientes], bebidas[clientes];
    int cal_pratos[] = {180, 250, 350, 230}; // Calorias : Vegetariano, Frango, Carne, Peixe
    int cal_sobremesas[] = {260, 110, 200, 170}; // Calorias : Fatia de Torta, Sorvete Diet, Mousse de Chocolate, Mousse Diet
    int cal_bebidas[] = {90, 149, 140, 94}; // Calorias : Suco de Laranja, Refrigerante, Cerveja, Limonada

    // Contadores
    int cont_pratos_femininos[4] = {0}; // Prato mais consumido pelas mulheres
    int cont_sobremesas_diet = 0; // Pessoas entre 30 e 50 anos que consumiram sobremesa diet
    int cont_pratos[4] = {0};
    int cont_sobremesas[4] = {0};
    int cont_bebidas[4] = {0};
    int total_calorias = 0;

    // Entrada de dados
    printf("----------- PESQUISA DE PREFERÊNCIA DOS CLIENTES ------------\n\n");
    for (int i = 0; i < clientes; i++) {
        printf("\n-------- Cliente %d --------\n", i + 1);
        printf("Qual a sua idade? ");
        scanf("%d", &idades[i]);

        printf("Qual o seu sexo? 1- Masculino, 2- Feminino: ");
        scanf("%d", &sexos[i]);

        printf("Qual tipo de prato principal consumiu? 1- Vegetariano, 2- Frango, 3- Carne, 4- Peixe: ");
        scanf("%d", &pratos_principais[i]);
        pratos_principais[i]--; // Ajustar índice para 0 a 3
        total_calorias += cal_pratos[pratos_principais[i]];
        cont_pratos[pratos_principais[i]]++;

        int sobremesa;
        printf("Consumiu alguma sobremesa? Se sim, qual o tipo de sobremesa comeu? 1- Fatia de Torta, 2- Sorvete Diet, 3- Mousse de Chocolate, 4- Mousse Diet (0 para nenhuma): ");
        scanf("%d", &sobremesa);
        if (sobremesa != 0) {
            sobremesas[i] = sobremesa - 1; // Ajustar índice para 0 a 3
            total_calorias += cal_sobremesas[sobremesas[i]];
            cont_sobremesas[sobremesas[i]]++;

            // Quantidade de sobremesas diet para pessoas entre 30 e 50 anos
            if (idades[i] >= 30 && idades[i] <= 50 && (sobremesas[i] == 1 || sobremesas[i] == 3)) {
                cont_sobremesas_diet++;
            }
        } else {
            sobremesas[i] = -1; // Nenhuma sobremesa
        }

        int bebida;
        printf("Consumiu alguma bebida? Se sim, qual o tipo de bebida? 1- Suco de Laranja, 2- Refrigerante, 3- Cerveja, 4- Limonada (0 para nenhuma): ");
        scanf("%d", &bebida);
        if (bebida != 0) {
            bebidas[i] = bebida - 1; // Ajustar índice para 0 a 3
            total_calorias += cal_bebidas[bebidas[i]];
            cont_bebidas[bebidas[i]]++;
        } else {
            bebidas[i] = -1; // Nenhuma bebida
        }

        // Contagem de pratos principais consumidos por mulheres
        if (sexos[i] == 2) {
            cont_pratos_femininos[pratos_principais[i]]++;
        }
    }

    // Cálculo da média de calorias consumidas
    double media_calorias = total_calorias / (double)clientes;

    // Processamento do prato principal mais consumido pelas mulheres
    int max_prato_feminino = 0;
    int tipo_prato_mais_consumido_feminino = 0;
    for (int i = 0; i < 4; i++) {
        if (cont_pratos_femininos[i] > max_prato_feminino) {
            max_prato_feminino = cont_pratos_femininos[i];
            tipo_prato_mais_consumido_feminino = i;
        }
    }

    // Processamento do combo mais consumido
    int max_prato = 0, max_sobremesa = 0, max_bebida = 0;
    int tipo_prato_mais_consumido = 0, tipo_sobremesa_mais_consumida = 0, tipo_bebida_mais_consumida = 0;
    for (int i = 0; i < 4; i++) {
        if (cont_pratos[i] > max_prato) {
            max_prato = cont_pratos[i];
            tipo_prato_mais_consumido = i;
        }
        if (cont_sobremesas[i] > max_sobremesa) {
            max_sobremesa = cont_sobremesas[i];
            tipo_sobremesa_mais_consumida = i;
        }
        if (cont_bebidas[i] > max_bebida) {
            max_bebida = cont_bebidas[i];
            tipo_bebida_mais_consumida = i;
        }
    }

    // Saída de dados
    printf("\n\nResultados da Pesquisa:\n");
    printf("1. A média de calorias consumidas pelo grupo: %.2f\n", media_calorias);
    printf("2. O tipo de prato principal mais consumido pelas mulheres: ");
    if (tipo_prato_mais_consumido_feminino == 0){
        printf ("Vegetariano\n");
    } else if (tipo_prato_mais_consumido_feminino == 1){
        printf ("Frango\n");
    } else if (tipo_prato_mais_consumido_feminino == 2){
        printf ("Carne\n");
    } else if (tipo_prato_mais_consumido_feminino == 3){
        printf ("Peixe\n");
    }
    printf("3. Quantas pessoas entre 30 e 50 anos consumiram algum tipo de sobremesa Diet: %d\n", cont_sobremesas_diet);
    printf("4. O combo mais consumido: ");
    if (tipo_prato_mais_consumido == 0){
        printf ("Vegetariano");
    } else if (tipo_prato_mais_consumido == 1){
        printf ("Frango");
    } else if (tipo_prato_mais_consumido == 2){
        printf ("Carne");
    } else if (tipo_prato_mais_consumido == 3){
        printf ("Peixe");
    }
    printf(", ");
    if (tipo_sobremesa_mais_consumida == 0){
        printf ("Fatia de Torta");
    } else if (tipo_sobremesa_mais_consumida == 1){
        printf ("Sorvete Diet");
    } else if (tipo_sobremesa_mais_consumida == 2){
        printf ("Mouse de Chocolate");
    } else if (tipo_sobremesa_mais_consumida == 3){
        printf ("Mouse Diet");
    }
    printf(", ");
    if (tipo_bebida_mais_consumida == 0){
        printf ("Suco de Laranja");
    } else if (tipo_bebida_mais_consumida == 1){
        printf ("Refrigerante");
    } else if (tipo_bebida_mais_consumida == 2){
        printf ("Cerveja");
    } else if (tipo_bebida_mais_consumida == 3){
        printf ("Limonada");
    }

    return 0;
}