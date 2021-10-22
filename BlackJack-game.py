import random
from replit import clear
#from ar import logo

user_score = 0
dealer_score = 0
dealer_card = []
user_card = []
winner = ''
players = {}
end_game = False

cards_list = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# User's card and score:
def black_jack_game():
    print(logo)
    user_card = random.sample(cards_list, k=2)
    if sum(user_card) == 21 and len(user_card) == 2:
        user_card = 0
        user_score = sum(user_card)
        print(user_card)
    elif 11 in user_card and sum(user_card) > 21:
        user_card.remove(11)
        user_card.append(1)
        user_score = sum(user_card)
        print(user_card)
    else:
        user_score = sum(user_card)
        print(f'Your cards: {user_card}, current score: {user_score}')

    # Dealer's cards and score:
    dealer_card = random.sample(cards_list, k=2)
    if sum(dealer_card) == 21 and len(dealer_card) == 2:
        dealer_card = 0
        dealer_score = sum(dealer_card)
    elif 11 in dealer_card and sum(dealer_card) > 21:
        dealer_card.remove(11)
        dealer_card.append(1)
        dealer_score = sum(dealer_card)
    else:
        dealer_score = sum(dealer_card)
        print(f"Dealer's first card: {dealer_card}, current score: {dealer_score}")


    def calculate_winner():
        if user_score > 21 and dealer_score > 21:
            print(f"You both lost, your scrore of {user_score} and {dealer_score} have supass the scoore of 21")
        if user_score == 0 and dealer_score > 0:
            print("You win with a black-jack")
        if dealer_score == 0 and user_score > 0:
            print("Dealer wins with a balck-jack")
        if user_score == 21 and dealer_score == 21 or user_score == 0 and dealer_score == 0:
            print(f"There's a tie, your score of {user_score} and {dealer_score} are the same, try again")
        if user_score <= 21 and dealer_score > 21 or user_score <= 21 and dealer_score > user_score or user_score <=21 and dealer_score < user_score:
            print(f"You won with a score of  {user_score}, dealer lose with a score of {dealer_score}")
        if dealer_score <= 21 and user_score > 21 or dealer_score <= 21 and user_score > dealer_score or dealer_score <= 21 and user_score < dealer_score:
            print(f"Dealer wins with a score of  {dealer_score}, you lose with a score of {user_score}")

#my while loop to calculate if game should continue based on current scores
    while end_game == False:
        if user_score == 0 or dealer_score == 0 or user_score > 21:
            end_game == True
            calculate_winner()
        else:
            user_choice = input("Type 'y' to get another card, type 'n' to pass ")
            if user_choice == 'y':
                user_card2 = random.choice(cards_list)
                user_card.append(user_card2)
                user_score += user_card2
                print(f'Your cards: {user_card}, current score: {user_score}')
            else:
                end_game == True
            while dealer_score != 0 and dealer_score < 16:
                dealer_card2 = random.choice(cards_list)
                dealer_card.append(dealer_card2)
                dealer_score = sum(dealer_card)
                print(f"Dealer's first card: {dealer_card}, current score: {dealer_score}")
            calculate_winner()
            play()
            clear()
            break
#the start of my program
def play():
    user_choice = input("would you like to play the game BlackJack? type 'y' or 'n' ")
    if user_choice == 'y':                                                             
        black_jack_game()                                                              
    elif user_choice == 'n':
        print("No problem")
play()
