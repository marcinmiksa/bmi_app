"""@BMI program"""

from tkinter import *
from PIL import Image, ImageTk


def bmi_counter():
    """function print bmi"""
    try:
        height = float(height_entry.get())
        weight = float(weight_entry.get())
        bmi = (weight / height ** 2) * 100 * 100
        bmi = round(bmi, 2)
        result = bmi_result.configure(text=bmi), results_list.insert(1, bmi)
    except ValueError:
        return None
    return result


top = Tk()
top.title("BMI")
top.geometry("430x430")
top.resizable(0, 0)  # no resizable
top.configure(background="#808080")  # gray background

height_label = Label(top, text="Wzrost")
height_label.place(x=20, y=20)
height_label.configure(height=2, width=6)

height_entry = Entry(top)
height_entry.place(x=90, y=20, width=50, height=30)


weight_label = Label(top, text="Waga")
weight_label.place(x=20, y=60)
weight_label.configure(height=2, width=6)

weight_entry = Entry(top)
weight_entry.place(x=90, y=60, width=50, height=30)

bmi_label = Label(top, text="BMI")
bmi_label.place(x=20, y=120)
bmi_label.configure(height=2, width=6)

bmi_result = Label(top, text="")
bmi_result.place(x=90, y=120)
bmi_result.configure(height=2, width=6)

bmi_button = Button(top, text="Oblicz BMI", command=bmi_counter)
bmi_button.configure(height=9, width=15)
bmi_button.place(x=170, y=20)

results_name = Label(top, text="Lista wynikow")
results_name.place(x=320, y=20)

results_list = Listbox(top)
results_list.place(x=320, y=50)
results_list.configure(height=7, width=10)

"""show chart"""
canvas = Canvas(top, height=230, width=390)
jpg = Image.open("chart.jpg")
canvas.image = ImageTk.PhotoImage(jpg)
canvas.create_image(0, 0, image=canvas.image, anchor="nw")
canvas.place(x=20, y=180)

top.mainloop()
