from tkinter import *  # help us in graphical user interface
# PIL(python image library) help to import jpg images
from tkinter import messagebox
from PIL import ImageTk, Image


def login():
    if usrnm_entry.get()=='' or pswrd_entry.get()=='':
        messagebox.showerror('Error','Fields cannot be empty')

    elif usrnm_entry.get()=='Saad' and pswrd_entry.get()=='1234':
        messagebox.showinfo('success','Welcome')
        root.destroy()
        import student

    else:
        messagebox.showerror('Error','Plz enter valid info')


root = Tk()
root.geometry('1200x700+0+0')  # window size
root.title('Login To Student Hub')
root.resizable(False, False)


img = Image.open('images/Pic 1.jpg')
rsiz_img = img.resize((1200, 700))
bg_img = ImageTk.PhotoImage(rsiz_img)
bg_lbl = Label(root, image=bg_img)
bg_lbl.place(x=0, y=0)

login_frame = Frame(root, background='gray93')  # container
login_frame.place(x=150, y=90)

logo_img = PhotoImage(file='images/logo.png',)
logo_lbl = Label(login_frame, image=logo_img, background='gray93')
logo_lbl.grid(row=0, column=0, columnspan=2, pady=30)


usrname_image = PhotoImage(file='images/usrname.png')
usrnm_lbl = Label(login_frame, image=usrname_image, text='Username', compound=LEFT,
                  font=('open sans', 20, 'bold'), background='gray93')
usrnm_lbl.grid(row=1, column=0, padx=20)

usrnm_entry = Entry(login_frame, font=(
    'open sans', 17), bd=2, background='gray92')
usrnm_entry.grid(row=1, column=1, padx=20)

pswrd_image = PhotoImage(file='images/password.png')
pswrd_lbl = Label(login_frame, image=pswrd_image, text='Password', compound=LEFT,
                  font=('open sans', 20, 'bold'), background='gray93')
pswrd_lbl.grid(row=2, column=0, padx=20, pady=20)

pswrd_entry = Entry(login_frame, font=(
    'open sans', 17), bd=2, background='gray92')
pswrd_entry.grid(row=2, column=1, padx=20)

login_btn = Button(login_frame, text='LOG IN',
                   font=('open sans', 16), width=15, background='light sky blue', fg='white', cursor='hand2', activebackground='light sky blue', activeforeground='white', command=login)
login_btn.grid(row=3, column=1, pady=20)


root.mainloop()
