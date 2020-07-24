#!/usr/bin/env python3
import time
from copy import deepcopy
from random import shuffle


class minimax_alphabeta:
	
    def __init__(self,start_time, time_limit):
        
        self.INFINITY=float("inf")
		#Set Iteration Depth
        self.init_depth=2 
        self.start_time=start_time
        self.time_limit=time_limit
        
    def alphabeta(self,b,depth,alpha,beta,maximize):
        
        #minimax algorithm with alpha-betasearch
        c_time= time.time()
		
		#Check for time limit
        if(float((c_time-self.start_time)) > (float(self.time_limit) -2)):
            self.time_up_flg=1
            return b.heuristic_evaluator()
        
		#At end of depth
        if(depth==0):
            return b.heuristic_evaluator()
        
		#Check if current move is making out Kingfisher in danger
        king_check=b.king_in_danger(b.current_player)
        if(king_check):
             return(self.INFINITY)
            
        if maximize:
            best_value = self.INFINITY
			#Get possible moves for current board
            moves_list=b.get_possible_moves()
            #Shuffle moves so that moves will be picked randomly rather in sequence
			#This will ensure if there is program end due to time limit, we do not always
			#consider start moves all time
            shuffle(moves_list)
            for move in moves_list:
				#Make temporary copy of current board and make move on new temp board
                b_temp1=deepcopy(b)
                b_temp1.make_move(move[0],move[1],move[2])
                score=self.alphabeta(b_temp1,depth,alpha,beta,False)
                best_value=max(best_value,score)
                alpha=max(alpha,best_value)
                if(alpha>beta):
                    break
            return best_value
        else:
            best_value = self.INFINITY
			#Get possible moves for current board
            moves_list=b.get_possible_moves()
			#Shuffle moves so that moves will be picked randomly rather in sequence
			#This will ensure if there is program end due to time limit, we do not always
			#consider start moves all time
            shuffle(moves_list)
            for move in moves_list:
                b_temp1=deepcopy(b)
                b_temp1.make_move(move[0],move[1],move[2])
                score=self.alphabeta(b_temp1,depth-1,alpha,beta,True)
                best_value=min(best_value,score)
                beta=min(beta,best_value)
                if(alpha>beta):
                    break
            return best_value

        return 0
            
   ####################################################################
    def best_move(self,b):
        
		#Function to get best move for current board
        self.time_up_flg=0
        self.best_move=None
        min_value=self.INFINITY
        min_move=None

        #Get possible moves for current board
        moves_list=b.get_possible_moves()
		#Check from current moves list, if there is any move which will 
		#capture other player's king
        winner_flg, winning_move=  b.winning_move(moves_list,b.current_player)
        if (winner_flg==1) :
            print ("Hurray!!!! Winner!!!!")
            min_move=winning_move
        else :
			#There is no move in current move list which will capture other
			#player's Kingfisher. So We need to iterate each move and identify
			#best move
            shuffle(moves_list)
            for move in moves_list:
                b_temp=deepcopy(b)
                b_temp.make_move(move[0],move[1],move[2])
                value=self.alphabeta(b_temp,self.init_depth,-self.INFINITY,self.INFINITY,False)
                if (value <= min_value and self.time_up_flg ==1 ):
                    #We are out of time, so get best possible move from iterated moves so far
                    min_value = value
                    min_move = move
                    break
                elif (value <= min_value and self.time_up_flg ==0 ):
                    min_value = value
                    min_move = move
       
        best=min_move
        start_posn=best[0]
        end_posn=best[1]
		#Get Row and Column number for start and end position for given move
        start_row=(b.get_row(int(start_posn))^7)
        start_col=(b.get_col(int(start_posn))^7)
        end_row=(b.get_row(int(end_posn))^7)
        end_col=(b.get_col(int(end_posn))^7)
        
        print("I would recommend moving the", b.square[start_posn].name, "at row" ,start_row+1, " column", start_col+1 ,"to row", end_row+1," column " ,end_col+1, "...")
    
		#Make actual move
        b.make_move(min_move[0],min_move[1],min_move[2])
		#Retrun board after move
        return b 

   ########################################################################
