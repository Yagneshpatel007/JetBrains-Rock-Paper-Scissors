import random
import math


def game():
    global ty
    item = ['rock', 'paper', "scissors"]
    end = True
    while end:
        user_choice = input()
        option = random.choice(item)
        if user_choice == 'scissors':
            if option == 'paper':
                print('Well done. The computer chose paper and failed')
                ty += 100
            elif option == 'rock':
                print('Sorry, but the computer chose rock')
            else:
                print('There is a draw (scissors)')
                ty += 50
        elif user_choice == 'paper':
            if option == 'rock':
                print('Well done. The computer chose rock and failed')
                ty += 100
            elif option == 'scissors':
                print('Sorry, but the computer chose scissors')
            else:
                print('There is a draw (paper)')
                ty += 50
        elif user_choice == 'rock':
            if option == 'scissors':
                print('Well done. The computer chose scissors and failed')
                ty += 100
            elif option == 'paper':
                print('Sorry, but the computer chose paper')
            else:
                print('There is a draw (rock)')
                ty += 50
        elif user_choice == '!exit':
            print('Bye!')
            end = False
        elif user_choice == '!rating':
            print('Yours rating:', ty)
        else:
            print('Invalid input')
def userdobo():
    global ty
    ele = []
    choosen = userwant[math.ceil(len(userwant)/2)]
    dd = True
    while dd:
        cd = input()
        if cd in userwant:
            for d in range(len(userwant)):
                if userwant[d] == cd:
                    i = d
            if i < math.ceil(len(userwant) / 2):
                print(f'Sorry, but the computer chose {choosen}')
            elif i > math.ceil(len(userwant) / 2):
                print(f'Well done. The computer chose {choosen} and failed')
                ty += 100
            elif i == math.ceil(len(userwant) / 2):
                print(f'There is a draw ({choosen})')
                ty += 50
        elif cd == '!rating':
            print('Yours rating:', ty)
        elif cd == '!exit':
            print('Bye!')
            dd = False
        else:
            print('Invalid input')


user = input('Enter your name:')
print('Hello,', user)
record = open('rating.txt', 'r+')
tb =record.readline().split('\n')
ty = 0
for i in tb:
    if user in i:
        co = i.split()
        ty = int(co[1])
        break
userwant = input().split(',')
print("Okay, let's start")
if userwant == ['']:
    game()
else:
    userdobo()
tt = user + ' ' + str(ty)
print(tt, file=record, flush=True)
record.close()


