from tkinter import *
import pandas
from PIL import ImageTk, Image
from tkinter import  messagebox
from states import states, states_dictionary


MY_FONT_TITLE = ("Avenir Next", 40)
MY_FONT=("Morriweather", 16, "bold")
MY_FONT_SUBTITLE=("Avenir Next", 16, "bold")

BACKGROUND= "#DFE6E9"
FOREGROUND="#2D3436"
HOTDEAL="#2D3436"


window = Tk()
window.title("Shopping Bag")
window.geometry('800x400')
window.config(padx=30, pady=30)

# open an image
my_pic = Image.open("image.png")

# resize the image

resized =my_pic.resize((800, 400), Image.ANTIALIAS)

# set image as a background

bg = ImageTk.PhotoImage(resized)
canvas1= Canvas(window, width=800, height=400)
canvas1.pack(fill="both", expand=True)
canvas1.create_image(0, 0, image=bg, anchor="nw")


# Read CSV FILE

data=pandas.read_csv("tax.csv")

def selected(drop):

    state = states_dictionary.get(clicked.get(), "Alaska")
    return data[data.State==state].stateTaxRate

# CALCULATE

def calculate():

    state_tax = selected(drop)

    try:
        price = float(original_price_entry.get())
        discount = float(discount_entry.get())
        extra_discount=float(extra_discount_entry.get())
        custom_tax = float(custom_tax_entry.get())

    except ValueError:
        messagebox.showinfo(title="Oops", message="Please insert a valid number. Do not use commas/characters."
                                                  "Put 0 instead of leaving the space blank")
    else:
        discount = discount / 100
        extra_discount = extra_discount / 100
        custom_tax = custom_tax / 100
        total = price - price * discount
        total = total - total * extra_discount
        total = total + total * custom_tax
        total = total + total * (state_tax/100)
        total = round(total.values.tolist()[0], 2)
        total_entry.config(text=total)




""""----------------------------------------------------------GUI------------------------------------------------------"""


title = canvas1.create_text(60, 140, text="Original Price:", font= MY_FONT)

total_button = Button(text="Total: \n (click here)", font=MY_FONT_SUBTITLE, bg=BACKGROUND, relief="groove", highlightthickness=0,fg=FOREGROUND, command=calculate)
total_button.place(x=500, y=200)

your_shopping_bag_total_label = Label(text="Your Shopping Bag Total: ", font=MY_FONT, padx=30, bg=BACKGROUND, fg=FOREGROUND)

hot_deal = canvas1.create_text(400, 50, text="Get Your Hot Deal", font= MY_FONT_TITLE)

discount = canvas1.create_text(300, 140, text="Discount, %:", font= MY_FONT)

custom_tax = canvas1.create_text(65, 220, text="Custom Tax, %:", font= MY_FONT)

extra_discount = canvas1.create_text(540, 140, text="Extra Discount, %:", font= MY_FONT)

state = canvas1.create_text(300, 220, text="State Tax:", font= MY_FONT)


# Entries

original_price_entry = Entry(width=6, highlightthickness = 0)
original_price_entry.focus()
original_price_entry.place(x=135, y=130, width=70, height=30)

discount_entry = Entry(width=6, highlightthickness = 0)
discount_entry.insert(0, "0")
discount_entry.place(x=370, y=130, width=70, height=30)

extra_discount_entry = Entry(width=6, highlightthickness = 0)
extra_discount_entry.place(x=640, y=130, width=70, height=30)
extra_discount_entry.insert(0, "0")

custom_tax_entry = Entry(width=6, highlightthickness = 0)
custom_tax_entry.insert(0, "0")
custom_tax_entry.place(x=135, y=205, width=70, height=30)

total_entry = Label(width=6, highlightthickness = 0)
total_entry.place(x=640, y=200, width=70, height=30)

your_shopping_bag_total_entry = Entry(width=6, highlightthickness = 0)
#your_shopping_bag_total_entry.grid(column=6, row=0)


# Drop_down menu

clicked = StringVar()
clicked.set("STATE")
drop = OptionMenu(window, clicked, *states, command=selected)
drop.config(width=4)
drop.place(x=370, y=205, width=70, height=30)


window.mainloop()


