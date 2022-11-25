from tkinter import *
windows = Tk()
windows.title('ULTIMATE_PING_PONG')
windows.config(bg='purple')

def continue_click():
    global frame,entry, frame1, name, label2
    frame1=LabelFrame(windows, text='CHOOSE YOUR DIFFICULTY LEVEL', font=('Helvetica',50),bd=0,fg='yellow',  pady=20, bg='green')
    label2=LabelFrame(frame1, text=f'HI {entry.get()}, PLEASE CHOOSE YOUR LEVEL!', font=('Helvetica',14), bg='green')
    easy_button=Button(label2, text='EASY', font=('Helvetica',14),width=20, pady=20, bg='blue')
    easy_button.pack()
    medium_buton=Button(label2, text='MEDIUM',font=('Helvetica',14),width=20, pady=20, bg='violet')
    medium_buton.pack()
    hard_button=Button(label2, text='HARD', font=('Helvetica',14),width=20, pady=20, bg='red')
    hard_button.pack()
    windows.config(bg='green')
    frame.destroy()
    label2.pack()
    frame1.pack()

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
