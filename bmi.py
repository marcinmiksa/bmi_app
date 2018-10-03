"""@BMI program"""

from tkinter import *


def bmi_counter():
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
top.geometry("440x420")
top.configure(background="#808080")  # gray background

height_label = Label(top, text="Wzrost")
height_label.place(x=20, y=20)
height_label.configure(height=2, width=6)

height_entry = Entry(top)
height_entry.place(x=90, y=20)


weight_label = Label(top, text="Waga")
weight_label.place(x=20, y=60)
weight_label.configure(height=2, width=6)

weight_entry = Entry(top)
weight_entry.place(x=90, y=60)

bmi_label = Label(top, text="BMI")
bmi_label.place(x=20, y=120)
bmi_label.configure(height=2, width=6)

bmi_result = Label(top, text="")
bmi_result.place(x=90, y=120)
bmi_result.configure(height=2, width=6)

bmi_button = Button(top, text="Oblicz BMI", command=bmi_counter)  # <-return result
bmi_button.configure(height=5, width=10)
bmi_button.place(x=190, y=120)

results_name = Label(top, text="Lista wynikow")
results_name.place(x=320, y=20)

results_list = Listbox(top)
results_list.place(x=320, y=50)
results_list.configure(height=9, width=10)

picture = LabelFrame(top)
picture.configure(height=150, width=390, background="#9f2929")
picture.place(x=20, y=220)

top.mainloop()
