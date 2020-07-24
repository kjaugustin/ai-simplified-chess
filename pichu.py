#!/usr/bin/env python3
# Import object classes
import sys
from minimax_alpha_beta import *
from chess_board import *
import time

start_time=time.time()
#Get User inputs 
current_player=sys.argv[1]
input_board=sys.argv[2]
time_limit=sys.argv[3]

c=minimax_alphabeta(start_time, time_limit)
b=chess_board(input_board,current_player)

#Display current board
print("Current Board")
b.display()

#Call Best move function to get best move for given board and make move
print("Thinking! Please wait...")
b1=c.best_move(b)

#Print board after best move made
print("Board after recomended Move")
b1.display()        
b1.display_line()
