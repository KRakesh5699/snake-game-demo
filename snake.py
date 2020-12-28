from colorama import Fore, Back, Style
import random

target=50
score=0

ladder1=5
ladder2=13
ladder3=22

snake=9
snake=15
snake=36
print(Fore.RED + 'SNAKE GAME')
print(Fore.RED + 'Rules and conditions are given below read carefully first:-')
print(Back.GREEN + "Enter d to roll the die")
print("Score start at :0")
print("ladders are at:5,23,32")
print("Sankes are at :9,15,36")
print("target score is 50.")
print(Style.RESET_ALL)
print('\n')
print(Fore.GREEN + '#################### GOOD LUCK ################')
print(Style.RESET_ALL)
a=True
while a:
    if score < target:
        print(Style.RESET_ALL)
        var=input("Roll diec:")
        if var == 'd':
            dice=random.randint(1,6)
            print(Fore.RED +"Dice:{}".format(dice))
            score=score+dice
            print(Fore.GREEN +"Score:{}".format(score))
            if score == 5:
                score=score+5
                print("luckky fellow you got a ladder now your score is {}".format(score))
            elif score == 13:
                score = score + 13
                print("luckky fellow you got a ladder now your score is {}".format(score))
            elif score == 22:
                score = score + 22
                print("luckky fellow you got a ladder now your score is {}".format(score))
            elif score == 9:
                score = score - 9
                print("no!!! bad luck you got a snake now it took 9 ponits from your score and score is{}".format(score))
            elif score == 13:
                score = score - 13
                print("no!!! bad luck you got a snake now it took 13 ponits from your score and score is{}".format(score))
            elif score == 22:
                score = score - 22
                print("no!!! bad luck you got a snake now it took 22 ponits from your score and score is{}".format(score))
            else:
                score = score
        else:
            print("enter d to roll the diec")
    else:
        print("You are won the match")
        a=False








