from tkinter import *


def main():

    root=Tk()
    root.title('Home Page')
    root.geometry('800x500')
    root.configure(bg='white')
    root.resizable(0,0)
    

    # def create_login_table():
    #     con=connect('contact.db')
    #     cur=con.cursor()
    #     cur.execute('''
    #                 CREATE TABLE IF NOT EXISTS login(
    #                 username TEXT NOT NULL PRIMARY KEY,
    #                 password TEXT NOT NULL
    #                 )''')
    #     cur.execute("insert into login (username, password) values(?,?)",('admin','admin'))
    #     con.commit()
    #     cur.close()


    # create_login_table()


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




    root.mainloop()

if __name__ == '__main__':
    main()