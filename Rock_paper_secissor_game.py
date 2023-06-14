import random
import time
def game():
    
    l=['rock' , 'paper' , 'scissor']
    choose=random.choice(l)
    take_input=input('enter rock , paper , scissor   ').lower()
    if take_input == choose:
        print('Congratulations! You win!')
    else:
        print('ohh! you lose')
        
        
if __name__ == "__main__":
    print('Starting game...')
    time.sleep(2)
    game()
    while(True):
        take =input('you want to play again  ').lower()
        if(take == 'yes'):
            print('Starting a New game...')
            time.sleep(1)
            game()
        else:
            break