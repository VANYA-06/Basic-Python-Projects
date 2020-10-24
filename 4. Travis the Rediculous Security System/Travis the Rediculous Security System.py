known_users = ["Alice", "Bob","Clair","Dan","Emma","Fred","Georgie"]
print(len(known_users))

while True:
    print("Hi! My name is Travis")
    name = input("What is your name?").strip().capitalize()#capitalise is for all cases  

    if name in known_users:
        #print("Hello "+ name+ "!")
        print("Hello {}".format(name))
        remove = input("Would you like to remove from the system (y/n)?:").strip().lower()
        #if remove == "y" or remove == "Y":
        if remove == "y":
            known_users.remove(name)
            print("No worries, see you again!")
        elif remove == "n":
            print("No problem, I didn't want to leave anyway!")
        

    else:
        print("Hmmmm I don't think I met you yet {}".format(name))
        add_me = input("Would you like to be added in the system (y/n)?: ").strip().lower()
        if add_me == "y":
            known_users.append(name)
            print("Hey {}! Welcome.".format(name))
        elif add_me == "n":
            print("No worries, see you around!")
            
#go to run and type bob in L

        
