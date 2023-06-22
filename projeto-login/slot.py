import random

# Define as imagens dos slots
slots = ["🍒", "🍊", "🍇", "🔔", "💰", "🍀"]

# Define o saldo inicial do jogador
saldo = 10000

# Define a aposta mínima e máxima
aposta_minima = 1
aposta_maxima = 1000

# Função para girar os slots
def girar_slots():
    # Escolhe aleatoriamente uma imagem para cada slot
    slot1 = random.choice(slots)
    slot2 = random.choice(slots)
    slot3 = random.choice(slots)
    
    # Retorna os resultados dos slots
    return (slot1, slot2, slot3)

# Função para calcular o resultado da aposta
def calcular_resultado_aposta(aposta, resultado_slots):
    # Verifica se os slots são iguais
    if resultado_slots[0] == resultado_slots[1] == resultado_slots[2]:
        # Três slots iguais - o jogador ganha 10x a aposta
        return aposta * 10
    elif resultado_slots[0] == resultado_slots[1] or resultado_slots[1] == resultado_slots[2]:
        # Dois slots iguais - o jogador ganha 5x a aposta
        return aposta * 5
    else:
        # Nenhum slot igual - o jogador perde a aposta
        return -aposta

# Loop principal do jogo
while True:
    # Imprime o saldo atual do jogador
    print("Seu saldo atual é de", saldo)
    
    # Pede ao jogador para fazer uma aposta
    aposta = int(input("Digite o valor da sua aposta (entre {} e {}): ".format(aposta_minima, aposta_maxima)))
    
    # Verifica se a aposta é válida
    if aposta < aposta_minima or aposta > aposta_maxima:
        print("A aposta deve estar entre {} e {}".format(aposta_minima, aposta_maxima))
        continue
    
    # Gira os slots
    resultado_slots = girar_slots()
    
    # Imprime o resultado dos slots
    print("Os slots são:", resultado_slots)
    
    # Calcula o resultado da aposta
    resultado_aposta = calcular_resultado_aposta(aposta, resultado_slots)
    
    # Atualiza o saldo do jogador
    saldo += resultado_aposta
    
    # Imprime o resultado da aposta
    if resultado_aposta > 0:
        print("Você ganhou", resultado_aposta)
    else:
        print("Você perdeu", -resultado_aposta)
    
    # Verifica se o jogador ficou sem saldo
    if saldo <= 0:
        print("Você ficou sem dinheiro!")
        break