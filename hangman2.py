import random
counter=0
guess=""
lists=["violet","red","pink","yellow","blue","green","black"]
item=list((random.choice(lists)))
items=""
for char in item:
    items+=char
x=len(item)
your_answer=['_']*(x)
while True:
    if counter<10 and your_answer!=item:
        guess=input("Enter an alphabet: ")
        if guess in item:
            print("Great Guess :)")
            for indexes in range(x-1):
                if item[indexes]==guess:
                    your_answer[indexes]=guess
            print("Your answer was: ", end="")
            for i in your_answer:
                print(i, end="")
            print()
            print("Wrong attempts="+str(counter)+"/10")
        else :
            print("Uh-oh! Not a good guess")
            counter+=1
            print("Wrong attempts="+str(counter)+"/10")
    else:
        print("Your answer was: ", end="")
        for i in your_answer:
            print(i, end="")
        print()
        print("Wrong attempts="+str(counter)+"/10")
        print("Correct answer was: "+str(items))
        break

    