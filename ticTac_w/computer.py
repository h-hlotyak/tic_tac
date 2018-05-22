import random
import time

board = {
    "first_row": ["___", "___","___"],
    "second_row": ["___","___","___"],
    "third_row": ["___","___","___"]
    }



x_count = 0
o_count = 0
got_one = False

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
        row_choice = input("Player 2, which row would you like to play? '1', '2', or '3': ")
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
    print("Thinking...")
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

def computer_win_rows():
    o_count = 0
    empty_count = 0
    looking = True

    while looking:
        # check the first row
        for spot in board["first_row"]:
            if spot == "_O_":  # if the spot is an 'O' then add 1
                o_count = o_count + 1
            if spot == "___":  # if the sport is empty add 1 to empty count
                empty_count = empty_count + 1
            else:
                pass
        if o_count == 2 and empty_count == 1:  # if there are 2 'O's and 1 empty
            for spot in board["first_row"]:  # find the empty spot
                if spot == "___":
                    spot = "_O_"  # change it to an 'o'
                    looking = False  # end while loop
                else:  # if the spot isnt empty, pass
                    pass

        o_count = 0
        empty_count = 0

        # check second row
        for spot in board["second_row"]:
            if spot == "_O_":  # if the spot is an 'O' then add 1
                o_count = o_count + 1
            if spot == "___":  # if the sport is empty add 1 to empty count
                empty_count = empty_count + 1
            else:
                pass
        if o_count == 2 and empty_count == 1:  # if there are 2 'O's and 1 empty
            for spot in board["second_row"]:  # find the empty spot
                if spot == "___":
                    spot = "_O_"  # change it to an 'o'
                    looking = False  # end while loop
                else:  # if the spot isnt empty, pass
                    pass

    o_count = 0
    empty_count = 0

    # check third row
    for spot in board["third_row"]:
        if spot == "_O_":  # if the spot is an 'O' then add 1
            o_count = o_count + 1
        if spot == "___":  # if the sport is empty add 1 to empty count
            empty_count = empty_count + 1
        else:
            pass
    if o_count == 2 and empty_count == 1:  # if there are 2 'O's and 1 empty
        for spot in board["third_row"]:  # find the empty spot
            if spot == "___":
                spot = "_O_"  # change it to an 'o'
                looking = False  # end while loop
            else:  # if the spot isnt empty, pass
                pass

    o_count = 0
    empty_count = 0

    looking = False

def computer_win_collums():
    o_count = 0
    empty_count = 0
    looking = True

    while looking:
        # check first collum
        top_space = board["first_row"][0]
        middle_space = board["second_row"][0]
        bottom_space = board["third_row"][0]

        if top_space == "_O_":  # checks if there is an o
            o_count = o_count + 1  # add 1
        if top_space == "___":  # checks if empty
            empty_count = empty_count + 1  # add 1
        else:
            pass

        if middle_space == "_O_":  # checks if there is an o
            o_count = o_count + 1  # add 1
        if middle_space == "___":  # checks if empty
            empty_count = empty_count + 1  # add 1
        else:
            pass

        if bottom_space == "_O_":  # checks if there is an o
            o_count = o_count + 1  # add 1
        if bottom_space == "___":  # checks if empty
            empty_count = empty_count + 1  # add 1
        else:
            pass

        if o_count == 2 and empty_count == 1:  # if thers 2 o's and an empty spot,  find the empty spot
            if top_space == "___":
                board["first_row"][0] = "_O_"  # and change it to an 'o'
            if middle_space == "___":
                board["second_row"][0] = "_O_"
            if bottom_space == "___":
                board["third_row"][0] = "_O_"
            looking = False

        o_count = 0
        empty_count = 0

        # second collum
        top_space = board["first_row"][1]
        middle_space = board["second_row"][1]
        bottom_space = board["third_row"][1]

        if top_space == "_O_":  # checks if there is an o
            o_count = o_count + 1  # add 1
        if top_space == "___":  # checks if empty
            empty_count = empty_count + 1  # add 1
        else:
            pass

        if middle_space == "_O_":  # checks if there is an o
            o_count = o_count + 1  # add 1
        if middle_space == "___":  # checks if empty
            empty_count = empty_count + 1  # add 1
        else:
            pass

        if bottom_space == "_O_":  # checks if there is an o
            o_count = o_count + 1  # add 1
        if bottom_space == "___":  # checks if empty
            empty_count = empty_count + 1  # add 1
        else:
            pass

        if o_count == 2 and empty_count == 1:  # if thers 2 o's and an empty spot,  find the empty spot
            if top_space == "___":
                board["first_row"][1] = "_O_"  # and change it to an 'o'
            if middle_space == "___":
                board["second_row"][1] = "_O_"
            if bottom_space == "___":
                board["third_row"][1] = "_O_"
            looking = False

        o_count = 0
        empty_count = 0

        # third collum
        top_space = board["first_row"][2]
        middle_space = board["second_row"][2]
        bottom_space = board["third_row"][2]

        if top_space == "_O_":  # checks if there is an o
            o_count = o_count + 1  # add 1
        if top_space == "___":  # checks if empty
            empty_count = empty_count + 1  # add 1
        else:
            pass

        if middle_space == "_O_":  # checks if there is an o
            o_count = o_count + 1  # add 1
        if middle_space == "___":  # checks if empty
            empty_count = empty_count + 1  # add 1
        else:
            pass

        if bottom_space == "_O_":  # checks if there is an o
            o_count = o_count + 1  # add 1
        if bottom_space == "___":  # checks if empty
            empty_count = empty_count + 1  # add 1
        else:
            pass

        if o_count == 2 and empty_count == 1:  # if thers 2 o's and an empty spot,  find the empty spot
            if top_space == "___":
                board["first_row"][2] = "_O_"  # and change it to an 'o'
            if middle_space == "___":
                board["second_row"][2] = "_O_"
            if bottom_space == "___":
                board["third_row"][2] = "_O_"
            looking = False

        o_count = 0
        empty_count = 0
        looking = False

def computer_win_diagonal():
    o_count = 0
    empty_count = 0
    # first diagonal
    '''
    O
        O
            O
    '''
    top_left = board["first_row"][0]
    middle = board["second_row"][1]
    bottom_right = board["third_row"][2]

    if top_left == "_O_":
        o_count = o_count + 1
    if top_left == "___":
        empty_count = empty_count + 1
    if middle == "_O_":
        o_count = o_count + 1
    if middle == "___":
        empty_count = empty_count + 1
    if bottom_right == "_O_":
        o_count = o_count + 1
    if bottom_right == "___":
        empty_count = empty_count + 1
    else:
        pass

    if o_count == 2 and empty_count == 1:
        if top_left == "___":
            board["first_row"][0] = "_O_"
        if middle == "___":
            board["second_row"][1] = "_O_"
        if bottom_right == "___":
            board["third_row"][2] = "_O_"

    o_count = 0
    empty_count = 0

    # second diagonal
    '''     O
        O
    O
    '''

    top_right = board["first_row"][2]
    middle = board["second_row"][1]
    bottom_left = board["third_row"][0]

    if top_right == "_O_":
        o_count = o_count + 1
    if top_right == "___":
        empty_count = empty_count + 1
    if middle == "_O_":
        o_count = o_count + 1
    if middle == "___":
        empty_count = empty_count + 1
    if bottom_left == "_O_":
        o_count = o_count + 1
    if bottom_left == "___":
        empty_count = empty_count + 1
    else:
        pass

    if o_count == 2 and empty_count == 1:
        if top_right == "___":
            board["first_row"][2] = "_O_"
        if middle == "___":
            board["second_row"][1] = "_O_"
        if bottom_left == "___":
            board["second_row"][0] = "_O_"

    o_count = 0
    empty_count = 0

def computer_block_rows():
    """
        check for X immediate win to block
        """

        # check the first row
        for spot in board["first_row"]:
            if spot == "_X_":  # if the spot is an 'O' then add 1
                x_count = x_count + 1
            if spot == "___":  # if the sport is empty add 1 to empty count
                empty_count = empty_count + 1
            else:
                pass
        if x_count == 2 and empty_count == 1:  # if there are 2 'O's and 1 empty
            for spot in board["first_row"]:  # find the empty spot
                if spot == "___":
                    spot = "_O_"  # change it to an 'o'
                    computer_check_immediate_win = False  # end while loop
                else:  # if the spot isnt empty, pass
                    pass

        x_count = 0
        empty_count = 0

        # check the second row
        for spot in board["second_row"]:
            if spot == "_X_":  # if the spot is an 'O' then add 1
                x_count = x_count + 1
            if spot == "___":  # if the sport is empty add 1 to empty count
                empty_count = empty_count + 1
            else:
                pass
        if x_count == 2 and empty_count == 1:  # if there are 2 'O's and 1 empty
            for spot in board["second_row"]:  # find the empty spot
                if spot == "___":
                    spot = "_O_"  # change it to an 'o'
                    computer_check_immediate_win = False  # end while loop
                else:  # if the spot isnt empty, pass
                    pass

        x_count = 0
        empty_count = 0

         #check third row

        for spot in board["third_row"]:
            if spot == "_X_":  # if the spot is an 'O' then add 1
                x_count = x_count + 1
            if spot == "___":  # if the sport is empty add 1 to empty count
                empty_count = empty_count + 1
            else:
                pass
        if x_count == 2 and empty_count == 1:  # if there are 2 'O's and 1 empty
            for spot in board["third_row"]:  # find the empty spot
                if spot == "___":
                    spot = "_O_"  # change it to an 'o'
                    computer_check_immediate_win = False  # end while loop
                else:  # if the spot isnt empty, pass
                    pass

        x_count = 0
        empty_count = 0

def computer_block_collums():
     # checking collums for block

        # first collum
        top_space = board["first_row"][0]
        middle_space = board["second_row"][0]
        bottom_space = board["third_row"][0]

        if top_space == "_X_":  # checks if there is an o
            x_count = x_count + 1  # add 1
        if top_space == "___":  # checks if empty
            empty_count = empty_count + 1  # add 1
        else:
            pass

        if middle_space == "_X_":  # checks if there is an o
            x_count = x_count + 1  # add 1
        if middle_space == "___":  # checks if empty
            empty_count = empty_count + 1  # add 1
        else:
            pass

        if bottom_space == "_X_":  # checks if there is an o
            x_count = x_count + 1  # add 1
        if bottom_space == "___":  # checks if empty
            empty_count = empty_count + 1  # add 1
        else:
            pass

        if x_count == 2 and empty_count == 1:  # if thers 2 o's and an empty spot,  find the empty spot
            if top_space == "___":
                board["first_row"][0] = "_O_"  # and change it to an 'o'
            if middle_space == "___":
                board["second_row"][0] = "_O_"
            if bottom_space == "___":
                board["third_row"][0] = "_O_"
            computer_check_immediate_win = False

        x_count = 0
        empty_count = 0

        # second collum
        top_space = board["first_row"][1]
        middle_space = board["second_row"][1]
        bottom_space = board["third_row"][1]

        if top_space == "_X_":  # checks if there is an o
            x_count = x_count + 1  # add 1
        if top_space == "___":  # checks if empty
            empty_count = empty_count + 1  # add 1
        else:
            pass

        if middle_space == "_X_":  # checks if there is an o
            x_count = x_count + 1  # add 1
        if middle_space == "___":  # checks if empty
            empty_count = empty_count + 1  # add 1
        else:
            pass

        if bottom_space == "_X_":  # checks if there is an o
            x_count = x_count + 1  # add 1
        if bottom_space == "___":  # checks if empty
            empty_count = empty_count + 1  # add 1
        else:
            pass

        if x_count == 2 and empty_count == 1:  # if thers 2 o's and an empty spot,  find the empty spot
            if top_space == "___":
                board["first_row"][1] = "_O_"  # and change it to an 'o'
            if middle_space == "___":
                board["second_row"][1] = "_O_"
            if bottom_space == "___":
                board["third_row"][1] = "_O_"
            computer_check_immediate_win = False

        x_count = 0
        empty_count = 0

        # third collum
        top_space = board["first_row"][2]
        middle_space = board["second_row"][2]
        bottom_space = board["third_row"][2]

        if top_space == "_X_":  # checks if there is an o
            x_count = x_count + 1  # add 1
        if top_space == "___":  # checks if empty
            empty_count = empty_count + 1  # add 1
        else:
            pass

        if middle_space == "_X_":  # checks if there is an o
            x_count = x_count + 1  # add 1
        if middle_space == "___":  # checks if empty
            empty_count = empty_count + 1  # add 1
        else:
            pass

        if bottom_space == "_X_":  # checks if there is an o
            x_count = x_count + 1  # add 1
        if bottom_space == "___":  # checks if empty
            empty_count = empty_count + 1  # add 1
        else:
            pass

        if x_count == 2 and empty_count == 1:  # if thers 2 o's and an empty spot,  find the empty spot
            if top_space == "___":
                board["first_row"][2] = "_O_"  # and change it to an 'o'
            if middle_space == "___":
                board["second_row"][2] = "_O_"
            if bottom_space == "___":
                board["third_row"][2] = "_O_"
            computer_check_immediate_win = False

        x_count = 0
        empty_count = 0

def computer_block_diagonal():

        #diagonals
        '''
        X
            X
                X
        '''
        top_space = board["first_row"][0]
        middle_space = board["second_row"][1]
        bottom_space = board["third_row"][2]

        if top_space == "_X_":
            x_count = x_count + 1
        if top_space == "___":
            empty_count = empty_count + 1

        if middle_space == "_X_":
            x_count = x_count + 1
        if middle_space == "___":
            empty_count = empty_count + 1

        if bottom_space == "_X_":
            x_count = x_count + 1
        if bottom_space == "___":
            empty_count = empty_count + 1

        if x_count == 2 and empty_count == 1:
            if top_space == "___":
                board["first_row"][0] = "_O_"
            if middle_space == "___":
                board["second_row"][1] = "_O_"
            if bottom_space == "___":
                board["third_row"][2] = "_O_"
            computer_check_immediate_win = False

        x_count = 0
        empty_count = 0

        """
                X
            X
        X
        """
        top_space = board["first_row"][2]
        middle_space = board["second_row"][1]
        bottom_space = board["third_row"][0]

        if top_space == "_X_":
            x_count = x_count + 1
        if top_space == "___":
            empty_count = empty_count + 1

        if middle_space == "_X_":
            x_count = x_count + 1
        if middle_space == "___":
            empty_count = empty_count + 1

        if bottom_space == "_X_":
            x_count = x_count + 1
        if bottom_space == "___":
            empty_count = empty_count + 1

        if x_count == 2 and empty_count == 1:
            if top_space == "___":
                board["first_row"][2] = "_O_"
            if middle_space == "___":
                board["second_row"][1] = "_O_"
            if bottom_space == "___":
                board["third_row"][0] = "_O_"
            computer_check_immediate_win = False

        x_count = 0
        empty_count = 0




def computer_smart_choice():

    # priorities
    # 1: check if computer has immediate win
    # 2: check if player has immediate win (to block)
    # 3: check if computer can force win (2 winning paths)
    # 4: pick random spot

    x_count = 0
    o_count = 0
    empty_count = 0
    computer_check_immediate_win = True
    got_one = False

    print("Computer's turn...")
    time.sleep(1)

    #immediate win
    #must check if there is 2 'O's in a row with an empty spot
    #if there is then place the last 'O' there
    computer_win_rows()
    
    computer_win_collums()

    computer_win_diagonal()

    #can block?

    computer_block_rows()

    computer_block_collums()

    computer_block_diagonal()

        
      

    




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
        computer_smart_choice()
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
