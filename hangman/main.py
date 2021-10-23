import random
from images import stages
from words import word_list, logo

#word_list = ["one", "two", "tree"]


def hamgman_game():
    chosen_word = random.choice(word_list)
    wordlenth = len(chosen_word)
    display = []
    print(logo)

    for letter in range(wordlenth):
        display += '_'
    print(display)

    end_of_game = False
    lives = 6

    while end_of_game != True:
        guess = input("guess the letters for this word\n").lower()
        if guess in display:
            print(f"you have already guessed this word {guess}, try another one.")
        for position in range(wordlenth):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter
        if guess not in chosen_word:
            lives -= 1
            print(f'You have guess a wrong letter you loose a life. now you have {lives} left')
        image = stages[lives]
        print(image)
        print(display)

        if "_" not in display:
            end_of_game = True
            print("Your Won!")
        else:
            if lives == 0:
                end_of_game = True
                print('YOU LOSE!')

    start_again = input('Would you like to play again? please input "y" for yes or "n" for no ').lower()
    if start_again == 'y':
        hamgman_game()
    else:
        print('😎 Thank you for playing 🤗')


hamgman_game()