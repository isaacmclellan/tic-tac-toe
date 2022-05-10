import os
import random
import sys

def clear():
    os.system('clear')


def draw_board(board):
    clear()
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')


def input_player_letter():
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        letter = input('Do you want to be X or O? ').upper()
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']


def who_goes_first():
    if random.randint(0, 1) == 0:
        return 'Player 1'
    else:
        return 'Player 2'


def play_again():
    return input('Do you want to play again? (y/n) ').lower().startswith('y')




def make_move(board, letter, move):
    board[move] = letter


def is_winner(board, letter):
    return ((board[7] == letter and board[8] == letter and board[9] == letter) or
            (board[4] == letter and board[5] == letter and board[6] == letter) or
            (board[1] == letter and board[2] == letter and board[3] == letter) or
            (board[7] == letter and board[4] == letter and board[1] == letter) or
            (board[8] == letter and board[5] == letter and board[2] == letter) or
            (board[9] == letter and board[6] == letter and board[3] == letter) or
            (board[7] == letter and board[5] == letter and board[3] == letter) or
            (board[9] == letter and board[5] == letter and board[1] == letter))


def get_board_copy(board):
    return board[:]


def is_space_free(board, move):
    return board[move] == ' '


def get_player_move(board):
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not is_space_free(board, int(move)):
        move = input('What is your next move? (1-9) ')
    return int(move)






def choose_random_move_from_list(board, moves_list):
    possible_moves = []
    for i in moves_list:
        if is_space_free(board, i):
            possible_moves.append(i)
    if len(possible_moves) != 0:
        return random.choice(possible_moves)
    else:
        return None


def get_computer_move(board, computer_letter):
    if computer_letter == 'X':
        player_letter = 'O'
    else:
        player_letter = 'X'

    # check if computer can win
    for i in range(1, 10):
        copy = get_board_copy(board)
        if is_space_free(copy, i):
            make_move(copy, computer_letter, i)
            if is_winner(copy, computer_letter):
                return i

    # check if player can win
    for i in range(1, 10):
        copy = get_board_copy(board)
        if is_space_free(copy, i):
            make_move(copy, player_letter, i)
            if is_winner(copy, player_letter):
                return i

    # check if center is free
    if is_space_free(board, 5):
        return 5

    # check if corners are free
    move = choose_random_move_from_list(board, [1, 3, 7, 9])
    if move != None:
        return move


    # check if sides are free
    return choose_random_move_from_list(board, [2, 4, 6, 8])


def is_board_full(board):
    for i in range(1, 10):
        if is_space_free(board, i):
            return False
    return True


def play_game():
    print('Welcome to Tic Tac Toe!')
    while True:
        the_board = [' '] * 10
        player_letter, computer_letter = input_player_letter()
        turn = who_goes_first()
        print(turn + ' will go first.')
        game_is_playing = True

        while game_is_playing:
            if turn == 'Player 1':
                draw_board(the_board)
                move = get_player_move(the_board)
                make_move(the_board, player_letter, move)
                if is_winner(the_board, player_letter):
                    draw_board(the_board)
                    print('You have won the game!')
                    game_is_playing = False
                else:
                    if is_board_full(the_board):
                        draw_board(the_board)
                        print('The game is a tie!')
                        break
                    else:
                        turn = 'Player 2'
            else:
                move = get_computer_move(the_board, computer_letter)
                make_move(the_board, computer_letter, move)
                if is_winner(the_board, computer_letter):
                    draw_board(the_board)



                    print('The computer has beaten you! You lose.')
                    game_is_playing = False
                else:
                    if is_board_full(the_board):
                        draw_board(the_board)
                        print('The game is a tie!')
                        break
                    else:
                        turn = 'Player 1'

        if not play_again():
            break


play_game()
input('Press Enter to exit')
clear()
sys.exit()
