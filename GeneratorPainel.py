import tkinter as tk
from tkinter import ttk
from tkinter import font
from PIL import ImageTk, Image
from tkinter import messagebox
import secrets
import time



# root
root = tk.Tk()
root.geometry('610x400')
root.resizable(False, False)
root.title('Terminal Strong Password')
root.iconbitmap('C:/Users/PEDRO MORAES/Downloads/George-Ui-Ancient-Legend-Virus-Shield.ico')
root.configure(bg='#050605')



custom_font = font.Font(family="Courier", size=14)
custom_font_dois = font.Font(family="Courier", size=6)
custom_font_tres = font.Font(family="Courier", size=7)


def atualizar_tempo():
    current_time = time.strftime("%H:%M:%S")
    time_label.config(text=current_time)
    root.after(1000, atualizar_tempo)


time_label = ttk.Label(root,
                       font=("Courier", 14),
                       foreground='#0BDA1C',
                       background='#1C1D1D'
                       )
time_label.place(
    x=50,
    y=1
)
time_label.pack()
def linkedin_clicou():
    my_linkedin = 'linkedin.com/in/pedro-konorath-736979278/'
    messagebox.showinfo("LinkedIn Profile", f"Visit my LinkedIn profile:\n{my_linkedin}")


linkedin_photo = ImageTk.PhotoImage(Image.open('C:/Users/PEDRO MORAES/Downloads/link.png'))
linkedin = ttk.Button(root,
                      text='Linkedin',
                      image=linkedin_photo,
                      cursor="hand2",
                      command=linkedin_clicou
                      )

linkedin.place(x=2,
               y=340
               )


komthe = ttk.Label(root,
                   text="""
                   A strong password is like a sturdy lock for your digital life.
                   """,
                   foreground='#3C3F42',
                   background='#050605',
                   font=custom_font_dois
                   )
komthe.place(
    x=71,
    y=100
)

output = ttk.Entry(root)
output.configure(width=30, background='#854EC4', foreground='#580792', font=custom_font)
output.place(x=154, y=130)


def criar_hash():
    hashrand = secrets.token_hex(14)
    output.delete(0, tk.END)  # Limpa o campo de entrada
    output.insert(0, hashrand)

def copy_buton():
    text_to_copy = output.get()
    root.clipboard_clear()
    root.clipboard_append(text_to_copy)


create_pass_button = ttk.Button(root,
                                text='CREATE PASS',
                                command=criar_hash
                                )
create_pass_button.place(x=235, y=170)
create_pass_button.configure(cursor="hand2")


copy_button = ttk.Button(root,
                         text='Copy',
                         command=copy_buton
                         )
copy_button.place(x=335, y=170)
copy_button.configure(cursor="hand2")



img3 = ImageTk.PhotoImage(Image.open('C:/Users/PEDRO MORAES/Downloads/berseker.png'))
panel = tk.Label(root, image = img3)
panel.place(
    y=300,
    x=300
)


img = ImageTk.PhotoImage(Image.open('C:/Users/PEDRO MORAES/Downloads/kali.png'))
panel = tk.Label(root, image = img)
panel.place(x=1,
            y=5
            )


atualizar_tempo()
root.mainloop()
