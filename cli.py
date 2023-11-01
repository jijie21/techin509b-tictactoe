# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.
from logic import make_empty_board

def get_winner(board):
 for i in range(0, 3):
  if board[i][0] != '' and board[i][0] == board[i][1] == board[i][2]:
   print(board[i][0], ' Won')
   return board[i][0]
  
 for i in range(0, 3):
  if board[0][i] != '' and board[0][i] == board[1][i] == board[2][i]:
   print(board[0][i], ' Won')
   return board[0][i]
  
 if board[1][1] != '' and (board[0][0] == board[1][1] == board[2][2] or board[2][0] == board[1][1] ==board[0][2]):
  print(board[1][1], ' Won')
  return board[1][1]
 for row in board:
  for col in row:
   if col == '':
    return ''
 print('Draw')
 return 'Draw'

def show_board(board):
    for row in board:
        print(row)
  
def input_move(board):
  x = int(input("input row (0-2): "))
  y = int(input("input col (0-2): "))

  if x < 0 or x > 2 or y < 0 or y > 2:
   raise ValueError('invalid')
  if board[x][y] != '':
   raise ValueError('invalid')
  return x, y

def other_player(now):
 if now == 'X':
  next = 'O'
 else:
  next = 'X'
 return next

if __name__ == '__main__':
    board = make_empty_board()
    winner = ''
    player = 'X'
    show_board(board)
    while winner == '':
        print('Next turn: ', player)
        x, y = input_move(board)
        board[x][y] = player
        show_board(board)
        winner = get_winner(board)
        player = other_player(player)
    