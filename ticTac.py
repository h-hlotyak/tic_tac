import random
import time

board = {
    "first_row": ["___", "___","___"],
    "second_row": ["___","___","___"],
    "third_row": ["___","___","___"]
    }


def player_choosing():
    choosing = True
    while choosing:
        row_choice = input("Player 1, which row would you like to play? '1', '2', or '3': ")
        collum_choice = input("Player 1, collum would you like to play? '1', '2', or '3': ")
        collum_choice = int(collum_choice)
        pick = collum_choice - 1
        if row_choice == "1" and board["first_row"][pick] == "___":
            board["first_row"][pick] = "_X_"
            print(board["first_row"])
            print(board["second_row"])
            print(board["third_row"])
            choosing = False
        elif row_choice == "2" and board["second_row"][pick] == "___":
            board["second_row"][pick] = "_X_"
            print(board["first_row"])
            print(board["second_row"])
            print(board["third_row"])
            choosing = False
        elif row_choice == "3" and board["third_row"][pick] == "___":
            board["third_row"][pick] = "_X_"
            print(board["first_row"])
            print(board["second_row"])
            print(board["third_row"])
            choosing = False
        else:
            print("Try again.")

def player_2_choosing():
    choosing = True
    while choosing:
        row_choice = innput("Player 2, which row would you like to play? '1', '2', or '3': ")
        collum_choice = input("Player 2, collum would you like to play? '1', '2', or '3': ")
        collum_choice = int(collum_choice)
        pick = collum_choice - 1
        if row_choice == "1" and board["first_row"][pick] == "___":
            board["first_row"][pick] = "_O_"
            print(board["first_row"])
            print(board["second_row"])
            print(board["third_row"])
            choosing = False
        elif row_choice == "2" and board["second_row"][pick] == "___":
            board["second_row"][pick] = "_O_"
            print(board["first_row"])
            print(board["second_row"])
            print(board["third_row"])
            choosing = False
        elif row_choice == "3" and board["third_row"][pick] == "___":
            board["third_row"][pick] = "_O_"
            print(board["first_row"])
            print(board["second_row"])
            print(board["third_row"])
            choosing = False
        else:
            print("Try again.")

def computer_choice():
    print("Computer's turn...")
    time.sleep(1)
    computer_playing = True
    computer_row = random.randint(0,2) #'[_0_','_1_','_2_']
    computer_collum = random.randint(0,2)
    print(computer_row, computer_collum)
    
    while computer_playing:
        if computer_row == 0:
            if board["first_row"][computer_collum] == "___":
                board["first_row"][computer_collum] = "_O_"
                computer_playing = False
            else:
                computer_row = random.randint(0,2)
                computer_collum = random.randint(0,2)
        if computer_row == 1:
            if board["second_row"][computer_collum] == "___":
                board["second_row"][computer_collum] = "_O_"
                computer_playing = False
            else:
                computer_row = random.randint(0,2)
                computer_collum = random.randint(0,2)
        if computer_row == 2:
            if board["third_row"][computer_collum] == "___":
                board["third_row"][computer_collum] = "_O_"
                computer_playing = False
            else:
                computer_row = random.randint(0,2)
                computer_collum = random.randint(0,2)
    print(board["first_row"])
    print(board["second_row"])
    print(board["third_row"])


def check_win_x():
    global game_running
    #horizontal wins
    if board["first_row"] == ["_X_", "_X_","_X_"]: 
        print("X wins!")
        game_running = False
        time.sleep(3)
        quit()
    if board["second_row"] == ["_X_", "_X_","_X_"]:
        print("X wins!")
        game_running = False
        time.sleep(3)
        quit()
    if board["third_row"] == ["_X_", "_X_","_X_"]:
        print("X wins!")
        game_running = False
        time.sleep(3)
        quit()
    #virtical wins
    if board["first_row"][0] == "_X_" and board["second_row"][0] == "_X_" and board["third_row"][0] == "_X_":
        print("X wins!")
        game_running = False
        time.sleep(3)
        quit()
    if board["first_row"][1] == "_X_" and board["second_row"][1] == "_X_" and board["third_row"][1] == "_X_":
        print("X wins!")
        game_running = False
        time.sleep(3)
        quit()
    if board["first_row"][2] == "_X_" and board["second_row"][2] == "_X_" and board["third_row"][2] == "_X_":
        print("X wins!")
        game_running = False
        time.sleep(3)
        quit()
    #diagonal wins
    if board["first_row"][0] == "_X_" and board["second_row"][1] == "_X_" and board["third_row"][2] == "_X_":
        print("X wins!")
        game_running = False
        time.sleep(3)
        quit()
    if board["first_row"][2] == "_X_" and board["second_row"][1] == "_X_" and board["third_row"][0] == "_X_":
        print("X wins!")
        game_running = False
        time.sleep(3)
        quit()

def check_win_o():
    global game_running
    #horizontal wins
    if board["first_row"] == ["_O_", "_O_","_O_"]: 
        print("O wins!")
        game_running = False
        time.sleep(3)
        quit()
    if board["second_row"] == ["_O_", "_O_","_O_"]:
        print("O wins!")
        game_running = False
        time.sleep(3)
        quit()
    if board["third_row"] == ["_O_", "_O_","_O_"]:
        print("O wins!")
        game_running = False
        time.sleep(3)
        quit()
    #virtical wins
    if board["first_row"][0] == "_O_" and board["second_row"][0] == "_O_" and board["third_row"][0] == "_O_":
        print("O wins!")
        game_running = False
        time.sleep(3)
        quit()
    if board["first_row"][1] == "_O_" and board["second_row"][1] == "_O_" and board["third_row"][1] == "_O_":
        print("O wins!")
        game_running = False
        time.sleep(3)
        quit()
    if board["first_row"][2] == "_O_" and board["second_row"][2] == "_O_" and board["third_row"][2] == "_O_":
        print("O wins!")
        game_running = False
        time.sleep(3)
        quit()
    #diagonal wins
    if board["first_row"][0] == "_O_" and board["second_row"][1] == "_O_" and board["third_row"][2] == "_O_":
        print("O wins!")
        game_running = False
        time.sleep(3)
        quit()
    if board["first_row"][2] == "_O_" and board["second_row"][1] == "_O_" and board["third_row"][0] == "_O_":
        print("O wins!")
        game_running = False
        time.sleep(3)
        quit()


start_question = input("Would you like to play against the computer or play another person. 'computer' or 'two player': ")
if start_question == "computer":
    print(board["first_row"])
    print(board["second_row"])
    print(board["third_row"])

    game_running = True
    #while game_running:
    for i in range (0,4):
        player_choosing()
        check_win_x()
        time.sleep(0.5)
        computer_choice()
        check_win_o()
        time.sleep(0.5)
    print("tie game")
    time.sleep(3)
    quit()

if start_question == "two player":
    print(board["first_row"])
    print(board["second_row"])
    print(board["third_row"])
    game_running = True
    for i in range (0,5):
        player_choosing()
        check_win_x()
        time.sleep(0.5)
        player_2_choosing()
        check_win_o()
        time.sleep(0.5)
    print("Tie game.")
    time.sleep(3)
    quit()
    
else:
    print("see ya later")
