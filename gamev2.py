from tkinter import Canvas, Tk
import time
import random

WIDTH = 800
HEIGHT = 500

tk = Tk()
gameCanvas = Canvas(tk, width=WIDTH, height=HEIGHT, bg="black")
tk.title("Drawing")
gameCanvas.pack(expand=1)

colors = ['yellow']
c=True
size = random.randrange(20, 40)
color = random.choice(colors)
x=random.randint(0,400)
ball = gameCanvas.create_oval(300, 0, 310, 10, fill=color)
bar = gameCanvas.create_rectangle(300, 500, 500, 400, fill=color)
speedx = random.randrange(10, 20)
speedy = random.randrange(10, 20)
print(gameCanvas.coords(ball))

def moves(e):
    global bar,pos_bar,gameCanvas
    gameCanvas.delete(bar)
    if pos_bar[0]>=0 and pos_bar[2]<=WIDTH:        
        bar = gameCanvas.create_rectangle(e.x-100, 500, e.x+100, 400, fill=color)
        pos_bar= gameCanvas.coords(bar)
    elif pos_bar[0]<=0:        
        bar = gameCanvas.create_rectangle(0,500,200,400, fill=color)
    elif pos_bar[0]>=0:        
        bar = gameCanvas.create_rectangle(600,500,800,400, fill=color)
    


def update(ball):
    global speedx,speedy,c,bar,pos_bar,pos_ball,gameCanvas
    gameCanvas.move(ball, speedx, speedy)
    pos_ball = gameCanvas.coords(ball)
    pos_bar= gameCanvas.coords(bar)
    #print(pos_ball)
    print(pos_bar)
    if pos_ball[2] >= WIDTH or pos_ball[0] <= 0:
        speedx *= -1
    if  pos_ball[1] <= 0:
        speedy *= -1
    if  pos_ball[3] >= HEIGHT:
        speedy *= -1
    #     print('youfail')
        # c=False
    if (pos_ball[0]+pos_ball[2])/2<=pos_bar[2] and (pos_ball[0]+pos_ball[2])/2>=pos_bar[0] and pos_ball[3]>=pos_bar[1]:
        speedy *= -1

pos_bar= gameCanvas.coords(bar)
gameCanvas.bind('<B1-Motion>', moves)
while c==True:
   
    
    update(ball)
    tk.update()
    time.sleep(.01)