def calcula_velocidade(distancia, tempo):
    if distancia <= 0 or tempo <= 0:
        raise ValueError("Distância e tempo devem ser maiores que zero.")
    return distancia / tempo

def classifica_velocidade(velocidade):
    if velocidade < 50:
        return 'Baixa'
    elif 50 <= velocidade <= 100:
        return 'Média'
    else:
        return 'Alta'

# Exemplos
try:
    v1 = calcula_velocidade(100, 2)
    c1 = classifica_velocidade(v1)
    print(f"Viagem1: Velocidade {v1:.2f} km/h, Classificação: {c1}")
    
    v2 = calcula_velocidade(200, 3)
    c2 = classifica_velocidade(v2)
    print(f"Viagem2: Velocidade {v2:.2f} km/h, Classificação: {c2}")
    
    v3 = calcula_velocidade(50, 1.5)
    c3 = classifica_velocidade(v3)
    print(f"Viagem3: Velocidade {v3:.2f} km/h, Classificação: {c3}")
except ValueError as e:
    print(e)