import random 
ran_Num = random.randint(0, 2)

choices = ['rock', 'paper', 'scissors']
comp_choice = choices[ran_Num]
print(comp_choice)

try:
    user_choice = str(input('choose between rock, paper & scissors: ')).lower()
    
    if user_choice not in choices:
        raise ValueError('input a valid option')
    
    
    if user_choice == 'scissors' and comp_choice == 'paper':
        print(f'you chose {user_choice} while computer chose {comp_choice}, you win')
        
    elif user_choice == 'rock' and comp_choice == 'scissors':
        print(f'you chose {user_choice} while computer chose {comp_choice}, you win')
    
    elif user_choice == 'paper' and comp_choice == 'rock':
        print(f'you chose {user_choice} while computer chose {comp_choice}, you win')
    
    elif user_choice == comp_choice:
        print(f'you chose {user_choice} while computer chose {comp_choice}, so its a draw')
    
    else:
        print(f'you chose {user_choice} while computer chose {comp_choice}, computer wins')
    
        
except ValueError as e:
    print(e)