#!/usr/bin/env python3
from movement import *

class chess_board:
  
  board_index=[
        'a8','b8','c8','d8','e8','f8','g8','h8',
        'a7','b7','c7','d7','e7','f7','g7','h7',
        'a6','b6','c6','d6','e6','f6','g6','h6',
        'a5','b5','c5','d5','e5','f5','g5','h5',
        'a4','b4','c4','d4','e4','f4','g4','h4',
        'a3','b3','c3','d3','e3','f3','g3','h3',
        'a2','b2','c2','d2','e2','f2','g2','h2',
        'a1','b1','c1','d1','e1','f1','g1','h1',
        ]
  ####################################################################
  def __init__(self, input_board,player):
        self.init(input_board,player)
        
  ####################################################################
  def init(self, input_board,player):
        #Set 64 piece board
        self.square = [
            piece(),piece(),piece(),piece(),piece(),piece(),piece(),piece(),
            piece(),piece(),piece(),piece(),piece(),piece(),piece(),piece(),
            piece(),piece(),piece(),piece(),piece(),piece(),piece(),piece(),
            piece(),piece(),piece(),piece(),piece(),piece(),piece(),piece(),
            piece(),piece(),piece(),piece(),piece(),piece(),piece(),piece(),
            piece(),piece(),piece(),piece(),piece(),piece(),piece(),piece(),
            piece(),piece(),piece(),piece(),piece(),piece(),piece(),piece(),
            piece(),piece(),piece(),piece(),piece(),piece(),piece(),piece()
            ]
            
        if (player=='w') :
            self.current_player='white'
        else:
            self.current_player='black'
  #Set board as per user input`          
        self.setboard(input_board)

  ####################################################################
  def setboard(self,input_board):
       
  #Set board as per user input
        in_board=input_board
        
        if(len(in_board)!=64):
            print('Error : Something wrong ')
            return False
                
        # Setting pieces
        i=63
        for c in in_board:
            if(c=='k'):
                self.square[i]=piece('Kingfisher','black')
                i=i-1
            elif(c=='q'):
                self.square[i]=piece('Quetzal','black')
                i=i-1
            elif(c=='r'):
                self.square[i]=piece('Robin','black')
                i=i-1
            elif(c=='n'):
                self.square[i]=piece('Nighthawk','black')
                i=i-1
            elif(c=='b'):
                self.square[i]=piece('Blue jay','black')
                i=i-1
            elif(c=='p'):
                self.square[i]=piece('Parakeet','black')
                i=i-1
            elif(c=='K'):
               self.square[i]=piece('Kingfisher','white')
               i=i-1
            elif(c=='Q'):
               self.square[i]=piece('Quetzal','white')
               i=i-1
            elif(c=='R'):
                self.square[i]=piece('Robin','white')
                i=i-1
            elif(c=='N'):
                self.square[i]=piece('Nighthawk','white')
                i=i-1
            elif(c=='B'):
                self.square[i]=piece('Blue jay','white')
                i=i-1
            elif(c=='P'):
                self.square[i]=piece('Parakeet','white')
                i=i-1
            else:
                i=i-1
	       
        # Checking number of pieces
        if(i!=-1):
            print('Error : Something wrong ')
            return False
        
        return True

  ####################################################################
  def get_possible_moves(self,color='',check_isattack=False):

  #Get all possible moves for given board  
        if(color==''):
            color=self.current_player
            
        moves_list=[]
        for position1,piece in enumerate(self.square):
            # piece color is not the wanted or empty piece
            if piece.color!=color:
                continue
            
            if(piece.name=='Kingfisher'): #Kingfisher
                moves_list+=piece.king_moves(position1,self.opposite_color(color),self)
                continue
            elif(piece.name=='Quetzal'): # Quetzal 
                moves_list+=piece.quetzal_moves(position1,self.opposite_color(color),self)
                continue
            elif(piece.name=='Robin'): # Robin
                moves_list+=piece.robin_moves(position1,self.opposite_color(color),self)
                continue
            elif(piece.name=='Nighthawk'): # Nighthawk
                moves_list+=piece.nighthawk_moves(position1,self.opposite_color(color),self)
                continue
            elif(piece.name=='Blue jay'): # Blue Jay
                moves_list+=piece.blue_jay_moves(position1,self.opposite_color(color),self)
                continue
            if(piece.name=='Parakeet'): # Parakeet
                moves_list+=piece.parakeet_moves(position1,piece.color,self)
                continue
            
        return moves_list
            
  ##############################################################################
  def opposite_color(self,c):
        #Get Opposition player color who is not making move
        if(c=='black'):
            return 'white'
        else:
            return 'black'           

  ####################################################################    
  def make_move(self,start,end,promote):

		#Make move 
        self.square[end]=self.square[start]
        self.square[start]=piece()
                
        if(promote!=''):
            if(promote=='q'):
                self.square[end]=piece('Quetzal',self.current_player)

        # Change player who will make next move
        self.change_player()
            
        return True
        
  ####################################################################
  def change_player(self):
        # Change player who will make next move
        
        if(self.current_player=='black'):
            self.current_player='white'
        else:
            self.current_player='black'   
  ####################################################################
  def heuristic_evaluator(self):
                
        value_black=0
        value_white=0
		 # iterating the board pieces 
        for position1,piece in enumerate(self.square):

            if(piece.color=='white'):
                value_white+=piece.value
            else: 
                value_black+=piece.value

        if(self.current_player=='white'):
            return value_white-value_black
        else:
            return value_black-value_white

  #########################################################################
  def check_threat(self,position,color):
        #Check threat for Kingfisher
        moves_list=self.get_possible_moves(color,True)
        for start_pos,end_pos,promote in moves_list:
            if(end_pos==position):
                return True
        
        return False    
  
  ##########################################################################
  def king_in_danger(self,color):
        #Check of Kingfisher can be captured
        flg=0  
        for i in range(0,64):
            if(self.square[i].name=='Kingfisher' and self.square[i].color==color):
                position=i
                flg=1
                break
            
        if flg==1:
            return self.check_threat(position,self.opposite_color(color))
        else:
            return True

  ##########################################################################
  def winning_move(self,moves_list, color):
	
		#Check for current move, if there is any move which will capture 
		#opponent Kingfisher
        opp_color= self.opposite_color(color)
        for i in range(0,64):
            if(self.square[i].name=='Kingfisher' and self.square[i].color==opp_color):
                position=i
                break

        for move in moves_list:
            if(move[1]==position):
                return 1, move
        return 0, None
    
  ####################################################################
  @staticmethod
  def get_row(x):
		#Get Row number given position of square
        return (x >> 3)

  ####################################################################
  @staticmethod
  def get_col(x):
		#Get Column number given position of square
        return (x & 7)
        
  ####################################################################
  def squreno_to_boardindex(self,i):
                
        if(i<0 or i>63):
            print("Error")
            return

        return self.board_index[i] 
    
  ####################################################################
  def boardindex_to_squareno(self,c):
        
        return self.board_index.index(c)
        
 ####################################################################
  
  def display(self) :

	#Function to display board position in 8X8 square board
  
        display_string=self.display_line()
      
      #  print('8',end='   ')
        i=1
        for p in display_string:
            print(p,end='   ')
                                
            if(i%8==0):
                print()
                print()
              
            i+=1
        
        print('Player to make next move : '+self.current_player)
        
  #####################################################################
  
  def display_line(self) :

	#Function to display board position in single line
    board_string=''
    for piece in self.square:
        if(piece.color=='black'):
            board_string+=(piece.name[0].lower())
        else:
            board_string+=(piece.name[0])
                                                             
    board_string=(board_string[::-1])
    print(board_string)
    return(board_string)