# This is a simple game of Tic-Tac-Toe

from random import randint


def display_board(x):
    '''Prints the board, including the input from a LIST(x) into the required squares'''
    print(' ')
    for i in range(1, 8, 3):
        if i != 1:
            print(' '*30,'-----+-----+-----')
        print(' '*30,'     |     |     ')
        print(' '*30,'  {}  |  {}  |  {}  '.format(x[i], x[i + 1], x[i + 2]))
        print(' '*30,'     |     |     ')
    print(' ')


def player_input():
    p1 = None
    '''Takes the input from the player, asking if they want to play as X or O'''
    while p1 != 'X' and p1 != 'O':
        p1 = (str(input('Player one, please pick if you want to be X or O\n'))).upper()

    if p1 == 'X':
        p2 = 'O'
    else:
        p2 = 'X'

    return p1, p2



def converted_player_choice(x):
    c = ['0', '7', '8', '9', '4', '5', '6', '1', '2', '3']
    x = c[x]
    return int(x)


def p1_place_marker(x):
    global list_to_board
    global player_active

    player_active = x

    player_choice = int(input('\nPlayer 1, place your {}\n'.format(player_one_marker)))
    if is_space_empty(player_choice):

        if player_choice in range(1,10):

            list_to_board[converted_player_choice(player_choice)] = player_one_marker
            clear_screen()
            display_board(list_to_board)
        else:
            print('That is not a valid choice')


def win_check(ltc):

    if 'XXX' == ''.join(ltc[1:4]) or 'OOO' == ''.join(ltc[1:4]):
        print('Winner winner chicken dinner for player {}!'.format(player_active))
        return True
    elif 'XXX' == ''.join(ltc[4:7]) or 'OOO' == ''.join(ltc[4:7]):
        print('A winrar is you, player {}'.format(player_active))
        return True
    elif 'XXX' == ''.join(ltc[7:]) or 'OOO' == ''.join(ltc[7:]):
        print('player {}, you won'.format(player_active))
        return True
    elif 'XXX' == ''.join(ltc[1::3]) or 'OOO' == ''.join(ltc[1::3]):
        print('player {}, you beast'.format(player_active))
        return True
    elif 'XXX' == ''.join(ltc[2::3]) or 'OOO' == ''.join(ltc[2::3]):
        print('player {}, you got that right'.format(player_active))
        return True
    elif 'XXX' == ''.join(ltc[3::3]) or 'OOO' == ''.join(ltc[3::3]):
        print('player {}, is the winner!'.format(player_active))
        return True
    elif 'XXX' == ''.join(ltc[1::4]) or 'OOO' == ''.join(ltc[1::4]):
        print('player {}, you got three in a row!'.format(player_active))
        return True
    elif 'XXX' == ''.join(ltc[3:8:2]) or 'OOO' == ''.join(ltc[3:8:2]):
        print('player {}, on the angle!'.format(player_active))
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


def is_space_empty(stc):
    return list_to_board[converted_player_choice(stc)] == ' '


def full_board_check():
    if ' ' not in list_to_board[1:]:
        print('This board is full guys, you drew... a full board')
        return True
    else:
        return False


def replay():
    x = str(input('\nType "Y" to play again?'))
    if x.upper() == 'Y':
        return True
    else:
        print('Thanks for playing')
        return False


def clear_screen():
    print('\n '*5)


game_running = True

while game_running == True:
    blank_board = ['#', 'T', 'I', 'C', 'T', 'A', 'C', 'T', 'O', 'E']
    list_to_board = [' '] * 10
    numbered_board = ['#',7,8,9,4,5,6,1,2,3]

    clear_screen()

    print('\nWelcome to extreme TIC TAC TOE')

    display_board(blank_board)

    player_one_marker, player_two_marker = player_input()

    clear_screen()
    print("\nYou're choice is {}\nPlayer two is {}".format(player_one_marker, player_two_marker))

    player_active = choose_first()

    display_board(numbered_board)

    while win_check(list_to_board) == False:
        if full_board_check() == False:

            p1_place_marker()

        else:
            clear_screen()
            display_board(list_to_board)
            print('that space is already taken')
            break


        if full_board_check() == False:

            p2_place_marker()

        else:
            clear_screen()
            display_board(list_to_board)
            print('that space is already taken')
            break
    else:
        break


game_running = replay()
