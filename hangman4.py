import random
from time import sleep

while True:
    size=0
    counter=0
    guess=""
    word_list=[]
    print("The Hangman is going to start.....")
    sleep(2)
    print("Choose the level of difficulty: ")
    print("  PRESS 1 -> EASY--->10 OR MORE CHARACTERS")
    print("  PRESS 2 -> MEDIUM--->6 TO 9 CHARACTERS")
    print("  PRESS 3 -> HARD--->5 OR LESS CHARACTERS")
    print("  PRESS 4 -> TO STATE YOUR CHOICE FOR NUMBER OF CHARACTERS")
    while True:
        level=int(input("Type here: "))
        if level==1:
            size=random.randint(11,22)
            break
        elif level==2:
            size=random.randint(7,10)
            break
        elif level==3:
            size=random.randint(2,6)
            break
        elif level==4 :
            size=int(input("Enter your choice for number of characters: "))+1
            break
        else:
            print("invalid input")
            print("Choose Again...")


    f=open("EnglishWords.txt","r")
    lists=[]
    for x in f:
        string=x
        if len(string)==size:
            lists.append(x)
            continue
    item=list((random.choice(lists)))
    item.remove(item[size-1])
    items=""
    for char in item:
        items+=char

    your_answer=['_']*(size-1)
    while True:
        if counter<10 and your_answer!=item:
            print("You can't enter letter from this list: ")
            print(word_list)
            while True:
                guess=input("Enter the character which is an alphabet and not present in the above list: ")
                if guess in word_list:                
                    guess=input("Enter the character which is an alphabet and not present in the above list: ")
                    if guess not in word_list:
                        break
                else:
                    if (int(guess) not in range(0,10)) or (guess=='\n'):
                        word_list.append(guess)
                        break
                    else:
                        continue
            if guess in item:
                print("Great Guess :)")
                for indexes in range(size-1):
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
    value = input("Enter 'Y' to continue else enter 'N' : ")
    if value.upper()!='Y':
        break

    
