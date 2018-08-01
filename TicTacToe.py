# This is a simple game of Tic-Tac-Toe

from random import randint


def display_board(x):
    '''Prints the board, including the input from a LIST(x) into the required squares'''
    print(' ')
    for i in range(1, 8, 3):
        if i != 1:
            print('-----+-----+-----')
        print('     |     |     ')
        print('  {}  |  {}  |  {}  '.format(x[i], x[i + 1], x[i + 2]))
        print('     |     |     ')
    print(' ')


def player_one_input():
    '''Takes the input from the player, asking if they want to play as X or O'''

    i = None
    while i != 'X' and i != 'O':
        i = (str(input('Player one, please pick if you want to be X or O\n'))).upper()
    return i


def player_two_calc(p1):
    if p1 == 'X':
        p2 = 'O'
    elif p1 == 'O':
        p2 = 'X'
    return p2


def converted_player_choice(x):
    c = ['0', '7', '8', '9', '4', '5', '6', '1', '2', '3']
    x = c[x]
    return int(x)


def place_marker():
    global list_to_board
    global player_active

    while win_check(list_to_board) is False:

        if player_active == 1:
            marker = player_one_marker
        elif player_active == 2:
            marker = player_two_marker

        player_choice = int(input('\nPlayer {}, place your {}\n'.format(player_active, marker)))

        list_to_board[converted_player_choice(player_choice)] = marker
        display_board(list_to_board)

        if player_active == 1:
            player_active = 2

        elif player_active == 2:
            player_active = 1


def win_check(ltc):
    if 'XXX' in ''.join(ltc[1:4]):
        print('Winner winner chicken dinner for player {}!'.format(player_active))
        return True
    elif 'XXX' in ''.join(ltc[4:7]):
        print('A winrar is you, player{}'.format(player_active))
        return True
    elif 'XXX' in ''.join(ltc[7:]):
        print('player{}, you won'.format(player_active))
        return True
    elif 'XXX' in ''.join(ltc[1::3]):
        print('player{}, you beast'.format(player_active))
        return True
    elif 'XXX' in ''.join(ltc[2::3]):
        print('player{}, you got that right'.format(player_active))
        return True
    elif 'XXX' in ''.join(ltc[1::4]):
        print('player{}, you got that right'.format(player_active))
        return True
    elif 'XXX' in ''.join(ltc[3:8:2]):
        print('player{}, you got that right'.format(player_active))
        return True
    else:
        return False


def choose_first():
    x = randint(0, 10)
    if x <= 5:
        print('Player one goes first')
        return 1
    else:
        print('Player two goes first')
        return 2


def space_full_check(stc):
    return list_to_board[stc] == ' '


def full_board_check():
    if ' ' not in list_to_board[1:]:
        print('This board is full guys')
        return True
    else:
        return False


def player_choice_func(x):
    if space_full_check(x) == True:
        print("That space is already taken, please don't cheat")
    else:
        return x


def replay():
    x = str(input('Type "Y" to play again?'))
    if x.upper() == 'Y':
        return True
    else:
        print('Thanks for playing')
        return False


# test_board = ['#','X','O','X','O','X','O','X','O','X']

game_running = True

# print(win_check(test_board))
while game_running == True:
    blank_board = [' '] * 10
    list_to_board = [' '] * 10

    print('Welcome to extreme TIC TAC TOE ')

    display_board(blank_board)

    player_one_marker = player_one_input()
    player_two_marker = player_two_calc(player_one_marker)

    print("\nYou're choice is {}\nPlayer two is {}".format(player_one_marker, player_two_marker))

    player_active = choose_first()

    place_marker()

    game_running = replay()
