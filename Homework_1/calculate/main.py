try:
    import tkinter as tk
except ImportError:
    import tkinter as tk 
from tkinter.constants import DISABLED, NORMAL
from triangle_madang import triangle 


window = tk.Tk()

window.title("Calculate the area of a triangle!")
window.geometry('500x250')

tk.Label(text="Base of the triangle: ").grid(row=0)
tk.Label(text="Height of the triangle: ").grid(row=1)
tk.Label(text="Area is:").grid(row=3)

b_txt = tk.Entry(window, width=15)
b_txt.grid(column=1, row=0, padx=10, pady=10)
b_txt.focus()

h_txt = tk.Entry(window, width=15)
h_txt.grid(column=1, row=1, padx=10, pady=10)
h_txt.focus()

a_txt = tk.Entry(window, width=15, state=DISABLED)
a_txt.grid(column=1, row=3, padx=10, pady=10)
a_txt.focus()


def clicked():
    b_val = int(b_txt.get())
    h_val = int(h_txt.get())
    area = triangle.calculate_area(b_val, h_val)
    a_txt["state"] = NORMAL
    a_txt.insert(0, str(area))
    a_txt["state"] = DISABLED
    a_txt.configure({"disabledforeground": "black"})


btn = tk.Button(window, text="Calculate", command=clicked)
btn.grid(column=0,row=2)

 
window.mainloop()
