import random
print('1:easy')
print('2:normal')
print('3:hard')
mode=int(input('hurdles: '))
elements_player=['Rock','Paper','Scissors']
elements_AI=['Rock','Paper','Scissors']
rule_lost={'Scissors':'Rock','Paper':'Scissors','Rock':'Paper'}
rule_win={'Rock':'Scissors','Scissors':'Paper','Paper':'Rock'}
def easy_mode():
    while True:
        AI=False
        print(elements_player)
        player_move=input(': ')
        try:
            elements_AI.remove(rule_lost[player_move])
        except:
            pass
        AI=random.choice(elements_AI)
        print(AI)
        if AI==rule_win[player_move]:
            print('win')
            break
        else:
            print('draw')

def normal_mode():
    while True:
        AI=False
        print(elements_player)
        player_move=input(': ')
        AI=random.choice(elements_AI)
        print(AI)
        if AI==rule_lost[player_move]:
            print('lost')
        elif AI==player_move:
            print('draw')
        elif AI!=rule_lost[player_move]:
            print('win')
            break
def hard_mode():#seemingly impossible
    while True:
        AI = False
        print(elements_player)
        player_move = input(': ')
        try:
            elements_AI.remove(rule_win[player_move])
        except:
            pass
        win=random.randrange(0,100)
        win_war=random.randrange(0,100)
        if win==win_war:
            print('win')
            break
        if AI==rule_lost[player_move]:
            print('lost')
        elif AI==player_move:
            print('draw')


match mode:
    case 1:
        easy_mode()
    case 2:
        normal_mode()
    case 3:
        hard_mode()