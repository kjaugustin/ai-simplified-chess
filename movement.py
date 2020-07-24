#!/usr/bin/env python3

class piece:
    
    EMPTY='.' # empty piece name (empty square '.' )

    # Name of the pieces
    name_piece=(EMPTY,'Kingfisher','Quetzal','Robin','Nighthawk','Blue jay','Parakeet')
        
    # Give a score value for each piece :
    value_piece=(0,20,9,5,3,3,1)
	
	#Move generation logic is based on "Mailbox" approach
	#Reference: https://chessprogramming.wikispaces.com/10x12+Board
	    
    
    table_120 = (
	-1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
	-1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
	-1,  0,  1,  2,  3,  4,  5,  6,  7, -1,
	-1,  8,  9, 10, 11, 12, 13, 14, 15, -1,
	-1, 16, 17, 18, 19, 20, 21, 22, 23, -1,
	-1, 24, 25, 26, 27, 28, 29, 30, 31, -1,
	-1, 32, 33, 34, 35, 36, 37, 38, 39, -1,
	-1, 40, 41, 42, 43, 44, 45, 46, 47, -1,
	-1, 48, 49, 50, 51, 52, 53, 54, 55, -1,
	-1, 56, 57, 58, 59, 60, 61, 62, 63, -1,
	-1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
	-1, -1, -1, -1, -1, -1, -1, -1, -1, -1
	)
    table_64 = (
	21, 22, 23, 24, 25, 26, 27, 28,
	31, 32, 33, 34, 35, 36, 37, 38,
	41, 42, 43, 44, 45, 46, 47, 48,
	51, 52, 53, 54, 55, 56, 57, 58,
	61, 62, 63, 64, 65, 66, 67, 68,
	71, 72, 73, 74, 75, 76, 77, 78,
	81, 82, 83, 84, 85, 86, 87, 88,
	91, 92, 93, 94, 95, 96, 97, 98
	)
    
    # Moving vectors according to the 'table_64',
    robin_vector=(-10,10,-1,1)
    blue_jay_vector=(-11,-9,11,9)
    nighthawk_vector=(-12,-21,-19,-8,12,21,19,8)
    kingfisher_vector=( -11,-10,-9,-1,1,9,10,11)
    quetzal_vector=( -11,-10,-9,-1,1,9,10,11)
	
    ####################################################################
    def __init__(self,name=EMPTY,color=''):
        
        self.name=name
        self.color=color        
        self.value=self.value_piece[self.name_piece.index(name)]
        
    ####################################################################
	#Check if square is empty
    def isEmpty(self):
        return (self.name==self.EMPTY)
        
    ####################################################################
    def king_moves(self,pos1,opposite_color,chess_b):
	
	#Get all moves for Kingfisher
        list_move=[]
        for i in self.kingfisher_vector:
            n=self.table_120[self.table_64[pos1]+i]
            if(n!=-1):
			#Not outside board as per table_120
                if(chess_b.square[n].isEmpty() or chess_b.square[n].color==opposite_color):
					# Append the move to move list if target square is empty of opposite_color
                    list_move.append((pos1,n,''))
                       
        return list_move
        
    ####################################################################
    def quetzal_moves(self,pos1,opposite_color,chess_b):
    
	#Get all moves for Quetzal
        list_move=[]
        
        for k in self.quetzal_vector:        
            j=1
            while(True):
                n=self.table_120[self.table_64[pos1] + (k * j)]
                if(n!=-1): 
					#Not outside board as per table_120
                    if(chess_b.square[n].isEmpty() or chess_b.square[n].color==opposite_color):
						# Append the move to move list if target square is empty of opposite_color
                        list_move.append((pos1,n,'')) 
                else:
					#Outside board as per table_120
                    break 
                if(not chess_b.square[n].isEmpty()):
					#Target Square is not empty
                    break 
                j=j+1

        return list_move
	####################################################################
    def robin_moves(self,pos1,opposite_color,chess_b):
        
    #Get all moves for Robin
        list_move=[]
        
        for k in self.robin_vector:        
            j=1
            while(True):
                n=self.table_120[self.table_64[pos1] + (k * j)]
                if(n!=-1): 
					#Not outside board as per table_120
                    if(chess_b.square[n].isEmpty() or chess_b.square[n].color==opposite_color):
						# Append the move to move list if target square is empty of opposite_color
                        list_move.append((pos1,n,'')) 
                else:
					#Outside board as per table_120
                    break 
                if(not chess_b.square[n].isEmpty()):
					#Target Square is not empty
                    break 
                j=j+1

        return list_move
        
    ####################################################################
    def blue_jay_moves(self,pos1,opposite_color,chess_b):
        
    #Get all moves for Blue Jay
        list_move=[]
        
        for k in self.blue_jay_vector:
            j=1
            while(True):
                n=self.table_120[self.table_64[pos1] + (k * j)]
                if(n!=-1): 
					# Not outside board as per table_120
                    if(chess_b.square[n].isEmpty() or chess_b.square[n].color==opposite_color):
                        # Append the move to move list if target square is empty of opposite_color
                        list_move.append((pos1,n,'')) 
                else:
					#Outside board as per table_120
                    break 
                if(not chess_b.square[n].isEmpty()):
					#Target Square is not empty
                    break 
                j=j+1

        return list_move
    ####################################################################
    def nighthawk_moves(self,pos1,opposite_color,chess_b):
        
	#Get All moves for Nighthawk
        list_move=[]
        
        for i in self.nighthawk_vector:
            n=self.table_120[self.table_64[pos1]+i]
            if(n!=-1):
				# Not outside board as per table_120
                if(chess_b.square[n].isEmpty() or chess_b.square[n].color==opposite_color):
                    # Append the move to move list if target square is empty of opposite_color
                    list_move.append((pos1,n,''))

        return list_move
        
    ####################################################################
    def parakeet_moves(self,pos1,color,chess_b):

	#Get all moves for Parakeet
        list_move=[]
        
        if(color=='white'):

            # Move one square up
            n=self.table_120[self.table_64[pos1]-10]
            if(n!=-1):
                if(chess_b.square[n].isEmpty()):
                    #If the Parakeet has arrived to first top row 
					#it will be promoted as Quetzal
                    if(n<8):
                        list_move.append((pos1,n,'q'))
                    else:
                        list_move.append((pos1,n,''))
                    
            # Move Parakeet 2 squares up if Parakeet is at starting square
            if(chess_b.get_row(pos1)==6):
                # If the 2 upper squares are empty
                if(chess_b.square[pos1-8].isEmpty() and chess_b.square[pos1-16].isEmpty()):
                    list_move.append((pos1,pos1-16,''))

            # Move One squre diagoanlly to capture upper left
            n=self.table_120[self.table_64[pos1]-11]
            if(n!=-1):
                if(chess_b.square[n].color=='black'):
                    if(n<8): 
						#If the Parakeet has arrived to first top row 
						#it will be promoted as Quetzal
                        list_move.append((pos1,n,'q'))
                    else:
                        list_move.append((pos1,n,''))

            # Move One squre diagoanlly to capture upper right
            n=self.table_120[self.table_64[pos1]-9]
            if(n!=-1):
                if(chess_b.square[n].color=='black'):
                    if(n<8):
						#If the Parakeet has arrived to first top row 
						#it will be promoted as Quetzal					
                        list_move.append((pos1,n,'q'))
                    else:
                        list_move.append((pos1,n,''))
        
        else:
            
            # Move one square up
            n=self.table_120[self.table_64[pos1]+10]
            if(n!=-1):
                if(chess_b.square[n].isEmpty()):
                    #If the Parakeet has arrived to top row 
					#it will be promoted as Quetzal
                    if(n>55):
                        list_move.append((pos1,n,'q'))
                    else:
                        list_move.append((pos1,n,''))

            # Move Parakeet 2 squares up if Parakeet is at starting square
            if(chess_b.get_row(pos1)==1):
                if(chess_b.square[pos1+8].isEmpty() and chess_b.square[pos1+16].isEmpty()):
                    list_move.append((pos1,pos1+16,''))
                     
            # Move One squre diagoanlly to capture upper left
            n=self.table_120[self.table_64[pos1]+9]
            if(n!=-1):
                if(chess_b.square[n].color=='white' ):
                    if(n>55):
                        list_move.append((pos1,n,'q'))
                    else:
                        list_move.append((pos1,n,''))

            # Move One squre diagoanlly to capture upper right
            n=self.table_120[self.table_64[pos1]+11]
            if(n!=-1):
                if(chess_b.square[n].color=='white' ):
                    if(n>55):
                        list_move.append((pos1,n,'q'))
                    else:
                        list_move.append((pos1,n,''))
            
        return list_move
        
    ####################################################################
