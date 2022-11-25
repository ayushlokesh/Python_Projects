from tkinter import *
import time
import random

WIDTH = 800
HEIGHT = 500

tk = Tk()
frame3=Frame(tk)
gameCanvas = Canvas(frame3, width=WIDTH, height=HEIGHT, bg="black")
tk.title("Drawing")
gameCanvas.pack(expand=1)

colors = ['yellow']
c=True
size = random.randrange(20, 40)
color = random.choice(colors)
x=random.randint(0,400)
ball = gameCanvas.create_oval(300, 0, 310, 10, fill=color)
bar = gameCanvas.create_rectangle(300, 500, 500, 400, fill=color)
speedx = random.randrange(1, 10)
speedy = random.randrange(1, 10)
print(gameCanvas.coords(ball))

def move_right(event):
    global bar,pos_bar,gameCanvas
    if pos_bar[2]>=WIDTH:        
        gameCanvas.move(bar, 0,0)
    else:       
        gameCanvas.move(bar, 5,0)
def move_left(event=None):
    global bar,pos_bar,gameCanvas
    if pos_bar[0]<=0:        
        gameCanvas.move(bar, 0,0)
    else:       
        gameCanvas.move(bar, -5,0)
    
scores=0
frame4=LabelFrame(tk, text='GAME OVER :(', font=('Helvetica',50),bd=0,fg='yellow',  pady=20, bg='pink')



def update(ball):
    global speedx,speedy,c,bar,pos_bar,pos_ball,gameCanvas,scores
    gameCanvas.move(ball, speedx, speedy)
    pos_ball = gameCanvas.coords(ball)
    pos_bar= gameCanvas.coords(bar)
    if pos_ball[2] >= WIDTH or pos_ball[0] <= 0:
        speedx *= -1
    if  pos_ball[1] <= 0:
        speedy *= -1
    if  pos_ball[3] >= HEIGHT:
        c=False
        frame3.destroy()
        frame4.pack()
    if (pos_ball[0]+pos_ball[2])/2<=pos_bar[2] and (pos_ball[0]+pos_ball[2])/2>=pos_bar[0] and pos_ball[3]>=pos_bar[1]:
        speedy *= -1
        scores+=1
frame3.pack()
pos_bar= gameCanvas.coords(bar)
tk.bind('<Right>', move_right)
tk.bind('<Left>', move_left)

while c==True:
    update(ball)
    tk.update()
    time.sleep(.01)

label2=Label(frame4, text='YOUR SCORE:'+str(scores), font=('Helvetica',14), bg='pink')
label2.pack(expand=1)
tk.mainloop()