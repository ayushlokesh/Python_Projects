from tkinter import Tk, PhotoImage, Button
window = Tk()
n=int(input("Choose the size of the grid (>2): "))
window.title("OXO_GAME")
window.geometry(f"{n*100}x{n*100}")
available_square=PhotoImage(file="images/myButton.png")
player_1=PhotoImage(file="images/myButtonP1.png")
player_2=PhotoImage(file="images/myButtonP2.png")
winner=PhotoImage(file="images/winner.png")
lists=[]
player1_moves=[]
player2_moves=[]
counter=0; 
def handle_button_click(i):
    global counter, player2_moves, player1_moves
    if counter%2==0:
        player1_moves.append(i)
        print(player1_moves)
        print(f"Clicked Button {i}")
        lists[i].configure(image=player_1, command=lambda: square_taken())
    else:
        player2_moves.append(i)
        print(player2_moves)
        print(f"Clicked Button {i}")
        lists[i].configure(image=player_2, command=lambda: square_taken())
    check_win()
    counter+=1
def square_taken():
    print("Square Already Taken!")
def check_win():
    global counter,player1_moves,player2_moves,n
    status=False
    mark=0
    if counter%2==0:
        player_name="Player1"
        lists=player1_moves.copy()
    else:
        player_name="Player2"
        lists=player2_moves.copy()
    
    for i in range(n):
        if status==True:
            break
        else:
            mark=0
            for j in range(n):
                if n*i+j in lists:
                    mark+=1
            if mark==n:
                status=True

    if status==False:
        for i in range(n):
            if status==True:
                break
            else:
                mark=0
                for j in range(n):
                    if i+n*j in lists:
                        mark+=1
                if mark==n:
                    status=True

    if status==False:
        for i in range(0,1):
            if status==True:
                break
            else:
                mark=0
                for j in range(n):
                    if i+j*(n+1) in lists:
                        mark+=1
                if mark==n:
                    status=True
                
    if status==False:
        for i in range((n-1)*n,(n-1)*n+1):
            if status==True:
                break
            else:
                mark=0
                for j in range(n):
                    if i-j*(n-1) in lists:
                        mark+=1
                if mark==n:
                    status=True


    if status==True:
        print(f"{player_name} Wins! :) :)")  
    elif status==False and counter==n*n:
        print(" ): ): the Game is Drawn :( :( ")      
y=0
for i in range(n*n):
    buttons=Button(window, width=100, height=100, image=available_square,command=lambda i=i :handle_button_click(i))
    y+=1
    lists.append(buttons)
x=0

for i in range(n):
    for j in range(n):
        lists[x].place(x=j*100,y=i*100)
        x+=1

window.mainloop()