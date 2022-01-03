import random
from art import logo, vs
from game_data import data
# from replit import clear

score = 0
is_game_on = True
player_1 = random.choice(data)


def check_result(guess, a_followers, b_followers):
    if a_followers > b_followers:
        if guess == 'A':
            return True
        else:
            return False
    else:
        if guess == 'B':
            return True
        else:
            return False


while is_game_on:
    # clear()
    print(logo)
    if score > 0:
        print(f"Current Score : {score}")
    print(f"Compare A: {player_1['name']}, {player_1['description']}, from {player_1['country']}.")
    print(vs)
    player_2 = random.choice(data)
    while player_1 == player_2:
        player_2 = random.choice(data)
    print(f"Against B: {player_2['name']}, {player_2['description']}, from {player_2['country']}.")

    user_guess = input("Who has more followers ? Type 'A' or 'B'. ").upper()
    is_correct = check_result(user_guess, player_1['follower_count'], player_2['follower_count'])
    if is_correct:
        score += 1
        player_1 = player_2
    else:
        print("Sorry, you're wrong. You Lose.")
        print(f"Your Final Score : {score}")
        is_game_on = False
