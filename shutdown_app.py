import os
from tkinter import * #type: ignore

root = Tk()
root.title("ShutDown")
root.geometry("500x600")
root.config(bg="Blue")

def restart():
    os.system("shutdown /r /t 1")

def restart_timer():
    os.system("shutdown /r /t 20")

def log_out():
    os.system("shutdown /l")
    
def shutDown():
    os.system("shutdown /s /t 1")



r_button = Button(root, text="Restart", font=("Time New Roman",16,"bold"),relief=RAISED, cursor = "plus",command= restart)
r_button.place(x=150, y=60, height =50, width=200)

rt_button = Button(root, text="Restart with Time", font=("Time New Roman",16,"bold"),relief=RAISED, cursor = "plus",command= restart_timer)
rt_button.place(x=150, y=170, height =50, width=200)

lg_button = Button(root, text="Log-Out", font=("Time New Roman",16,"bold"),relief=RAISED, cursor = "plus", command = log_out)
lg_button.place(x=150, y=270, height =50, width=200)

sd_button = Button(root, text="Shut Down", font=("Time New Roman",16,"bold"),relief=RAISED, cursor = "plus", command= shutDown)
sd_button.place(x=150, y=370, height =50, width=200)

quit_button = Button(root, text="Quit", font=("Elephant",25,"bold","underline"),fg="Red", relief=RAISED, command= root.quit, cursor="plus")
quit_button.place(x=150, y=470, height= 50, width = 200)

root.mainloop()