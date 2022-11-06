# jogo papel
import random
GoodValues = ["pedra", "papel", "tesoura"]
def game():
    UserPlay = input("introduza o seu palpite: pedra papel tesoura  ")
    if UserPlay in GoodValues:
        print("Your choice is: " + UserPlay)
        CompValueN = random.randint(1, 3)
        CompValue = GoodValues[(CompValueN-1)]
        print("computer played: " + CompValue)
        if GoodValues.index(CompValue)==GoodValues.index(UserPlay)-1 : print ("User won")
        if GoodValues.index(UserPlay)==GoodValues.index(CompValue)-1 : print ("Computer won")
        if GoodValues.index(UserPlay)==GoodValues.index(CompValue): print ("Nobody won")
    else: print("incorrect value")
game()
OneMore = input("One more time? (y for more)  ")
if OneMore == "y": game()