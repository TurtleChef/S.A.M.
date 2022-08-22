import tkinter as tk
import random

root = tk.Tk()

root.title("S.A.M")

entry_label = tk.Label(root, text = "blah blah: ")
entry_label.grid(row = 0, column = 1)

user_entry = tk.Entry(root)
user_entry.grid(row = 0, column = 1)

text_box = tk.Text(root, width = 150, height = 100)
text_box.grid(row = 1, column = 0, columnspan = 2)

text_box.insert("end-1c", "simple answering machine")

random_num = random.randint(1, 5)

def guess_number(event = None):
    guess = user_entry.get()
    
    if guess == str(random_num):
        text_box.delete(1.0, "end-1c")
        text_box.insert("end-1c", "you win!")
    else:
        text_box.delete(1.0, "end-1c")
        text_box.insert("end-1c", "try again")
        
        user_entry.delete(0, "end")
    
user_entry.bind("<Return>", guess_number)

root.mainloop()