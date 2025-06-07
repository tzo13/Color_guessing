import random
from tkinter import *

colors = ["red", "yellow", "purple","blue","green","brown", "teal", "magenta","pink", "orange", "black","white","cyan"]
screen = Tk()
time = 30
score = 0

def startGame(event):
    nextColor()
    ol.delete(0, END)
    if time == 30:
        countdown()

def countdown():
    global time
    if time > 0 :
        time -= 1
        tim.configure(text = "Time: "+ str(time))
        tim.after(1000,countdown)

def nextColor(): 
     global score
     if time > 0 :
         a = ol.get()
         if a == colors[1]:
             score += 1
             print(score)
             scor.configure(text ="Score: " + str(score))
         random.shuffle(colors)  
         Color.configure(text=colors[0], fg=colors[1])


lav = Label(screen, text = "Type in the color of the word ")
scor = Label(screen, text = "Score")
tim = Label(screen, text = "Time")
Color = Label(screen, font  =("Arial",50) )
ol = Entry (screen)

lav.pack()
scor.pack()
tim.pack()
Color.pack()
ol.pack()
ol.focus_set() 
screen.bind('<Return>', startGame) 



screen.mainloop()
