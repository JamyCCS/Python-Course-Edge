from tkinter import*
from tkinter import messagebox
from PIL import ImageTk, Image


email= 'obidullahjamy@gmail.com'
password= '1234abc'

def validity():
    check_mail= email_entry.get()
    check_pass= pass_entry.get()
    if check_mail==email and check_pass==password:
        messagebox.showinfo("user", "Login Succes")
    else :
        messagebox.showerror("Error", "Credential Mismatched")
     
root = Tk()
root.title('Facebook')
root.geometry('300x450')
root.resizable(0,0)
root.configure(background='white')

root.iconphoto(False, PhotoImage(file='Facebook Login/fb logo.png'))

fbimage = Image.open("Facebook Login/FB full.png")
resized_image=fbimage.resize((250,100))
final_image= ImageTk.PhotoImage(resized_image)
image_label=Label(root,image=final_image)
image_label.pack()


email_label= Label(root,text='Email : ', bg='White' ,fg='black')
email_label.pack()





email_entry= Entry(root, width = 25)
email_entry.pack()


pass_label= Label(root,text='Password : ', bg='White' ,fg='black')
pass_label.pack()



pass_entry= Entry(root, width = 25)
pass_entry.pack()


login_btn = Button(root, text = 'Login', command=validity)
login_btn.pack(pady=(20,20))









root.mainloop()