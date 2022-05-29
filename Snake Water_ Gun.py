import random
#snake water  Gun or paper scissors
def gameWin(comp, you):
    # if two values are equal, declare a tie!
    if comp == you:
        return None
    # check of all possiblities when computer chose s    
    elif comp == 's':
        if you == 'w':
            return False 
        elif you == 'g':
            return True

    # check of all possiblities when computer chose w        
    elif comp == 'w':
        if you == 'g':
            return False 
        elif you == 's':
            return True 

    # check of all possiblities when computer chose g        
    elif comp == 'g':
        if you == 's':
            return False 
        elif you == 'w':
            return True              


randNO = random.randint(1,3)
print(randNO)
if randNO  == 1:
    comp = 's'
elif randNO  == 2:
    comp = 'w'
elif randNO  == 3:
    comp = 'g'
you = input("your  Turn: Snake(s) Water(w) or Gun(g)? ") 
a=gameWin(comp,you)  

print(f"computer chose {comp}")
print(f"you chose {you}")

if a == None:
    print("This game is a tie!")
elif a:
    print("you Win!")
else:
    print("You Lose!")        




# a = input("comp  Turn: Snake(s) Water(w) or Gun(g)?")
# b = input("player's Turn: Snake(s) Water(w) or Gun(g)?")

# game()