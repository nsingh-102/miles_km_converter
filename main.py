from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=100)
window.config(padx=25, pady=25)


def mile_to_km():
    user_input = float(entry.get())
    result = user_input * 1.609344
    label_4.config(text=f'{result}')


label = Label(text="Miles")
label.grid(column=2, row=0)

label_2 = Label(text="is equal to")
label_2.grid(column=0, row=1)

label_3 = Label(text="Km")
label_3.grid(column=2, row=1)

button = Button(text="Calculate", command=mile_to_km)
button.grid(column=1, row=2)

entry = Entry(width=5)
entry.insert(END, string="0")
entry.grid(column=1, row=0)

label_4 = Label(text="0")
label_4.grid(column=1, row=1)

window.mainloop()