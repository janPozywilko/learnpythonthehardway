from sys import exit

def start():

    print("\n")
    print("""Hi you are in front of three rooms numbered from #1 to #3 and you are
    about to make the most important choice of your entire life. Please take your pick wisely.""")
    print("So what's your choice? #1 , #2 or maybe #3?")

    choice = input("> ")

    if choice == "1":
        thanos_room()
    #elif choice == "2":
        #frog_room()
    #elif choice == "3":
        #deadpool_room()
    else:
        print("Really bro you didn't pick anything? That's a shame now you are going to wear Hulk's old pyjama.")

def thanos_room():
    print("So your pick was the worst possible and you are with Thanos")
    print("Do you want to leave or join his side?")
    thanos_reaction = False

    while True:

        choice_thanos = input("> ")
        
        if choice_thanos == "join":
            print("Thank you for staying with me I'm glad you stayed with me.")
            print("We are going to make this Galaxy one of the most amazing places to live.")
            print("Others must be gratefull for having us here")
            exit(0)

        elif choice_thanos == "leave" and not thanos_reaction:
            print("You pissed him a lot and now he's is going to use on of the infinity stones")
            print("Lucky for you he picked wrong stone and now he's stuck in time.")
            print("You now became the hero of galaxy and you got invite to become an Avengers.")
            thanos_reaction = True

        elif choice_thanos == "leave" and thanos_reaction:
            print("You waited too long and now Thanos is back.")
            print("This time he picked right stone")
            print("You are dead.")
            exit(0)

        elif choice_thanos == "yes" and thanos_reaction:
            print("So you are in the starting point for the second time.")
            print("I'm going to make your pick easier. Choose room #3 this time.")
            start()
        
        else:
            print("So you haven't decide what to do?")
            print("I'm going to do it for you")
            print("You are dead")
            exit(0)

def frog_room():
    #pokój zabki w ktorym dwa wyjscia to smierc a jedno wraca cie do poczatku

def deadpool_room():
    #pokoj deadpool'a w ktorym prowadzisz rozmowe z nim i jest tylko jedna opcja
    #ze giniesz bo powiedziales ze jestes avengersem

#zrob to jak wrocisz bo nie chce mi sie tego teraz robic





start()     
        







