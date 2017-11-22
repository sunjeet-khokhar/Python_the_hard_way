import os
import subprocess as sp


def present_the_door():
    print("""Welcome to Bears and Dragons.....circa 2017 \n take your pick... 
    \n Press 1 for playing mind games with a bear
    \n Press 2 for battling drangons 
    \n 3 For chickening out""")
    choice = input(">...")
    if choice == '1':
        print("Entering Bear zone now...")
        bear_zone()
    elif choice == '2':
        print("Dragons here I come....")
        # dragon_fight()
    elif choice == '3':
        print("Bye bye chicken")
    elif choice == '000':
        print("Clearing screen now...")
        #sp.call('cls',shell=True)
        #os.system('cls')
        print("\033[H\033[J")
    else:
        print("Is it so difficult mate? just enter 1,2 or 3, lets try again !")
        present_the_door()
        
def bear_zone():
    print(""" GGGGGRRRRRRRRRRRRRAAAAAAAAAAH...how do you want to fight the bear
    \n Press 1 for a fist fight
    \n Press 2 for making peace with the bear by offering him some honey
    \n 3 For choosing a battle with a dragon instead""")
    choice = input(">...")
    if choice == '1':
        print("Press enter until the fingers come off your hand")
        while True:
            input()
    elif choice == '2':
        print("haha .... tricked you , it is death now")
        death("by honey overdose")
    elif choice == '3':
        print("off to fight the dragon")
        #dragon_fight()
    else:
        print("Is it so difficult mate? just enter 1,2 or 3, lets try again !")
        bear_zone()

        
def death(medium):
    print(f"Sorry, just have just been killed {medium}")


present_the_door()
