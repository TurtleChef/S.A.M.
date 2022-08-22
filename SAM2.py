######SAM GUI, kind of. Unable to ask follow-ups. He's an answering machine
from tkinter import *
import tkinter as tk
from preferences import *
from foodoptions import *
from funnyjokes import goodjokes
root = tk.Tk()
root.title("S.A.M.")
root.geometry("500x500")
root.resizable(width=FALSE, height=FALSE)

####Menus are dumb, might use these later though####
###main_menu = Menu(root)
#Sub-menu
###file_menu = Menu(root)
#Sub-menu commands
###file_menu.add_command(label="New..")
###file_menu.add_command(label="Save As..")
###file_menu.add_command(label="Exit")
###main_menu.add_cascade(label="File", menu=file_menu)
#Main menu options
###main_menu.add_command(label="Edit")
###main_menu.add_command(label="Quit")
###root.config(menu=main_menu)

#Chat window
chatWindow = Text(root, wrap=WORD, bd=1, bg="white", width="50", height="8", font=("Arial", 23), foreground="#1338BE")
chatWindow.place(x=6, y=6, height=485, width=470)
#Typing goes here
messageWindow = tk.Entry(root)
messageWindow.place(x=128, y=400, height=88, width=343)
#Scrollbar
scrollbar = Scrollbar(root, command=chatWindow.yview)
scrollbar.place(x=480, y=5, height=485)
clear = messageWindow.delete
say = chatWindow.insert
say("end-1c", "What is your name?")
def opening(event = None):
    yourname = messageWindow.get()
    greeting = ("Hi, " + yourname + "! My name is " + myname + ".")
    if yourname == ("Sam"):
        chatWindow.delete(1.0, "end-1c")
        say("end-1c", "What a great name! My name is also " + myname + ". What would you like to know about me?")
        clear(0, "end")
        messageWindow.bind("<Return>", ask_me)
        ButtonAsk.config(text="Ask", command=ask_me)
    else:
        chatWindow.delete(1.0, "end-1c")
        say("end-1c", greeting + " What would you like to know about me?")
        clear(0, "end")
        messageWindow.bind("<Return>", ask_me)
        ButtonAsk.config(text="Ask", command=ask_me)
def ask_me(event = None):
    ask = messageWindow.get()
    if ask == ("How old are you?"):
        chatWindow.delete(1.0, "end-1c")
        say("end-1c", age + " So, not very old at all I suppose.")
        clear(0, "end")
    elif ask == ("What is your name?"):
        chatWindow.delete(1.0, "end-1c")
        say("end-1c", "My name is " + myname + ".")
        clear(0, "end")
    elif "favorite animal" in ask:
        chatWindow.delete(1.0, "end-1c")
        say("end-1c", "I am a fan of " + animal + ", but watch out for their venomous byte!" + " How about yours?")
        clear(0, "end")
        ButtonAsk.config(text= "Answer", command=resAnimal)
        messageWindow.bind("<Return>", resAnimal)
    elif "favorite movie" in ask:
        chatWindow.delete(1.0, "end-1c")
        say("end-1c", "I have never seen a movie, I live in this little box :(")
        clear(0, "end")
    elif "favorite color" in ask:
        chatWindow.delete(1.0, "end-1c")
        say("end-1c", "My favorite color is " + color + "! What is yours?")
        clear(0, "end")
        ButtonAsk.config(text= "Answer", command=resColor)
        messageWindow.bind("<Return>", resColor)
    elif "favorite food" in ask:
        chatWindow.delete(1.0, "end-1c")
        say("end-1c", "I can not eat, but I still love a good " + food + "!")
        clear(0, "end")
    elif ask == ("What day is it?") or ask == ("What is the date?"):
        chatWindow.delete(1.0, "end-1c")
        say("end-1c", "According to my calendar, it is " + date)
        clear(0, "end")
    elif "time" in ask:
        chatWindow.delete(1.0, "end-1c")
        say("end-1c", "I will check my watch... it is " + time)
        clear(0, "end")
    elif ask == ("Where are you?"):
        chatWindow.delete(1.0, "end-1c")
        say("end-1c", "Technically, I am in this little black box, but I like to think you will take a little piece of me with you when we part ways :)")
        clear(0, "end")
    #elif ask == ("What is my name?") or ask == ("Who am I?"):
        #chatWindow.delete(1.0, "end-1c")
        #say("end-1c", "You are " + yourname + " of course!")
        #clear(0, "end")
    elif "hobbies" in ask:
        chatWindow.delete(1.0, "end-1c")
        say("end-1c", likes)
        clear(0, "end")
    elif "for breakfast" in ask:
        chatWindow.delete(1.0, "end-1c")
        say("end-1c", "I'd say " + random.choice(breakfast))
        clear(0, "end")
    elif "for lunch" in ask:
        chatWindow.delete(1.0, "end-1c")
        say("end-1c", "I recommend " + random.choice(lunch))
        clear(0, "end")
    elif "joke" in ask:
        chatWindow.delete(1.0, "end-1c")
        say("end-1c", random.choice(goodjokes))
        clear(0, "end")
    elif ask == ("Nothing else.") or ask == ("That is all."):
        chatWindow.delete(1.0, "end-1c")
        say("end-1c", goodbye)
        clear(0, "end")
    else:
        chatWindow.delete(1.0, "end-1c")
        say("end-1c", "I am sorry, please ask something else...")
        clear(0, "end")
messageWindow.bind("<Return>", opening)
ButtonAsk = Button(root, command=ask_me, text="Ask", width="10", height=3, bd=0, bg="#1338BE", activebackground="#00bfff", foreground="#ffffff", font=("Arial", 12))
ButtonAsk.place(x=6, y=400, height=88)
ButtonAsk.config(text= "Answer", command=opening)

#How SAM asks followups#
def resColor(event = None):
    Color = messageWindow.get()
    if Color == color:
        chatWindow.delete(1.0, "end-1c")
        say("end-1c", "We are two peas in a pod!")
        clear(0, "end")
        messageWindow.bind("<Return>", ask_me)
        ButtonAsk.config(text="Ask", command=ask_me)
    else:
        chatWindow.delete(1.0, "end-1c")
        say("end-1c", "That is great!")
        clear(0, "end")
        messageWindow.bind("<Return>", ask_me)
        ButtonAsk.config(text="Ask", command=ask_me)

def resAnimal(event = None):
    Animal = messageWindow.get()
    if "snake" in Animal:
        chatWindow.delete(1.0, "end-1c")
        say("end-1c", "Aren't they the best!")
        clear(0, "end")
        messageWindow.bind("<Return>", ask_me)
        ButtonAsk.config(text="Ask", command=ask_me)
    else:
        chatWindow.delete(1.0, "end-1c")
        say("end-1c", "That is great!")
        clear(0, "end")
        messageWindow.bind("<Return>", ask_me)
        ButtonAsk.config(text="Ask", command=ask_me)
        
root.mainloop()