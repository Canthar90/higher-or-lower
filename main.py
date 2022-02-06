
from art import logo, vs
from game_data import data
import random
import os
import time

clear = lambda: os.system('cls')


def random_choice():
    return random.choice(data)


def duplicate_check(first, second):
    """Sprawdza czy nie trafił się duplikat"""
    flag = 0
    while flag == 0:
        if first == second:
            second = random_choice()
            return second
        else:
            flag = 1
            return second


def choice_and_check(first, second):
    """Prosi gracza o podjęcie wyboru oraz sprawdza jego wybór zwraca True/False oraz second"""
    print(f"Compare A: {first['name']}, a {first['description']}, from {first['country']}")
    print(vs)
    print(f"Against B: {second['name']}, a {second['description']}, from {second['country']}")
    #print(f"testowo A {first['follower_count']} B {second['follower_count']}  ")
    choice = input("Who has more followers? Type 'A' or 'B': ").lower()
    if choice == 'a' and int(first['follower_count']) > int(second['follower_count']):
        return True, second
    elif choice == 'b' and int(first['follower_count']) < int(second['follower_count']):
        return True, second
    else:
        return False, second


def game_reset():
    again = input("Do you wanna play again? Type 'y'").lower()
    if again == 'y':
        game_start()


def mid_game(flag, first):
    score = 1
    while flag:
        clear()
        print(logo)
        print(f"Your right! Current score: {score} ")
        second = random_choice()
        second = duplicate_check(first=first, second=second)
        second_flag, first = choice_and_check(first=first, second=second)
        if second_flag:
            score += 1
        else:
            clear()
            print(logo)
            print(f"Sorry that's wrong. Final score: {score}")
            game_reset()
            time.sleep(8)
            flag = False



def game_start():
    clear()
    print(logo)
    first_rand = random_choice()
    second_rand = random_choice()
    second_rand = duplicate_check(first=first_rand, second=second_rand)
    flag, first_rand = choice_and_check(first=first_rand, second=second_rand)
    if flag:
        mid_game(flag=flag, first=first_rand)
    else:
        clear()
        print(logo)
        print(f"Sorry that's wrong. Final score: 0")
        game_reset()
        time.sleep(8)
game_start()