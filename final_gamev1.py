from tkinter import *
import time
import random
status=True
def leaderboard():
    global scores
    f = open("data.txt", "a")
    f.write(str(scores)+' ')
    f.close()

def best_scores():
    f = open("data.txt", "a")
    f.write(str(scores)+' ')
    f.close()
    f = open("data.txt", "r")
    f1=f.read().split()
    score=0
    for a in f1:
        if score<=int(a):
            score=int(a)
    return score



c=True
WIDTH = 800
HEIGHT = 500


tk = Tk()
frame3=Frame(tk)

gameCanvas = Canvas(frame3, width=WIDTH, height=HEIGHT, bg="black")




tk.title("Drawing")
gameCanvas.pack(expand=1)




def move_right(event):
    global bar,gameCanvas
    pos_bar=gameCanvas.coords(bar)
    if pos_bar[2]>=WIDTH:        
       gameCanvas.move(bar, 0,0)
    else:       
        gameCanvas.move(bar, 30,0)
def cheat(e):
    global bar,gameCanvas
    bar=gameCanvas.create_rectangle(0,470,800,500)
def uncheat(e):
    global bar,gameCanvas
    bar=gameCanvas.create_rectangle(0,470,800,500)

def move_left(event):
    global bar,gameCanvas
    pos_bar=gameCanvas.coords(bar)
    if pos_bar[0]<=0:        
        gameCanvas.move(bar, 0,0)
    else:       
        gameCanvas.move(bar, -30,0)

scores=0
colors = ['yellow']
size = random.randrange(20, 40)
color = random.choice(colors)
x=random.randint(0,400)
ball = gameCanvas.create_oval(x, 0, x+size, size, fill=color)
bar = gameCanvas.create_rectangle(300, 500, 500, 300, fill=color)
speedx = random.randrange(1, 10)
speedy = random.randrange(1, 10)
frame3.pack()
tk.bind('<Right>', move_right)
tk.bind('<Left>', move_left)
tk.bind('<Return>',cheat)
tk.bind('<Up>',uncheat)
frame4=LabelFrame(tk, text='GAME OVER :(', font=('Helvetica',50),bd=0,fg='yellow',  pady=20, bg='pink')


while c==True:
        gameCanvas.move(ball, speedx, speedy)
        pos_ball = gameCanvas.coords(ball)
        pos_bar= gameCanvas.coords(bar)
        if pos_ball[2] >= WIDTH or pos_ball[0] <= 0 :
            speedx *= -1

        if  (pos_ball[2]>=pos_bar[0] and pos_ball[0]<=pos_bar[0] and pos_ball[3]>=pos_bar[1]):
            if speedx>0:
                speedx *= -1
            else:
                gameCanvas.move(ball, -5, speedy)


        if  (pos_ball[2]>=pos_bar[2] and pos_ball[0]<=pos_bar[2] and pos_ball[3]>=pos_bar[1]):
            if speedx<0:
                speedx *= -1
            else:
                gameCanvas.move(ball, 5, speedy)
        if  pos_ball[1] <= 0:
            speedy *= -1
        if  pos_ball[3] >= HEIGHT:
            c=False
            frame3.destroy()
            frame4.pack()
        if (pos_ball[0]+pos_ball[2])/2<=pos_bar[2] and (pos_ball[0]+pos_ball[2])/2>=pos_bar[0] and pos_ball[3]>=pos_bar[1]:
            speedy *= -1
            scores+=1
        
        tk.update()
        time.sleep(0.001)

label2=Label(frame4, text='YOUR SCORE:'+str(scores), font=('Helvetica',14), bg='pink')
label2.pack(expand=1)
scores=best_scores()
label2=Label(frame4, text='BEST SCORE:'+str(scores), font=('Helvetica',14), bg='pink')
label2.pack(expand=1)
leader_board=Button(frame4, text='LEADERBOARD',font=('Helvetica',20),width=20,bd=3,fg='white',  pady=20, bg='green', command=leaderboard)
leader_board.pack()

tk.mainloop() 
