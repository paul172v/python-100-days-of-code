from tkinter import *

window = Tk()

window.title("Mile to KM Converter")
window.minsize(width=200, height=100)

miles_input = Entry()
miles_input.grid(column=2, row=1)

miles_label = Label(text="Miles")
miles_label.grid(column=3, row=1)

is_equal_to_label = Label(text="is equal to")
is_equal_to_label.grid(column=1, row=2)

km_value_label = Label(text="0")
km_value_label.grid(column=2, row=2)

km_label = Label(text="Km")
km_label.grid(column=3, row=2)


def calc_conversion():
    miles = miles_input.get()
    km = int(miles) * 1.60934
    km_value_label["text"] = str(km)


calc_button = Button(text="Calculate", command=calc_conversion)
calc_button.grid(column=2, row=3)


window.mainloop()
