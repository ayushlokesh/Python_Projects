from tkinter import *
import time
import random
#from PIL import Image,ImageTk


   
windows = Tk()
windows.title('ULTIMATE_PING_PONG')
# windows.bind_all('<Control-x>',boss_key)
windows.config(bg='purple')
n=0; lists=[]



def leaderboard():
    global scores,gameWindow
    
    f = open("last_game_score_data.txt", "r").read()
    f1 = open("last_game_name_data.txt","r").read()
    lists1=f.split().copy()
    lists2=f1.split().copy()
    lists3=[]
    print(lists1)
    for j in range(len(lists1)):
        for i in range(len(lists1)-1):
            if len(lists3)<len(lists1):
                lists3.append('')
            if int(lists1[i])<int(lists1[i+1]):
                lists1[i]=str(int(lists1[i])+int(lists1[i+1]))
                (lists1[i+1])=str(int(lists1[i])-int(lists1[i+1]))
                (lists1[i])=str(int(lists1[i])-int(lists1[i+1]))
                lists3[i]=lists2[i+1]
    print(lists3)
    frame5=Frame(gameWindow, bg='turquoise')
    label=Label(frame5, text='RANK         NAMES         SCORES')
    frame5.pack()
    label.pack()
    labels=[]
    for i in range(len(lists1)):
        labels.append(Label(frame5, text=str(i+1)+'         '+lists3[i]+'         '+lists1[i],fg='blue')) 
        labels[i].pack()



def best_scores():
    f = open("last_game_score_data.txt", "a")
    f.write(str(scores)+' ')
    f.close()
    f = open("last_game_score_data.txt", "r")
    f1=f.read().split()
    score=0
    for a in f1:
        if score<=int(a):
            score=int(a)
    return score


def resume():
    global frame4,frame3,gameWindow
    frame4.pack_forget()

    pass

def cheat(e):
    global bar,gameCanvas
    bar=gameCanvas.create_rectangle(0,470,800,500)



def save():
    global pos_ball, pos_bar,speedx,speedy,t
    f=open('last_game_data.txt', 'a')
    x=''; y=''
    for a in pos_ball:
        x=x+str(a)+' '
    for b in pos_bar:
        y=y+str(b)+' '
    f.write(f'{x}{speedx} {t} {y}{scores}')


def move_right(event=None):
    global bar,gameCanvas, pos_bar, WIDTH
    pos_bar=gameCanvas.coords(bar)
    if pos_bar[2]>=WIDTH:        
       gameCanvas.move(bar, 0,0)
    else:       
        gameCanvas.move(bar, 20,0)

def move_left(event):
    print('hi')
    global bar,gameCanvas, pos_bar
    pos_bar=gameCanvas.coords(bar)
    if pos_bar[0]<=0:        
        gameCanvas.move(bar, 0,0)
    else:       
        gameCanvas.move(bar, -20,0)


def continue_click():
    global frame,entry, frame1, name, label2
    lists=[]
    frame1=LabelFrame(windows, text='CHOOSE YOUR DIFFICULTY LEVEL', font=('Helvetica',50),bd=0,fg='yellow',  pady=20, bg='green')
    f=open('last_game_name_data.txt','a')
    f.write(entry.get()+' ')
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

def pause_click():
    global frame4,frame3,gameWindow
    frame4=Frame(gameCanvas,bg='grey', padx=30, pady=30)
    resume_button=Button(frame4, text='Resume', bg='yellow', padx=10,font=('Helvetica', 14))
    save_button=Button(frame4, text='Save & Quit', bg='blue',fg='white', padx=10,font=('Helvetica', 14), command=save)
    frame4.pack()
    resume_button.pack()
    save_button.pack()
    # frame3.pack_forget() 

def easy():
    global n, lists, windows
    n=1
    lists=[0,0,100,150,5,0.01,300,470,600,500,0]
    windows.quit()
    
    
def medium():
    global lists, windows
    n=2
    lists=[0,0,60,90,8,0.007,350,460,550,500,0]
    windows.quit()
    
def hard():
    global lists, windows
    n=3
    lists=[0,0,20,40,10,0.004,400,450,500,500,0]
    windows.quit()
def reload():
    global lists, windows
    f=((open('last_game_data.txt','r')).read()).split(' ')
    lists=f.copy()
    print(lists)
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
file=(open('last_game_data.txt', 'r').read()).split()
reload_button=Button(frame,bg='red', text='RELOAD LAST GAME', font=('Helvetica',14), width=20, pady=20, command=reload)
if len(file)==0:
    reload_button.config(state='disabled')
reload_button.grid(row=2,column=0,columnspan=2)
windows.mainloop()


WIDTH = 800
HEIGHT = 500
x1=float(lists[0])
y1=float(lists[1])
x2=float(lists[2])
y2=float(lists[3])
speedx=float(lists[4])
t=float(lists[5])
r1=float(lists[6])
r2=float(lists[7])
r3=float(lists[8])
r4=float(lists[9])
speedy=speedx
scores=float(lists[10])
status=True
c=True
WIDTH = 800
HEIGHT = 500


gameWindow= Tk()
gameWindow.title("Drawing")
gameWindow.bind('<Right>', move_right)
gameWindow.bind('<Left>', move_left)
gameWindow.bind('<Return>',cheat)

frame3=Frame(gameWindow)
gameCanvas = Canvas(frame3, width=WIDTH, height=HEIGHT, bg="black")
pause_button=Button(frame3, text='PAUSE', font=('Helvetica',14),width=72, pady=20, bg='blue', command=pause_click)
pause_button.pack()
gameCanvas.pack(expand=1)
scores=0
ball = gameCanvas.create_oval(x1, y1, x2, y2, fill='yellow')
bar = gameCanvas.create_rectangle(r1, r2, r3, r4, fill='yellow')
frame3.pack()
pos_ball = gameCanvas.coords(ball)
pos_bar= gameCanvas.coords(bar)

frame4=LabelFrame(gameWindow, text='GAME OVER :(', font=('Helvetica',50),bd=0,fg='yellow',  pady=20, bg='pink')




while c==True:
    gameWindow.bind_all('<Right>', move_right)
    gameWindow.bind_all('<Left>', move_left)

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
