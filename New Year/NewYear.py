from tkinter import*
from tkinter import messagebox
from PIL import ImageTk, Image #type: ignore






def is_leap_year():
    year= int(text_entry.get())
    if((year%400 == 0 or year%100 != 0 and year %4 == 0)):
        messagebox.showinfo("Yeaaa", f"{year} is a Leap Year")
    else:
        messagebox.showerror("pong pong", f"{year} is Not a Leap Year")
        




root=Tk()
root.title('Leap Year Calculator')
root.geometry('300x400')
root.configure(background='black')
root.iconphoto(False, PhotoImage(file='New Year/logo.png'))
root.resizable(0,0)
text_label= Label(root,text='Enter Year: ', bg='black' ,fg='white')
text_label.pack()





text_entry= Entry(root, width = 30)
text_entry.pack()

check_btn = Button(root, text = 'Check', command=is_leap_year)
check_btn.pack(pady=(20,20))

root.mainloop()