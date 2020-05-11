# Importing Libraries
import random as r

# Variables
user_name = input('Type Your name : ').title()
user_said = input(f'Welcome {user_name}.\nDo you want to play Rock Paper Scissors (Y/N) : ').lower()

while True:
    if ('y' not in user_said) and ('n' not in user_said) and (user_said != True):
        user_said = input('Invalid keyword\nType again : ')

    elif 'y' in user_said:
        
        user_point = 0
        computer_point = 0
        # User inputs
        user_like = int(input('\nHow much point you like to play : '))
        user_choice = input('For Rock "R" for paper "P" for scissors "S"\nType your choice : ').lower()

        # Checking user input valid or not if valid then tell him/her what he/she choose
        while True:
            # points count when game over
            if (user_point == user_like) or (computer_point == user_like):
                if user_point > computer_point:
                    print(f'You won by {user_point - computer_point} points.')
                elif computer_point > user_point:
                    print(f'Computer won by {computer_point - user_point} points.')
                else:
                    print(f'Match Draw. Your scored {user_point} and computer scored {computer_point}.')
                break
            
            # if user input not valid
            elif ("r" not in user_choice) and ("p" not in user_choice) and ("s" not in user_choice): 
                print('\nInvalid Choice.')
                user_choice = input('Choose right letter again : ')

            # Now the real things
            else:
                # create random choice
                computer_choice = r.choice(["R", "P", "S"])
                print('\n')
                
                #tell user what he/she choose
                if "r" in user_choice:
                    print('You choose Rock.')
                elif "p" in user_choice:
                    print('You choose Paper.')
                else:
                    print('You choose scissors.')

                #tell user what computer choose
                if "R" in computer_choice:
                    print('Computer choose Rock.')
                elif "P" in computer_choice:
                    print('Computer choose Paper.')
                else:
                    print('Computer choose Scissors.')

                # Now check who won
                    
                    # if user choose Rock as R
                if "r" in user_choice:
                    if "R" in computer_choice:
                        print('Draw.')
                    elif "P" in computer_choice:
                        print('Computer Won.')
                        computer_point += 1
                    else:
                        print('You won.')
                        user_point += 1

                        # if user choose paper as P
                elif "p" in user_choice:
                    if "P" in computer_choice:
                        print('Draw.')
                    elif "R" in computer_choice:
                        print('You Won.')
                        user_point += 1
                    else:
                        print('Computer Won.')
                        computer_point += 1
                    
                    # if user choose Scissors as S
                else:
                    if "S" in computer_choice:
                        print('Draw.')
                    elif "R" in computer_choice:
                        print('Computer Won.')
                        computer_point += 1
                    else:
                        print('You Won.')
                        user_point += 1

                # tell user current point
                print(f'\nYour score {user_point} and computer score {computer_point}.')
                
                # checking user_like == points or not if not then ask again else game over
                if (user_point < user_like) and (computer_point < user_like):
                    user_choice = input('Type again to play next round : ')

        user_said = input(f'\n{user_name} do you want to play Rock Paper Scissors (Y/N) :').lower()


    else:
        print(f'\nGood bye {user_name}. See you soon.')
        break
