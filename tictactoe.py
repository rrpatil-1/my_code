import os

class Board:
    def __init__(self):
        self.cell =[' ']*10
        
    def display(self):
        print(f' {self.cell[1]}|{self.cell[2]}|{self.cell[3]}')
        print('-------')
        print(f' {self.cell[4]}|{self.cell[5]}|{self.cell[6]}')
        print('-------')
        print(f' {self.cell[7]}|{self.cell[8]}|{self.cell[9]}')
        
    def update_board(self,index,payer):
        if self.cell[index]==' ':
            self.cell[index]=payer
            
    def check_match(self,start,stop,step,player):
        for i in range(start,stop,step):
            if self.cell[i]!=player:
                return False
        return True
    def is_winner(self,player):
        if self.check_match(1,4,1,player):
            return True
        elif self.check_match(4,7,1,player):
            return True
        elif self.check_match(7,10,1,player):
            return True
        elif self.check_match(1,10,4,player):
            return True
        elif self.check_match(3,8,2,player):
            return True
        elif self.check_match(1,8,3,player):
            return True
        elif self.check_match(2,9,3,player):
            return True
        elif self.check_match(3,10,3,player):
            return True
        else:
            return False
        
    def reset(self):
        self.cell = [' ']*10
        

bord=Board()

def print_header():
    print('Welcome to Tic Tac Toe\n')

def refresh_screen():
    os.system('clear')
    
    print_header()
    
    bord.display()
    
    
while True:
    refresh_screen()
    
    X_choice = int(input('X turn (Please choose 1-9.) :',))
    
    bord.update_board(X_choice,"X")
    
    refresh_screen()
    if bord.is_winner("X"):
        print("X win's")
        play_again = input("Do you want to play again (Y/N):").upper()
        if play_again=="Y":
            bord.reset()
            continue
        else:
            break
    
    O_choice = int(input("O turns (Please choose 1 - 9) :",))
    bord.update_board(O_choice,"O")
    refresh_screen()
    if bord.is_winner("O"):
        print("O win's")
        play_again = input("Do you want to play again (Y/N):").upper()
        if play_again=="Y":
            bord.reset()
            continue
        else:
            break