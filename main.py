import tkinter as tk
from tkinter import ttk
from tkinter import*
from PIL import Image, ImageFilter
import random
import notmain

root = tk.Tk()
root.geometry('400x300')

def get_file_name():
    global file_name
    file_name = notmain.select_files()

def My_image():
    my_image = Image.open(file_name)
    rows = my_image.size[0]
    cols = my_image.size[1]
    print(rows, cols)

    px = my_image.load()
    # px[9, 9] = (0, 0, 0)

    for i in range(0, rows):
        start = random.randint(0, rows)
        end = random.randint(0, cols)
        nub = random.randint(1, 2)

        if i % 2 == 0:
            start = 0
        else:
            start = i

        for j in range(start, cols, nub):
            red_str = slider_red.get()
            red = int(red_str)
            green_str = slider_green.get()
            green = int(green_str)
            blue_str = slider_blue.get()
            blue = int(blue_str)
            px[i, j] = (red, green, blue)
            if j % 2 == 0:
                red = 0
                green = 0
                blue = 0
            else:
                red = 255
                green = 255
                blue = 255

    my_image.show()

def Contour():
    my_image = Image.open(file_name)
    contour = my_image.filter(ImageFilter.CONTOUR)
    contour.show()

def Emboss():
    my_image = Image.open(file_name)
    emboss = my_image.filter(ImageFilter.EMBOSS)
    emboss.show()

#emboss button
embossbutton = Checkbutton(root, onvalue=1, offvalue=0, text='Emboss image', command=Emboss)
embossbutton.grid(row=1,column=1)

#contour button
contourbutton = Checkbutton(root, onvalue=1, offvalue=0, text='Contour image', command=Contour)
contourbutton.grid(row=0, column=1)

#open file button
open_button = ttk.Button(root, text='Open Files', command=get_file_name)
open_button.grid(row=0, column=0)

#glitch button
open_button = ttk.Button(root, text='Glitch it', command=My_image)
open_button.grid(row=4, column=0)

#red slider
slider_red = Scale(root, from_=0, to=255, orient=HORIZONTAL, background='red', fg='grey')
slider_red.grid(row=1, column=0)

#green slider
slider_green = Scale(root, from_=0, to=255, orient=HORIZONTAL, background='green', fg='grey')
slider_green.grid(row=2, column=0)

#blue slider
slider_blue = Scale(root, from_=0, to=255, orient=HORIZONTAL, background='blue', fg='grey')
slider_blue.grid(row=3, column=0)

root.mainloop()