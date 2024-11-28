from tkinter import *
import os 
from PIL import Image, ImageTk


files=os.listdir('Image Show/Wallpapers')
counter = 1
def handle_next_btn():
    global counter
    image_label.config(image=image_array[counter%len(image_array)])
    counter+=1


root = Tk()
root.title('Single Image Viewer')
root.geometry('450x450')
root.resizable(350,350)
root.configure(background='black')

image_array = []

for file in files:
    image = Image.open(os.path.join('Image Show/Wallpapers',file))
    resized_image = image.resize((250,350))
    image_array.append(ImageTk.PhotoImage(resized_image))

image_label=Label(root, image = image_array[0])
image_label.pack()

next_btn= Button(root , text='Next', bg= 'white', fg='black' , command = handle_next_btn)
next_btn.pack()
root.mainloop()
