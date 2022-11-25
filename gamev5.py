from tkinter import *
import time
import random

WIDTH = 800
HEIGHT = 500
tk = Tk()
pause=False
def pause_click():
    global pause,pause_button,play_button
    pause=True
    pause_button.destroy()
    play_button=Button(frame3, text='PLAY', font=('Helvetica',14),width=72, pady=20, bg='yellow', fg='white',command=play_click)
    play_button.pack()
    return
def play_click():
    global pause,pause_button,play_button
    pause=False
    play_button.destroy()
    pause_button=Button(frame3, text='PAUSE', font=('Helvetica',14),width=72, pady=20, bg='blue', command=pause_click)
    pause_button.pack()
    play_game()
    return


frame3=Frame(tk)
play_button=Button(frame3, text='PLAY', font=('Helvetica',14),width=72, pady=20, bg='yellow', fg='white',command=play_click)
gameCanvas = Canvas(frame3, width=WIDTH, height=HEIGHT, bg="black")
pause_button=Button(frame3, text='PAUSE', font=('Helvetica',14),width=72, pady=20, bg='blue', command=pause_click)
play_button.pack()
tk.title("Drawing")
gameCanvas.pack(expand=1)

colors = ['yellow']

size = random.randrange(20, 40)
color = random.choice(colors)
x=random.randint(0,400)
ball = gameCanvas.create_oval(x, 0, x+size, size, fill=color)
bar = gameCanvas.create_rectangle(300, 500, 500, 400, fill=color)
speedx = random.randrange(1, 10)
speedy = random.randrange(1, 10)
print(gameCanvas.coords(ball))

def move_right(event):
    global bar,pos_bar,gameCanvas
    print("Hi  ")
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
frame4=Label
frame5=LabelFrame(tk, text='GAME OVER :(', font=('Helvetica',50),bd=0,fg='yellow',  pady=20, bg='pink')

label2=Label(frame5, text='YOUR SCORE:'+str(scores), font=('Helvetica',14), bg='pink')
label2.pack(expand=1)

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
        frame5.pack()
    if (pos_ball[0]+pos_ball[2])/2<=pos_bar[2] and (pos_ball[0]+pos_ball[2])/2>=pos_bar[0] and pos_ball[3]>=pos_bar[1]:
        speedy *= -1
        scores+=1
        label2.destroy()
        label2=Label(frame5, text='YOUR SCORE:'+str(scores), font=('Helvetica',14), bg='pink')
        label2.pack(expand=1)
frame3.pack()
pos_bar= gameCanvas.coords(bar)
gameCanvas.bind('<Right>', move_right)
gameCanvas.bind('<Left>', move_left)
def play_game():
    global pause,scores
    while c==True:
        if pause==True:
            tk.update()
            tk.mainloop()
        else:
            update(ball)
            tk.update()
            time.sleep(0.001)



tk.mainloop()