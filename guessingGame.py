print('welcome to the guessing game')

user_name = input('what is your name:')

secret_number = '7'

print('hello' ,user_name)
print('guess the secret number from 1 to 10: ')

user_guess=input()
if user_guess == secret_number:
 print('correct,you win!')
else: 
 print('you loser, guess again ')
   
user_guess=input()

if user_guess == secret_number:
 print('correct, you win!')
else:
 print('you loser, guess  again ')
   
user_guess=input()

if user_guess == secret_number:
 print('correct, you win!')
else:
 print('you loser, guess again')
   
print('game over,you lose')
   
   import random
event = random.random(0,1)

def function(event, is_favorable):
    if not is_favorable:
        evet = "reset event"
        return event

def function2(event):
    if event = 0:
        return event
        else:
            return none 
