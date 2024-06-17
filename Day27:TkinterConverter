from tkinter import *
import tkinter


window = tkinter.Tk()
window.title("A mile to km converter")
window.minsize(width=200, height=200)
window.config(padx=20, pady=20)

#Kindof like a format can imporove by using oop
my_label = Label(text="Choose a converter on the bottom left", font=("Arial",12))
my_label.grid(column=2, row=0)

input_enter = tkinter.Entry(width=10)
input_enter.grid(column=2, row=3)

miles_text = Label(text="Entry", font=("Arial",12))
miles_text.grid(column=3, row=3)

equal_to_text = Label(text="is equal to", font=("Arial",12))
equal_to_text.grid(column=1, row=4)
equal_to_text.config(padx=0, pady=0)

km_text = Label(text="Convert", font=("Arial",12))
km_text.grid(column=3, row=4)

start_label = Label(text="0", font=("Arial",12, "bold"))
start_label.grid(column=2, row=4)


def miles_to_km_click():
    print("converting...")
    num_miles = float(input_enter.get())
    new_km = num_miles * 1.609
    start_label.config(text=round(new_km, 2))


def km_to_miles_click():
    print("converting...")
    num_km = float(input_enter.get())
    new_miles = num_km/1.609
    start_label.config(text=round(new_miles, 2))


button = tkinter.Button(text="Calculate")
button.grid(column=2, row=5)


def radio_used():
    if radio_state.get() == 1:
        my_label.config(text="Select your Milage Below")
        miles_text.config(text="Miles")
        km_text.config(text="Km")
        button.config(command=miles_to_km_click)
    else:
        my_label.config(text="Select your Kmeters Below")
        miles_text.config(text="Km")
        km_text.config(text="Miles")
        button.config(command=km_to_miles_click)


radio_state = IntVar()
radiobutton1 = Radiobutton(text="miles to km", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="km to miles", value=2, variable=radio_state, command=radio_used)


radiobutton1.grid(column=1, row=6)
radiobutton2.grid(column=1, row=7)
window.mainloop()
