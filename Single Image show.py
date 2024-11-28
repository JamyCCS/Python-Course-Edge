from tkinter import *
from PIL import ImageTk,Image # type: ignore

root = Tk()
root.title('Single Image Viewer')
root.geometry('450x450')
root.resizable(350,350)
root.configure(background='black')
image = Image.open("1057363.png")
resized_image=image.resize((250,350))
final_image= ImageTk.PhotoImage(resized_image)
image_label=Label(root,image=final_image)
image_label.pack()

root.mainloop()
