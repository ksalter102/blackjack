import random



def deal_card():
    """Returns a random card from deck"""
    cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11 ]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """Take list tof cards and returns calculated score"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, computer_score):
    """Compares the scores of a user against the scores of a computer"""
    if user_score == computer_score:
        return "Draw :|"
    elif computer_score == 0:
        return "You LOSE, opponent has BLACKJACK :O "
    elif user_score == 0:
        return "You WIN, wth a BLACKJACK! :)"
    elif user_score > 21:
        return "You went over 21, You lose!"
    elif computer_score > 21:
        return "Opponent went over 21, You win!"
    elif user_score > computer_score:
        return "You win! :)"
    else:
        return "You lose! :("

def play_game():
    user_card = []
    computer_card = []
    user_score = 0
    computer_score = 0
    game_over = False

    for _ in range(2):
        user_card.append(deal_card())
        computer_card.append(deal_card())

    while not game_over:

        user_score = calculate_score(user_card)
        computer_score = calculate_score(computer_card)

        print(f"Your cards:{user_card}, current score:{user_score}")
        print(f"My cards:{computer_card}, current score:{computer_score}")

        if user_score == 0 or computer_score == 0 or computer_score > 21:
            game_over = True
        else:
            user_should_deal = input("Do you want to draw another card? (y/n): ")
            if user_should_deal == "y":
                user_card.append(deal_card())
            else:
                game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_card.append(deal_card())
        computer_score = calculate_score(computer_card)

    print(f"Your final hand: {user_card}, final score: {user_score}")
    print(f"Computer's final hand: {computer_card}, final score: {computer_score}")
    print(compare(user_score, computer_score))



while input("Do you want to play a game of Blackjack? (y/n):") == 'y':
    play_game()

