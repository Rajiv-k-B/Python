# snake and ladders

from PIL import Image
import random
end=100


def show_board():
    img =Image.open('slb.jpg')
    img.show()
    
def paly():
    p1_name = raw_input('Player 1, Please enter your name: ')
    p2_name = raw_input('Player 2, Please enter your name: ')
    #initial point of player 1
    pp1=0
    # initial point of player 2
    pp2=0
    
    turn =0
    while(1):
        if turn%2==0:
            # player 1 turn 
            print(p1_name,' Your turn')
            # ask player's choice to continue
            c = input('Press 1 to continue, 0 to quit : ')
            if c==0:
                print(p1_name,' scored',pp1)
                print(p2_name, 'scored',pp2)
                print('Quitting the game, Thanks for playing')
                break
            dice = random.randint(1,6)
            print('Dice showed', dice)
            # add the points
            pp1=pp1 + dice

            pp1 = check_ladder(pp1)

            pp2 = check_snake(pp1)
            
            # check if player goes beyond the board
            if pp1>end:
                pp1=end
            print(p1_name,'Your score: ',pp1)
            
            if reached_end(pp1):
                print(P1_name,' won')
                break
        else:
                
show_board()
play()