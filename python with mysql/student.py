from tkinter import *
import time
import ttkthemes
from tkinter import ttk, messagebox, filedialog
import pymysql
import pandas

# exit button command


def ext():
    result = messagebox.askyesno('confirm', 'Do you want to exit?')
    if result:
        window.destroy()
    else:
        pass

# export button command


def export_data():
    url = filedialog.asksaveasfilename(defaultextension='.csv')
    indexing = student_table.get_children()
    new_list = []
    for index in indexing:
        content = student_table.item(index)
        data_list = content['values']
        new_list.append(data_list)

    table = pandas.DataFrame(new_list, columns=['ID', 'First Name',  'Last Name', 'Father Name',
                             'DOB',  'Address',  'Gender',  'Phone',  'Attendence',  'Added Date',  'Added Time'])
    table.to_csv(url, index=False)
    messagebox.showinfo('Success', 'Data successfully saved')

# update button command


def update():
    def update_btn():
        query = 'update student set first_name=%s , last_name=%s , father_name=%s , DOB=%s , address =%s , gender=%s ,   phone=%s , attendence=%s where id=%s'
        my_cursor.execute(query, (fname_entry.get(), lname_entry.get(), fthrnm_entry.get(),  dob_entry.get(
        ), adrs_entry.get(), gndr_entry.get(), phone_entry.get(), atndnc_entry.get(), id_entry.get()))
        con.commit()
        messagebox.showinfo(
            'updated', f'id {id_entry.get()} is modify successfully', parent=updt_window)
        updt_window.destroy()
        show()

    updt_window = Toplevel()
    updt_window.grab_set()
    updt_window.geometry('400x570+280+30')
    updt_window.title('Update DATA')
    updt_window.resizable(0, 0)

    id_lbl = Label(updt_window, text='ID', font=('open sans', 16))
    id_lbl.grid(row=0, column=0, padx=15, pady=10, sticky=W)
    id_entry = Entry(updt_window, font=('open sans', 16), bd=1)
    id_entry.grid(row=0, column=1)

    fname_lbl = Label(updt_window, text='first Name', font=('open sans', 16))
    fname_lbl.grid(row=1, column=0, padx=15, pady=10, sticky=W)
    fname_entry = Entry(updt_window, font=('open sans', 16), bd=1)
    fname_entry.grid(row=1, column=1)

    lname_lbl = Label(updt_window, text='Last Name', font=('open sans', 16))
    lname_lbl.grid(row=2, column=0, padx=15, pady=10, sticky=W)
    lname_entry = Entry(updt_window, font=('open sans', 16), bd=1)
    lname_entry.grid(row=2, column=1)

    fthrnm_lbl = Label(updt_window, text='F Name', font=('open sans', 16))
    fthrnm_lbl.grid(row=3, column=0, padx=15, pady=10, sticky=W)
    fthrnm_entry = Entry(updt_window, font=('open sans', 16), bd=1)
    fthrnm_entry.grid(row=3, column=1)

    dob_lbl = Label(updt_window, text='DOB', font=('open sans', 16))
    dob_lbl.grid(row=4, column=0, padx=15, pady=10, sticky=W)
    dob_entry = Entry(updt_window, font=('open sans', 16), bd=1)
    dob_entry.grid(row=4, column=1)

    adrs_lbl = Label(updt_window, text='Address', font=('open sans', 16))
    adrs_lbl.grid(row=5, column=0, padx=15, pady=10, sticky=W)
    adrs_entry = Entry(updt_window, font=('open sans', 16), bd=1)
    adrs_entry.grid(row=5, column=1)

    gndr_lbl = Label(updt_window, text='Gender', font=('open sans', 16))
    gndr_lbl.grid(row=6, column=0, padx=15, pady=10, sticky=W)
    gndr_entry = Entry(updt_window, font=('open sans', 16), bd=1)
    gndr_entry.grid(row=6, column=1)

    phone_lbl = Label(updt_window, text='Phone', font=('open sans', 16))
    phone_lbl.grid(row=7, column=0, padx=15, pady=10, sticky=W)
    phone_entry = Entry(updt_window, font=('open sans', 16), bd=1)
    phone_entry.grid(row=7, column=1)

    atndnc_lbl = Label(updt_window, text='Attendence', font=('open sans', 16))
    atndnc_lbl.grid(row=8, column=0, padx=15, pady=10, sticky=W)
    atndnc_entry = Entry(updt_window, font=('open sans', 16), bd=1)
    atndnc_entry.grid(row=8, column=1)

    sbmt_btn = ttk.Button(updt_window, text='Update', command=update_btn)
    sbmt_btn.grid(row=9, columnspan=2, pady=15)

    indexing = student_table.focus()

    content = student_table.item(indexing)
    listdata = content['values']
    id_entry.insert(0, listdata[0])
    fname_entry.insert(0, listdata[1])
    lname_entry.insert(0, listdata[2])
    fthrnm_entry.insert(0, listdata[3])
    dob_entry.insert(0, listdata[4])
    adrs_entry.insert(0, listdata[5])
    gndr_entry.insert(0, listdata[6])
    phone_entry.insert(0, listdata[7])
    atndnc_entry.insert(0, listdata[8])

# display button command


def show():
    query = 'select * from student'
    my_cursor.execute(query)
    ftch_data = my_cursor.fetchall()
    student_table.delete(*student_table.get_children())

    for data in ftch_data:
        data_list = list(data)
        student_table.insert('', END, values=data_list)

# erase button command


def dlt():
    indexing = student_table.focus()
    print(indexing)
    content = student_table.item(indexing)
    content_id = content['values'][0]
    query = 'delete from student where id=%s'
    my_cursor.execute(query, content_id)
    con.commit()
    messagebox.showinfo('deleted', f'id {content_id} is deleted')

# explore button command


def srch():
    def search_student():
        query = 'select * from student where id=%s or first_name=%s or last_name=%s or father_name=%s or gender=%s or address=%s'
        my_cursor.execute(query, (id_entry.get(), fname_entry.get(), lname_entry.get(
        ), fthrnm_entry.get(), gndr_entry.get(), adrs_entry.get()))
        ftch_data = my_cursor.fetchall()
        student_table.delete(*student_table.get_children())

        for data in ftch_data:
            student_table.insert('', END, values=data)

    srch_window = Toplevel()
    srch_window.grab_set()
    srch_window.geometry('400x570+280+30')
    srch_window.title('Explore DATA')
    srch_window.resizable(0, 0)

    id_lbl = Label(srch_window, text='ID', font=('open sans', 16))
    id_lbl.grid(row=0, column=0, padx=15, pady=10, sticky=W)
    id_entry = Entry(srch_window, font=('open sans', 16), bd=1)
    id_entry.grid(row=0, column=1)

    fname_lbl = Label(srch_window, text='first Name', font=('open sans', 16))
    fname_lbl.grid(row=1, column=0, padx=15, pady=10, sticky=W)
    fname_entry = Entry(srch_window, font=('open sans', 16), bd=1)
    fname_entry.grid(row=1, column=1)

    lname_lbl = Label(srch_window, text='Last Name', font=('open sans', 16))
    lname_lbl.grid(row=2, column=0, padx=15, pady=10, sticky=W)
    lname_entry = Entry(srch_window, font=('open sans', 16), bd=1)
    lname_entry.grid(row=2, column=1)

    fthrnm_lbl = Label(srch_window, text='F Name', font=('open sans', 16))
    fthrnm_lbl.grid(row=3, column=0, padx=15, pady=10, sticky=W)
    fthrnm_entry = Entry(srch_window, font=('open sans', 16), bd=1)
    fthrnm_entry.grid(row=3, column=1)

    dob_lbl = Label(srch_window, text='DOB', font=('open sans', 16))
    dob_lbl.grid(row=4, column=0, padx=15, pady=10, sticky=W)
    dob_entry = Entry(srch_window, font=('open sans', 16), bd=1)
    dob_entry.grid(row=4, column=1)

    adrs_lbl = Label(srch_window, text='Address', font=('open sans', 16))
    adrs_lbl.grid(row=5, column=0, padx=15, pady=10, sticky=W)
    adrs_entry = Entry(srch_window, font=('open sans', 16), bd=1)
    adrs_entry.grid(row=5, column=1)

    gndr_lbl = Label(srch_window, text='Gender', font=('open sans', 16))
    gndr_lbl.grid(row=6, column=0, padx=15, pady=10, sticky=W)
    gndr_entry = Entry(srch_window, font=('open sans', 16), bd=1)
    gndr_entry.grid(row=6, column=1)

    phone_lbl = Label(srch_window, text='Phone', font=('open sans', 16))
    phone_lbl.grid(row=7, column=0, padx=15, pady=10, sticky=W)
    phone_entry = Entry(srch_window, font=('open sans', 16), bd=1)
    phone_entry.grid(row=7, column=1)

    atndnc_lbl = Label(srch_window, text='Attendence', font=('open sans', 16))
    atndnc_lbl.grid(row=8, column=0, padx=15, pady=10, sticky=W)
    atndnc_entry = Entry(srch_window, font=('open sans', 16), bd=1)
    atndnc_entry.grid(row=8, column=1)

    sbmt_btn = ttk.Button(srch_window, text='Explore', command=search_student)
    sbmt_btn.grid(row=9, columnspan=2, pady=15)

# enroll button command


def add_data():
    def submt():
        if id_entry.get() == '' or fname_entry.get() == '' or lname_entry.get() == '' or fthrnm_entry.get() == '' or dob_entry.get() == '' or adrs_entry.get() == '' or gndr_entry.get() == '' or phone_entry.get() == '' or atndnc_entry.get() == '':
            messagebox.showerror(
                'warning', 'All fields should be fill ', parent=add_window)
        else:
            crnt_date = time.strftime('%d/%m/%y')
            crnt_time = time.strftime('%H:%M:%S')
            query = 'insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            my_cursor.execute(query, (id_entry.get(), fname_entry.get(), lname_entry.get(), fthrnm_entry.get(),  dob_entry.get(
            ), adrs_entry.get(), gndr_entry.get(), phone_entry.get(), atndnc_entry.get(), crnt_date, crnt_time))
            con.commit()
            result = messagebox.askyesno(
                'Confirmation', 'Are you sure to add that data', parent=add_window)
            if result:
                id_entry.delete(0, END)
                fname_entry.delete(0, END)
                lname_entry.delete(0, END)
                fthrnm_entry.delete(0, END)
                dob_entry.delete(0, END)
                adrs_entry.delete(0, END)
                gndr_entry.delete(0, END)
                phone_entry.delete(0, END)
                atndnc_entry.delete(0, END)
            else:
                pass

            show()

    add_window = Toplevel()
    add_window.grab_set()
    add_window.geometry('400x570+280+30')
    add_window.title('ADD DATA')
    add_window.resizable(0, 0)

    id_lbl = Label(add_window, text='ID', font=('open sans', 16))
    id_lbl.grid(row=0, column=0, padx=15, pady=10, sticky=W)
    id_entry = Entry(add_window, font=('open sans', 16), bd=1)
    id_entry.grid(row=0, column=1)

    fname_lbl = Label(add_window, text='first Name', font=('open sans', 16))
    fname_lbl.grid(row=1, column=0, padx=15, pady=10, sticky=W)
    fname_entry = Entry(add_window, font=('open sans', 16), bd=1)
    fname_entry.grid(row=1, column=1)

    lname_lbl = Label(add_window, text='Last Name', font=('open sans', 16))
    lname_lbl.grid(row=2, column=0, padx=15, pady=10, sticky=W)
    lname_entry = Entry(add_window, font=('open sans', 16), bd=1)
    lname_entry.grid(row=2, column=1)

    fthrnm_lbl = Label(add_window, text='F Name', font=('open sans', 16))
    fthrnm_lbl.grid(row=3, column=0, padx=15, pady=10, sticky=W)
    fthrnm_entry = Entry(add_window, font=('open sans', 16), bd=1)
    fthrnm_entry.grid(row=3, column=1)

    dob_lbl = Label(add_window, text='DOB', font=('open sans', 16))
    dob_lbl.grid(row=4, column=0, padx=15, pady=10, sticky=W)
    dob_entry = Entry(add_window, font=('open sans', 16), bd=1)
    dob_entry.grid(row=4, column=1)

    adrs_lbl = Label(add_window, text='Address', font=('open sans', 16))
    adrs_lbl.grid(row=5, column=0, padx=15, pady=10, sticky=W)
    adrs_entry = Entry(add_window, font=('open sans', 16), bd=1)
    adrs_entry.grid(row=5, column=1)

    gndr_lbl = Label(add_window, text='Gender', font=('open sans', 16))
    gndr_lbl.grid(row=6, column=0, padx=15, pady=10, sticky=W)
    gndr_entry = Entry(add_window, font=('open sans', 16), bd=1)
    gndr_entry.grid(row=6, column=1)

    phone_lbl = Label(add_window, text='Phone', font=('open sans', 16))
    phone_lbl.grid(row=7, column=0, padx=15, pady=10, sticky=W)
    phone_entry = Entry(add_window, font=('open sans', 16), bd=1)
    phone_entry.grid(row=7, column=1)

    atndnc_lbl = Label(add_window, text='Attendence', font=('open sans', 16))
    atndnc_lbl.grid(row=8, column=0, padx=15, pady=10, sticky=W)
    atndnc_entry = Entry(add_window, font=('open sans', 16), bd=1)
    atndnc_entry.grid(row=8, column=1)

    sbmt_btn = ttk.Button(add_window, text='Submit', command=submt)
    sbmt_btn.grid(row=9, columnspan=2, pady=15)

# connect database button command


def conct_dtabse():
    def connect():
        global my_cursor, con
        try:
            con = pymysql.connect(
                host='localhost', user='root', password='admin123')
            my_cursor = con.cursor()  # host_entry.get(),  usrnm_entry.get(),   pswrd_entry.get()
            messagebox.showinfo(
                'Success', 'Connected Successfully', parent=conct_window)

        except:
            messagebox.showerror(
                'warning', 'invalid details', parent=conct_window)
            return
        try:
            query = 'create database school_hub'
            my_cursor.execute(query)

            query = 'use school_hub'
            my_cursor.execute(query)

            query = 'create table student(id int not null primary key, first_name varchar(30), last_name varchar(30),\
                                                    father_name varchar(50) , DOB varchar(20), Address varchar(200),gender varchar(14), phone int, attendence varchar(20),\
                                                    added_date varchar(20), added_time varchar(20))'
            my_cursor.execute(query)
        except:
            query = 'use school_hub'
            my_cursor.execute(query)
        conct_window.destroy()
        add_student.config(state=NORMAL)
        dlt_student.config(state=NORMAL)
        show_student.config(state=NORMAL)
        updt_student.config(state=NORMAL)
        srch_student.config(state=NORMAL)
        exprt_student.config(state=NORMAL)
        exit_student.config(state=NORMAL)

    conct_window = Toplevel()
    conct_window.grab_set()
    conct_window.geometry('420x220+480+200')
    conct_window.title('Connection')
    conct_window.resizable(0, 0)

    host_lbl = Label(conct_window, text='Host', font=('open sans', 18))
    host_lbl.grid(row=0, column=0, padx=20, pady=20)
    host_entry = Entry(conct_window, font=('open sans', 16), bd=1)
    host_entry.grid(row=0, column=1)

    usrnm_lbl = Label(conct_window, text='Username', font=('open sans', 18))
    usrnm_lbl.grid(row=1, column=0, padx=20)
    usrnm_entry = Entry(conct_window, font=('open sans', 16), bd=1)
    usrnm_entry.grid(row=1, column=1)

    pswrd_lbl = Label(conct_window, text='Password', font=('open sans', 18))
    pswrd_lbl.grid(row=2, column=0, padx=20, pady=20)
    pswrd_entry = Entry(conct_window, font=('open sans', 16), bd=1)
    pswrd_entry.grid(row=2, column=1)

    cnct_btn = ttk.Button(conct_window, text='Connect',
                          width=8, command=connect)
    cnct_btn.grid(row=3, columnspan=2)


count = 0
text = ''
# function of sliding text (student hub)


def slider():
    global text, count
    if count == len(slidr_txt):
        count = 0
        text = ''
    text = text+slidr_txt[count]
    slidr_lbl.config(text=text)
    count += 1
    slidr_lbl.after(300, slider)

# def clock():
#     date=time.strftime('%d/%m/%y')
#     crnt_time=time.strftime('%H:%M:%S')
#     datetime_lbl.config(text=f'  Date: {date} \n Time: {crnt_time}')
#     datetime_lbl.after(1000,clock)


window = ttkthemes.ThemedTk()
window.get_themes()
window.set_theme('itft1')
window.geometry('1200x700+0+0')
window.title('Student Hub')
window.resizable(0, 0)

# datetime_lbl=Label(window,font=('open sans', 18))
# datetime_lbl.place(x=10,y=15)
# clock()

logo_img = PhotoImage(file='images/main_logo.png',)
logo_lbl = Label(window, image=logo_img)
logo_lbl.place(x=40, y=22)

slidr_txt = 'Student Hub'
slidr_lbl = Label(window, text=slidr_txt, width=25, font=(
    'open sans', 30, 'italic bold'), fg="gray11")
slidr_lbl.place(x=200, y=15)
slider()

cnct_btn = ttk.Button(window, text='Connect to database',
                      width=20, cursor='hand2', command=conct_dtabse)
cnct_btn.place(x=950, y=25)

left_frame = Frame(window, pady=10)
left_frame.place(x=40, y=75, width=300, height=580)

dshbord_img = PhotoImage(file='images/logo123.png')
dshbord_lbl = Label(left_frame, image=dshbord_img)
dshbord_lbl.grid(row=0, column=0, pady=20)

add_student = ttk.Button(left_frame, text='Enroll',
                         width=13, state=DISABLED, command=add_data)
add_student.grid(row=1, column=0, pady=23)

srch_student = ttk.Button(left_frame, text='Explore',
                          width=13, state=DISABLED, command=srch)
srch_student.grid(row=2, column=0, pady=13,)

dlt_student = ttk.Button(left_frame, text='Erase',
                         width=13, state=DISABLED, command=dlt)
dlt_student.grid(row=3, column=0, pady=13,)

updt_student = ttk.Button(left_frame, text='Update',
                          width=13, state=DISABLED, command=update)
updt_student.grid(row=4, column=0, pady=13,)

show_student = ttk.Button(left_frame, text='Display',
                          width=13, state=DISABLED, command=show)
show_student.grid(row=5, column=0, pady=13,)

exprt_student = ttk.Button(left_frame, text='Export',
                           width=13, state=DISABLED, command=export_data)
exprt_student.grid(row=6, column=0, pady=13,)

exit_student = ttk.Button(left_frame, text='Exit',
                          width=13, state=DISABLED, command=ext)
exit_student.grid(row=7, column=0, pady=13,)

right_frame = Frame(window, background='white', bd=4)
right_frame.place(x=200, y=110, width=950, height=520)

scrl_brX = Scrollbar(right_frame, orient=HORIZONTAL)
scrl_brY = Scrollbar(right_frame, orient=VERTICAL)
scrl_brX.pack(side='bottom', fill=X)
scrl_brY.pack(side='right', fill=Y)

student_table = ttk.Treeview(right_frame, columns=('id', 'first name', 'last name',
                                                   'father name', 'DOB', 'Address', 'gender', 'phone no', 'attendence',
                                                   'added date', 'added time'), xscrollcommand=scrl_brX.set,
                             yscrollcommand=scrl_brY.set)
scrl_brX.config(command=student_table.xview)
scrl_brY.config(command=student_table.yview)
student_table.pack(fill='both', expand=1)

student_table.heading('id', text='ID')
student_table.heading('first name', text='First Name')
student_table.heading('last name', text='Last Name')
student_table.heading('father name', text='Father Name')
student_table.heading('DOB', text='DOB')
student_table.heading('Address', text='Address')
student_table.heading('gender', text='Gender')
student_table.heading('phone no', text='Phone')
student_table.heading('attendence', text='Attendence')
student_table.heading('added date', text='Added Date')
student_table.heading('added time', text='Added Time')

student_table.column('id', width=50, anchor=CENTER)
student_table.column('first name', width=200, anchor=CENTER)
student_table.column('last name', width=200, anchor=CENTER)
student_table.column('father name', width=200, anchor=CENTER)
student_table.column('DOB', width=200, anchor=CENTER)
student_table.column('Address', width=200, anchor=CENTER)
student_table.column('gender', width=200, anchor=CENTER)
student_table.column('phone no', width=200, anchor=CENTER)
student_table.column('attendence', width=200, anchor=CENTER)
student_table.column('added date', width=200, anchor=CENTER)
student_table.column('added time', width=200, anchor=CENTER)

student_table.config(show='headings')

style = ttk.Style()

style.configure('Treeview', font=('open sans', 14), background='sky blue',
                fieldbackground='sky blue', foreground='black', rowheight=25)


window.mainloop()
