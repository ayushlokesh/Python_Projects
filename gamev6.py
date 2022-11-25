from tkinter import *
import time
import random
windows = Tk()
windows.title('ULTIMATE_PING_PONG')
windows.config(bg='purple')
n=0; lists=[]
def continue_click():
    global frame,entry, frame1, name, label2
    lists=[]
    frame1=LabelFrame(windows, text='CHOOSE YOUR DIFFICULTY LEVEL', font=('Helvetica',50),bd=0,fg='yellow',  pady=20, bg='green')
    label2=LabelFrame(frame1, text=f'HI {entry.get()}, PLEASE CHOOSE YOUR LEVEL!', font=('Helvetica',14), bg='green')
    easy_button=Button(label2, text='EASY', font=('Helvetica',14),width=20, pady=20, bg='blue', command=easy)
    easy_button.pack()
    medium_buton=Button(label2, text='MEDIUM',font=('Helvetica',14),width=20, pady=20, bg='violet', command=medium)
    medium_buton.pack()
    hard_button=Button(label2, text='HARD', font=('Helvetica',14),width=20, pady=20, bg='red', command=hard)
    hard_button.pack()
    windows.config(bg='green')
    frame.destroy()
    label2.pack()
    frame1.pack()

    

def easy():
    global n, lists, windows
    n=1
    lists=[100,150,0,5,0.01,300,600,470]
    windows.quit()
    
    
def medium():
    global lists, windows
    n=2
    lists=[60,90,6,9,0.007,350,550,460]
    windows.quit()
    
def hard():
    global lists, windows
    n=3
    lists=[20,40,10,12,0.004,400,500,450]
    windows.quit()
   

frame=LabelFrame(windows, text='WELCOME TO ULTIMATE PING PONG....', font=('Helvetica',50),bd=0,fg='yellow',  pady=20, bg='purple')
label1=LabelFrame(frame, text='Enter Your Name', font=('Helvetica',14))
label1.grid(padx=200,row=0,columnspan=2, column=0)
entry=Entry(label1, width=50 ,bg='pink', fg='black', borderwidth=10, font=('Helvetica',20))
entry.pack()
frame.pack(expand=1)
next_button=Button(frame, text='CONTINUE', font=('Helvetica',14),width=20, pady=20, bg='green', command=continue_click)
next_button.grid(padx=20,pady=20,row=1, column=0)
exit_button=Button(frame,bg='red', text='EXIT', font=('Helvetica',14), width=20, pady=20, command=windows.quit)
exit_button.grid(padx=20,pady=20,row=1, column=1)

windows.mainloop()

print(lists)
# WIDTH = 800
# HEIGHT = 500
x2=lists[0]
y2=lists[1]
l_s=lists[2]
m_s=lists[3]
t=lists[4]
r1=lists[5]
r2=lists[6]
r3=lists[7]

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


gameWindow= Tk()
frame3=Frame(gameWindow)

gameCanvas = Canvas(frame3, width=WIDTH, height=HEIGHT, bg="black")




gameWindow.title("Drawing")
gameCanvas.pack(expand=1)




def move_right(event):
    global bar,gameCanvas, pos_bar, WIDTH
    pos_bar=gameCanvas.coords(bar)
    if pos_bar[2]>=WIDTH:        
       gameCanvas.move(bar, 0,0)
    else:       
        gameCanvas.move(bar, 20,0)

def move_left(event):
    global bar,gameCanvas, pos_bar
    pos_bar=gameCanvas.coords(bar)
    if pos_bar[0]<=0:        
        gameCanvas.move(bar, 0,0)
    else:       
        gameCanvas.move(bar, -20,0)

scores=0
colors = ['yellow']
size = random.randrange(x2, y2)
color = random.choice(colors)
x=random.randint(0,400)
ball = gameCanvas.create_oval(x, 0, x+size, size, fill=color)
bar = gameCanvas.create_rectangle(r1, 500, r2, r3, fill=color)
speedx = random.randrange(l_s, m_s)
speedy = random.randrange(l_s, m_s)
frame3.pack()
gameWindow.bind('<Right>', move_right)
gameWindow.bind('<Left>', move_left)


frame4=LabelFrame(gameWindow, text='GAME OVER :(', font=('Helvetica',50),bd=0,fg='yellow',  pady=20, bg='pink')


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
        
        gameWindow.update()
        time.sleep(t)

label2=Label(frame4, text='YOUR SCORE:'+str(scores), font=('Helvetica',14), bg='pink')
label2.pack(expand=1)
scores=best_scores()
label2=Label(frame4, text='BEST SCORE:'+str(scores), font=('Helvetica',14), bg='pink')
label2.pack(expand=1)
leader_board=Button(frame4, text='LEADERBOARD',font=('Helvetica',20),width=20,bd=3,fg='white',  pady=20, bg='green', command=leaderboard)
leader_board.pack()
gameWindow.mainloop() 