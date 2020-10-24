films = {
    "Finding Dory": [3,5],
    "Bourne": [18,5],
    "Tarzan": [15,5],
    "Ghost Busters": [12,5]
    }

while True:
    choice = input("What film you want to watch?: ").strip().title()
    if choice in films:
       age = int(input("How old are you?: ").strip())

       #Check user age

       if age >= films[choice][0]:

           #check for the seats
           if films[choice][1] > 0:
            print("Enjoy the film!")
            films[choice][1] = films[choice][1] - 1
           else:
               print("Sorry! No tickets left.")
       else:
           print("You are too young to see the film!")
           
    else:
        print("We don't have this film!")
