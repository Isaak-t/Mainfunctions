from tkinter import filedialog as fd

def select_files():
    global filename
    global myimage
    filetypes = (('image files', '*.jpg .png'), ('All files', '.*'))
    filename = fd.askopenfilename(title='Open files', initialdir='/', filetypes=filetypes)
    print(filename)
    return filename