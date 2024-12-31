from tkinter import *
from tkinter import messagebox
from sqlite3 import *
import home

def main():

    

    root=Tk()
    root.title('Login Page')
    root.geometry('800x500')
    root.configure(bg='white')
    root.resizable(0,0)

    # def create_login_table():
    #     con=connect('contact.db')
    #     cur=con.cursor()
    #     cur.execute('''
    #                 CREATE TABLE IF NOT EXISTS login(
    #                 username TEXT NOT NULL,
    #                 password TEXT NOT NULL
    #                 )''')
    #     cur.execute("insert into login (username, password) values(?,?)",('admin','admin'))
    #     con.commit()
    #     cur.close()


    # create_login_table()

    def handle_login_btn():
        con=connect('contact.db')
        cur=con.cursor()
        cur.execute("select * from login where username=? and password=?", (username_entry.get(), password_entry.get())) #? = %d
        result= cur.fetchone()
        if result is not None:
            messagebox.showinfo("user", "Login Successful")
            root.destroy()
            home.main()

        else:
            messagebox.showerror("Error", "Credential Mismatched")
            
        con.close()

            

    # def list_table():
    #     con=connect('contact.db')
    #     cur=con.cursor()
    #     cur.execute("select name from sqlite_master where type='table'")
    #     print(cur.fetchall())
    #     con.close()

    # list_table()

    # def list_table_data():
    #     con=connect('contact.db')
    #     cur=con.cursor()
    #     cur.execute("select * from login")
    #     print(cur.fetchall())
    #     con.close()
    
    # list_table_data()

    header_frame=Frame(root ,background='blue',height=60)  
    header_frame.pack(fill=X)
    header_label= Label(header_frame, text='My Contact Book', bg='blue', fg='white')
    header_label.pack(ipady=10)
    header_label.config(font=('Arial', 20,"bold"))


    content_frame=Frame(root, background='white')
    content_frame.pack(fill=BOTH, expand=True)

    login_frame=Frame(content_frame, background='grey')
    login_frame.place(relx=0.5, rely=0.5,anchor=CENTER) 

    login_label= Label(login_frame, text='Login Form', bg='blue', fg='white', width=30)
    login_label.grid(row=0, column=0, columnspan=2,ipady=5)

    username_label= Label(login_frame, text='Username', bg='white', fg='black')
    username_label.grid(row=1, column=0,ipady=10)

    username_entry= Entry(login_frame, bg='white', fg='black')
    username_entry.grid(row=1, column=1,ipady=10)

    password_label= Label(login_frame, text='Password', bg='white', fg='black')
    password_label.grid(row=2, column=0,ipady=10)

    password_entry= Entry(login_frame,  bg='white', fg='black')
    password_entry.grid(row=2, column=1,ipady=10)

    login_btn= Button(login_frame, text='Login', bg='blue', fg='white', width=30,command=handle_login_btn)
    login_btn.grid(row=3, column=0, columnspan=2,pady=2)




    
    

   

    root.mainloop()

if __name__ == '__main__':
    main()