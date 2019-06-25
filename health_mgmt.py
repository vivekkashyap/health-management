def getdate():
    import datetime
    return datetime.datetime.now()


def get_exercise(name):
    f = open(name+"_exercise.txt", "a")
    a = input("exercise input: ")
    f.write("["+str(getdate())+"] "+a+"\n")

    return getdate()


def get_diet(name):
    f = open(name + "_diet.txt", "a")
    a = input("Diet input: ")
    f.write("[" + str(getdate()) + "] "+a+"\n")

    return getdate()


def show_exercise(name):
    f = open(name+"_exercise.txt", "r+")
    print(f.read())


def show_diet(name):
    f = open(name+"_diet.txt", "r+")
    print(f.read())


print("vivek || vaibhav || vijay \n Exercise and Diet plan")

while True:
    name = input("Enter your name:")
    if name == 'vivek' or name == 'vaibhav' or name == 'vijay':
        while True:
            print("1. Record Exercise \n2. Record Diet \n3. Show Exercise \n4. Show Diet\n")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                get_exercise(name)
            elif choice == 2:
                get_diet(name)
            elif choice == 3:
                show_exercise(name)
            elif choice == 4:
                show_diet(name)
            else:
                print("Wrong Choice Try Again !!")
                continue

            print(name + "... Do you Want to continue..(y/n)")
            if input() == 'y':
                continue
            else:
                break
        break
    else:
        print("Wrong Input Try Again!!")
        continue
