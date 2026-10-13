
import random

# Baralho de cartas
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


# Escolher uma carta aleatória
def deal_card():
    return random.choice(cards)


# Calcular a pontuação
def calculate_score(cards):

    # Blackjack: 21 pontos com duas cartas
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    # Transformar Ás de 11 para 1 se ultrapassar 21
    if sum(cards) > 21 and 11 in cards:
        cards[cards.index(11)] = 1

    return sum(cards)


# Comparar as pontuações
def compare(user_score, computer_score):
    if user_score > 21:
        return "You went over. You lose!"

    elif user_score == computer_score:
        return "Draw!"

    elif computer_score == 0:
        return "You lose! Computer has Blackjack."

    elif user_score == 0:
        return "You win with a Blackjack!"

    elif computer_score > 21:
        return "Computer went over. You win!"

    elif user_score > computer_score:
        return "You win!"

    else:
        return "You lose!"







# Função que executa uma partida completa
def play_game():
    user_cards = []
    computer_cards = []

    # Distribuir duas cartas para cada jogador
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    # Calcular pontuações iniciais
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    # VEZ DO JOGADOR
    while True:
        user_score = calculate_score(user_cards)

        print(f"\nYour cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or user_score > 21:
            break

        should_continue = input(
            "Deseja mais uma carta? 'y' ou 'n': "
        ).lower()

        if should_continue == "y":
            user_cards.append(deal_card())
        else:
            break

    # VEZ DO COMPUTADOR
    if user_score != 0 and user_score <= 21 and computer_score != 0:
        while computer_score < 17:
            computer_cards.append(deal_card())
            computer_score = calculate_score(computer_cards)

    # RESULTADO FINAL
    print(f"\nYour final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")

    print(compare(user_score, computer_score))


# REPETIR O JOGO
while True:
    play_game()

    continuar = input("\nJogar novamente? y/n: ").lower()

    if continuar == "n":
        print("Obrigado por jogar Blackjack!")
        break
