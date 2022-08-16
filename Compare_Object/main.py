import random
from data import datas
from function import *

win_score = 0

is_end_game = False
while not is_end_game:
    print("========================>Start Guess<======================")
    ran_user1 = random.choice(datas)
    ran_user2 = random.choice(datas)

    while ran_user1 == ran_user2:
        ran_user2 = random.choice(datas)

    print_object(ran_user1)
    print_object(ran_user2)

    user_choose = input("Which user have more flower than 'A' or 'B' ").lower()

    result_compare = compare_object(ran_user1, ran_user2)

    if user_choose == result_compare:
        win_score += 1
        print(f'You are correct and your score is {win_score}')
    else:
        print(f'You are not correct and your score is {win_score}')
        is_end_game = True
