from tkinter import *

window = Tk()

window.title("My first GUI program")
window.minsize(width=500, height=300)

## Label
my_label = Label(text="I am a label", font=("Arial", 24))
my_label["text"] = "New Text"
my_label.config(text="New Text")
my_label.grid(column=1, row=1)
my_label.config(padx=50, pady=50)


## Button
def button_clicked():
    new_text = input.get()
    my_label["text"] = new_text


button = Button(text="Click Me", command=button_clicked)
button.grid(column=2, row=2)
# button.config(padx=50, pady=50)

new_button = Button(text="Click Me Too")
new_button.grid(column=1, row=3)
# new_button.config(padx=50, pady=50)

## Entry

input = Entry(width=10)
input.grid(column=3, row=4)
# input.config(padx=50, pady=50)


window.mainloop()
