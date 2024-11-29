from tkinter import*

import math



#functions

def get_digit(digit):
    current=result_label['text']
    new=current+str(digit)
    result_label.config(text=new)

def clear():
    result_label.config(text='')

def get_operator(op):
    global first_number, operator
    first_number= float(result_label['text'])
    operator=op
    result_label.config(text='')
def get_pre_op(pop):
    if pop== "SIN":
        current= result_label["text"]
        new= math.sin(math.radians(int(current)))
        result_label.config(text=str(round(new,2)))
    elif pop=="COS":
         current= result_label["text"]
         new= math.cos(math.radians(int(current)))
         result_label.config(text=str(round(new,2)))
    elif pop== "TAN":
        current= result_label["text"]
        if (int(current))% 180==90:
            result_label.config(text="Math Error")
        else :
            new= math.tan(math.radians(int(current)))
            result_label.config(text=str(round(new,2)))
            
    else :
         current= result_label["text"]
         new= math.sqrt(int(current))
         result_label.config(text=str(round(new,2)))
    

def get_result():
    global second_number, first_number,operator
    second_number=float(result_label['text'])
    

    if operator=="+":
        result_label.config(text=str(first_number+second_number))
    
    elif operator=="-":
        result_label.config(text=str(first_number-second_number))

    elif operator=="x":
        result_label.config(text=str(first_number*second_number))
    

    else:
        if second_number==0:
            result_label.config(text='Math Error')
        else:
           result_label.config(text=str(first_number/second_number))
    

       


root=Tk()

root.title('Calculator')
root.geometry('420x500')
root.configure(bg='black')
root.resizable(0,0)



result_label=Label(root, text='',bg='black', fg='white')
result_label.grid(row=0,column=0,pady=(50,25), columnspan= 10, padx=(10,10),sticky='w')
result_label.config(font=('Times New Roman',25,'bold'))

#interface
#row 1 design
btn_7=Button(root,text='7', width=5,height=2,bg='gray',fg='white' ,command= lambda: get_digit(7))
btn_7.grid(row=1,column=0,padx=(10,5),pady=(5,5))
btn_7.config(font=('Times New Roman',15,'bold'))

btn_8=Button(root,text='8', width=5,height=2,bg='gray',fg='white',command=lambda: get_digit(8))
btn_8.grid(row=1,column=1,padx=(5,5),pady=(5,5))
btn_8.config(font=('Times New Roman',15,'bold'))

btn_9=Button(root,text='9', width=5,height=2,bg='gray',fg='white', command=lambda: get_digit(9))
btn_9.grid(row=1,column=2,padx=(5,5),pady=(5,5))
btn_9.config(font=('Times New Roman',15,'bold'))

btn_add=Button(root,text='+', width=5,height=2,bg='gray',fg='white',command=lambda :get_operator('+'))
btn_add.grid(row=1,column=3,padx=(5,5),pady=(5,5))
btn_add.config(font=('Times New Roman',15,'bold'))

btn_sin=Button(root,text='SIN', width=5,height=2,bg='gray',fg='white',command=lambda :get_pre_op('SIN'))
btn_sin.grid(row=1,column=4,padx=(5,10),pady=(5,5))
btn_sin.config(font=('Times New Roman',15,'bold'))


#row 2 design
btn_4=Button(root,text='4', width=5,height=2,bg='gray',fg='white', command=lambda: get_digit(4))
btn_4.grid(row=2,column=0,padx=(10,5),pady=(5,5))
btn_4.config(font=('Times New Roman',15,'bold'))

btn_5=Button(root,text='5', width=5,height=2,bg='gray',fg='white', command=lambda: get_digit(5))
btn_5.grid(row=2,column=1,padx=(5,5),pady=(5,5))
btn_5.config(font=('Times New Roman',15,'bold'))

btn_6=Button(root,text='6', width=5,height=2,bg='gray',fg='white', command=lambda: get_digit(6))
btn_6.grid(row=2,column=2,padx=(5,5),pady=(5,5))
btn_6.config(font=('Times New Roman',15,'bold'))

btn_sub=Button(root,text='-', width=5,height=2,bg='gray',fg='white',command=lambda :get_operator('-'))
btn_sub.grid(row=2,column=3,padx=(5,5),pady=(5,5))
btn_sub.config(font=('Times New Roman',15,'bold'))


btn_cos=Button(root,text='COS', width=5,height=2,bg='gray',fg='white',command=lambda :get_pre_op('COS'))
btn_cos.grid(row=2,column=4,padx=(5,10),pady=(5,5))
btn_cos.config(font=('Times New Roman',15,'bold'))

#row 3 design
btn_1=Button(root,text='1', width=5,height=2,bg='gray',fg='white', command=lambda: get_digit(1))
btn_1.grid(row=3,column=0,padx=(10,5),pady=(5,5))
btn_1.config(font=('Times New Roman',15,'bold'))

btn_2=Button(root,text='2', width=5,height=2,bg='gray',fg='white', command=lambda: get_digit(2))
btn_2.grid(row=3,column=1,padx=(5,5),pady=(5,5))
btn_2.config(font=('Times New Roman',15,'bold'))

btn_3=Button(root,text='3', width=5,height=2,bg='gray',fg='white', command=lambda: get_digit(3))
btn_3.grid(row=3,column=2,padx=(5,5),pady=(5,5))
btn_3.config(font=('Times New Roman',15,'bold'))

btn_mul=Button(root,text='X', width=5,height=2,bg='gray',fg='white',command=lambda :get_operator('x'))
btn_mul.grid(row=3,column=3,padx=(5,5),pady=(5,5))
btn_mul.config(font=('Times New Roman',15,'bold'))

btn_tan=Button(root,text='TAN', width=5,height=2,bg='gray',fg='white',command=lambda :get_pre_op('TAN'))
btn_tan.grid(row=3,column=4,padx=(5,10),pady=(5,5))
btn_tan.config(font=('Times New Roman',15,'bold'))
#row 4 design
btn_clr=Button(root,text='C', width=5,height=2,bg='gray',fg='white',command=clear)
btn_clr.grid(row=4,column=0,padx=(10,5),pady=(5,5))
btn_clr.config(font=('Times New Roman',15,'bold'))

btn_0=Button(root,text='0', width=5,height=2,bg='gray',fg='white', command=lambda: get_digit(0))
btn_0.grid(row=4,column=1,padx=(5,5),pady=(5,5))
btn_0.config(font=('Times New Roman',15,'bold'))

btn_equal=Button(root,text='=', width=5,height=2,bg='gray',fg='white',command=get_result)
btn_equal.grid(row=4,column=2,padx=(5,5),pady=(5,5))
btn_equal.config(font=('Times New Roman',15,'bold'))

btn_div=Button(root,text='/', width=5,height=2,bg='gray',fg='white',command=lambda :get_operator('/'))
btn_div.grid(row=4,column=3,padx=(5,10),pady=(5,5))
btn_div.config(font=('Times New Roman',15,'bold'))

btn_dot=Button(root,text='.', width=5,height=2,bg='gray',fg='white',command=lambda: get_digit('.'))
btn_dot.grid(row=4,column=4,padx=(5,10),pady=(5,5))
btn_dot.config(font=('Times New Roman',15,'bold'))

#row 5 design

btn_root=Button(root,text='√', width=32,height=2,bg='gray',fg='white', command=lambda :get_pre_op('√'))
btn_root.grid(row=5,column=0,columnspan= 5,padx=(10,5),pady=(5,5))
btn_root.config(font=('Times New Roman',15,'bold'))


root.mainloop()