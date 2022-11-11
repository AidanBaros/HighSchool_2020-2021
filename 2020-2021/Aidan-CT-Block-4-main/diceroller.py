import random

print("Wecome to Aidan's dice roller")

def diceEngine():
    myRolls = []
    while True:
        dieType = input("How many sides on this die?    ")
        rollTimes = input("How many times should I roll the die?    ")
        print("*shakes die*")

        for x in range(0, int(rollTimes)):
            myRolls.append(random.randint(1, int(dieType)))

        print("Here are your rolls: {}".format(myRolls))
        print("Your roll total was: {}".format(sum(myRolls)))
        print("Your highest roll was: {}".format(max(myRolls)))
        print("your lowest roll was: {}".format(min(myRolls)))

        myRolls.clear()

        playerQuit = input("Do you want to quit?  Y/N   ")
        if playerQuit.lower() == "y":
            break

if __name__== "__main__":
    diceEngine()
