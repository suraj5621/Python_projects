import time
import random

print('Game Starting..')
time.sleep(5)
lower_bound=int(input(' Give your lower bound range'))
upper_bound=int(input(' Give your upper bound range'))

random_value=random.randint(lower_bound,upper_bound)

print('you have only 3 chance to guess the no.')

i=1
while i<8:
    a=int(input('guess your no.'))
    if random_value == a:
        print('congratulation you make rock!')
        break
    elif random_value - a > 2 :
        print('your input too low from excat value')
    elif a - random_value > 2 : 
        print('your input too high from excat value')
    elif random_value - a <= 2:
        print('your input nearly from excat value')
    elif a - random_value <= 2 : 
         print('your input nearly from excat value')
    i=i+1