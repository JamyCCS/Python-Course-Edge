from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
        process_text(text)



def save_output(output_text):
    output_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if output_path:
        with open(output_path, 'w', encoding='utf-8') as result:
            result.write(output_text)
        messagebox.showinfo("Success", "Summary saved successfully!")

def process_text(text):
    sentence_list = text.split('.')
    Total_Sentences = len(sentence_list)
    longest_sentence = max(sentence_list)
    shortest_sentence = min(sentence_list)
    longest_sentence_size = len(longest_sentence.split(" "))
    shortest_sentence_size = len(shortest_sentence.split(" "))
    output_text = (
        f"Total Sentences: {Total_Sentences}\n"
        f"Longest Sentence: '{longest_sentence}'\nLongest Length: {longest_sentence_size} words\n"
        f"Shortest Sentence: '{shortest_sentence}'\nShortest Length: {shortest_sentence_size} words\n"
        )
    save_output(output_text)




root= Tk()
root.title("Text Summary Generator")
root.geometry('450x450')
root.resizable(0,0)
root.configure(background='black')


bg = Image.open("02_Obidullah_Mahmud_Jamy_Final/background.png")
bg=ImageTk.PhotoImage(bg)
image_label=Label(root,image=bg)
image_label.pack(fill=BOTH, expand=True)

open_button = Button(image_label, text="Open Text File",  fg="black", bg="white" ,command=open_file)
open_button.place(relx=0.5, rely=0.5,anchor=CENTER)

root.mainloop()