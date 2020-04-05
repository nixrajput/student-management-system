import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessagebox
import cx_Oracle
import time

# ===========================================ROOT WINDOW START HERE==================================================
rootWindow = tk.Tk()
screen_width = rootWindow.winfo_screenwidth()
screen_height = rootWindow.winfo_screenheight()
rootWindow.geometry("%dx%d+%d+%d" % (screen_width, screen_height, 0, 0))
rootWindow.attributes('-fullscreen', True)
rootWindow.config(bg="#6d046c")
rootWindow.grid_columnconfigure(0, weight=1)

# ============================================GLOBAL VARIABLES==================================================
ROLL = tk.IntVar()
NAME = tk.StringVar()
CLASS = tk.StringVar()
MARKS = tk.DoubleVar()
GRADE = tk.StringVar()
SEX = tk.StringVar()
CITY = tk.StringVar()
SEARCH = tk.StringVar()
USERNAME = tk.StringVar()
PASSWORD = tk.StringVar()
time1 = ''


def App():
    # ========================================TITLE FRAME========================================================
    title_frame = tk.Frame(rootWindow, width=screen_width, bg="#6d046c")
    title_frame.grid(row=0, column=0)

    lbl_title = tk.Label(title_frame, text="Student Management System", font=('Times New Roman', 32),
                         bg="#6d046c",
                         fg="#f2f2f2")
    lbl_fill = tk.Label(title_frame, bg="#6d046c", fg="#f2f2f2",
                        text="==================================================================================")
    btn_exit2 = tk.Button(title_frame, text="X", activebackground="#6d046c", relief=tk.FLAT,
                          activeforeground="#f2f2f2", bg="#6d046c", fg="#f2f2f2", font=('calibri', 12),
                          width=3, height=1, cursor="hand2", command=lambda: Exit())
    btn_minimize = tk.Button(title_frame, text="-", activebackground="#6d046c", relief=tk.FLAT,
                             activeforeground="#f2f2f2", bg="#6d046c", fg="#f2f2f2", font=('calibri', 12),
                             width=3, height=1, cursor="hand2", command=lambda: Minimize())

    lbl_title.grid(row=0, column=0, ipadx=460)
    lbl_fill.grid(row=1, column=0, padx=20)
    btn_minimize.grid(row=0, column=1, pady=10)
    btn_exit2.grid(row=0, column=2, pady=10)

    # ==============================================LOGIN FRAME=================================================
    login_frame = tk.Frame(rootWindow, width=500, height=500, bg="#6d046c", highlightbackground="#f2f2f2",
                           highlightthickness=2)
    login_frame.grid(row=1, column=0, pady=200)

    lbl_menu = tk.Label(login_frame, text="ADMIN LOGIN", font=('calibri', 24, 'bold'), bg="#6d046c",
                        fg="#f2f2f2")
    lbl_username = tk.Label(login_frame, text="Username", bg="#6d046c", font=('calibri', 12, 'bold'),
                          fg="#f2f2f2")
    lbl_password = tk.Label(login_frame, text="Password", bg="#6d046c", font=('calibri', 12, 'bold'),
                          fg="#f2f2f2")
    entry_username = tk.Entry(login_frame, textvariable=USERNAME, width=32, font=('calibri', 12), justify='center')
    entry_password = tk.Entry(login_frame, textvariable=PASSWORD, width=32, font=('calibri', 12),
                              show="*", justify='center')
    btn_login = tk.Button(login_frame, text="Login", activebackground="#6d046c", relief=tk.FLAT,
                          activeforeground="#f2f2f2", bg="#f2f2f2", fg="#6d046c", font=('calibri', 12),
                          width=10, height=1, cursor="hand2", command=lambda: Login())

    lbl_menu.grid(row=0, column=0, padx=10, pady=20)
    lbl_username.grid(row=1, column=0, pady=5)
    entry_username.grid(row=2, column=0, padx=10, ipady=4)
    lbl_password.grid(row=3, column=0, pady=5)
    entry_password.grid(row=5, column=0, padx=10, ipady=4)
    btn_login.grid(row=6, column=0, padx=10, pady=30)

    rootWindow.mainloop()


# ===========================================ROOT WINDOW END HERE================================================

# ===========================================HOME WINDOW START HERE==============================================
def HomeWindow():
    global Home, tree
    global lbl_time
    Home = tk.Tk()
    # Home.title("Student Management System")

    Home.geometry("%dx%d+%d+%d" % (screen_width, screen_height, 0, 0))
    Home.attributes('-fullscreen', True)
    Home.config(bg="#6d046c")
    Home.grid_columnconfigure(0, weight=1)

    # ======================================TOP VIEW FRAME========================================================
    topView = tk.Frame(Home, width=screen_width, bg="#6d046c")
    topView.grid(row=0, column=0)

    lbl_titleHome = tk.Label(topView, text="Student Management System", font=('Times New Roman', 32),
                             bg="#6d046c", fg="#f2f2f2")
    lbl_fillHome = tk.Label(topView, bg="#6d046c", fg="#f2f2f2",
                            text="==================================================================================")
    btn_exit = tk.Button(topView, text="X", activebackground="#6d046c", relief=tk.FLAT,
                         activeforeground="#f2f2f2", bg="#6d046c", fg="#f2f2f2", font=('calibri', 12),
                         width=3, height=1, cursor="hand2", command=lambda: Exit())
    btn_minimize2 = tk.Button(topView, text="-", activebackground="#6d046c", relief=tk.FLAT,
                              activeforeground="#f2f2f2", bg="#6d046c", fg="#f2f2f2", font=('calibri', 12),
                              width=3, height=1, cursor="hand2", command=lambda: Minimize2())
    lbl_time = tk.Label(topView, compound=tk.CENTER, bg="#6d046c", fg="#f2f2f2", relief=tk.GROOVE,
                        font=('calibri', 16, 'bold'))

    lbl_titleHome.grid(row=0, column=0, ipadx=460)
    lbl_fillHome.grid(row=1, column=0)
    lbl_time.grid(row=1, column=0, pady=10, ipadx=20)
    btn_minimize2.grid(row=0, column=1, pady=10)
    btn_exit.grid(row=0, column=2, pady=10)

    # ======================================SEARCH VIEW FRAME====================================================
    searchView = tk.Frame(Home, width=screen_width, bg="#6d046c")
    searchView.grid(row=1, column=0)
    lbl_search = tk.Label(searchView, text="Search", bg="#6d046c", font=('calibri', 12, 'bold'),
                          fg="#f2f2f2")
    lbl_search.grid(row=0, column=0, padx=10, pady=10)
    search = tk.Entry(searchView, width=40, font=('calibri', 12))
    search.grid(row=0, column=1, pady=20, ipady=4)
    btn_search = tk.Button(searchView, textvariable=SEARCH, text="Search", activebackground="#6d046c", relief=tk.FLAT,
                           activeforeground="#f2f2f2", bg="#f2f2f2", fg="#6d046c", font=('calibri', 12),
                           width=8, height=1, cursor="hand2", command=lambda: Search())

    btn_search.grid(row=0, column=2, padx=20, pady=10)

    # ======================================MID VIEW FRAME========================================================
    midView = tk.Frame(Home, width=screen_width, bg="#6d046c")
    midView.grid(row=2, column=0)
    scrollbary = tk.Scrollbar(midView, orient=tk.VERTICAL)

    style = ttk.Style(midView)
    style.theme_use("default")
    style.configure("Treeview", background="#6d046c", fieldbackground="#6d046c", foreground="#f2f2f2")
    style.configure("Treeview", highlightthickness=0, bd=0, font=('calibri', 10))
    style.configure("Treeview.Heading", font=('calibri', 10, 'bold'), foreground="#f2f2f2", background="#6d046c")

    tree = ttk.Treeview(midView, columns=("Name", "Roll No", "Class", "Marks", "Grade", "Sex", "City"),
                        style="Treeview", selectmode="extended", height=28, yscrollcommand=scrollbary.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=tk.RIGHT, fill=tk.Y)
    tree.column('#0', stretch=tk.NO, minwidth=0, width=0, anchor='center')
    tree.heading('Name', text="Name", anchor=tk.CENTER)
    tree.column('#1', stretch=tk.NO, minwidth=0, width=300, anchor='center')
    tree.heading('Roll No', text="Roll No", anchor=tk.CENTER)
    tree.column('#2', stretch=tk.NO, minwidth=0, width=150, anchor='center')
    tree.heading('Class', text="Class", anchor=tk.CENTER)
    tree.column('#3', stretch=tk.NO, minwidth=0, width=150, anchor='center')
    tree.heading('Marks', text="Marks", anchor=tk.CENTER)
    tree.column('#4', stretch=tk.NO, minwidth=0, width=150, anchor='center')
    tree.heading('Grade', text="Grade", anchor=tk.CENTER)
    tree.column('#5', stretch=tk.NO, minwidth=0, width=100, anchor='center')
    tree.heading('Sex', text="Sex", anchor=tk.CENTER)
    tree.column('#6', stretch=tk.NO, minwidth=0, width=100, anchor='center')
    tree.heading('City', text="City", anchor=tk.CENTER)
    tree.column('#7', stretch=tk.NO, minwidth=0, width=250, anchor='center')

    tree.pack(pady=10, fill="both", expand=True)
    ShowData()

    # ======================================BOTTOM VIEW FRAME====================================================
    btnView = tk.Frame(Home, width=screen_width, bg="#6d046c")
    btnView.grid(row=3, column=0, pady=10)

    btn_add = tk.Button(btnView, text="Add", activebackground="#6d046c", relief=tk.FLAT,
                        activeforeground="#f2f2f2", bg="#f2f2f2", fg="#6d046c", font=('calibri', 12),
                        width=8, height=1, cursor="hand2", command=lambda: ShowInsertWindow())
    btn_add.grid(row=0, column=0, padx=20, pady=10)

    btn_edit = tk.Button(btnView, text="Edit", activebackground="#6d046c", relief=tk.FLAT,
                         activeforeground="#f2f2f2", bg="#f2f2f2", fg="#6d046c", font=('calibri', 12),
                         width=8, height=1, cursor="hand2", command=lambda: ShowEditWindow())
    btn_edit.grid(row=0, column=1, padx=20, pady=10)

    btn_delete = tk.Button(btnView, text="Delete", activebackground="#6d046c", relief=tk.FLAT,
                           activeforeground="#f2f2f2", bg="#f2f2f2", fg="#6d046c", font=('calibri', 12),
                           width=8, height=1, cursor="hand2", command=lambda: Delete())
    btn_delete.grid(row=0, column=2, padx=20, pady=10)

    btn_reset = tk.Button(btnView, text="Reset", activebackground="#6d046c", relief=tk.FLAT,
                          activeforeground="#f2f2f2", bg="#f2f2f2", fg="#6d046c", font=('calibri', 12),
                          width=8, height=1, cursor="hand2", command=lambda: Reset())
    btn_reset.grid(row=0, column=3, padx=20, pady=10)

    btn_add.bind('<Return>', lambda: ShowInsertWindow())
    btn_edit.bind('<Return>', lambda: ShowEditWindow())
    Tick()


# ===========================================HOME WINDOW END HERE================================================


# ===========================================INSERT DATA WINDOW START HERE=======================================
def ShowInsertWindow():
    global InsertWindow
    InsertWindow = tk.Toplevel()
    InsertWindow.title("Student Management System")
    dwidth = 640
    dheight = 560
    x = (screen_width / 2) - (dwidth / 2)
    y = (screen_height / 2) - (dheight / 2)
    InsertWindow.geometry("%dx%d+%d+%d" % (dwidth, dheight, x, y))
    InsertWindow.resizable(0, 0)
    InsertWindow.config(bg="#6d046c")
    # InsertWindow.overrideredirect(True)
    InsertWindow.grid_columnconfigure(0, weight=1)

    # ==============================================TOP VIEW FRAME===============================================
    topView = tk.Frame(InsertWindow, width=dwidth, bg="#6d046c")
    topView.grid(row=0, column=0, pady=10)

    lbl_title = tk.Label(topView, text="Add Data", font=('calibri', 16, 'bold'), bg="#6d046c", fg="#f2f2f2")
    lbl_title.grid(row=0, column=0, pady=10)

    # ==============================================MID VIEW FRAME===============================================
    midView = tk.Frame(InsertWindow, width=dwidth, bg="#6d046c")
    midView.grid(row=1, column=0, pady=10)

    lbl_roll = tk.Label(midView, text="Roll No", font=('calibri', 12), bg="#6d046c", fg="#f2f2f2")
    entry_roll = tk.Entry(midView, textvariable=ROLL, width=40, font=('calibri', 12))
    lbl_name = tk.Label(midView, text="Name", font=('calibri', 12), bg="#6d046c", fg="#f2f2f2")
    entry_name = tk.Entry(midView, textvariable=NAME, width=40, font=('calibri', 12))
    lbl_class = tk.Label(midView, text="Class", font=('calibri', 12), bg="#6d046c", fg="#f2f2f2")
    entry_class = tk.Entry(midView, textvariable=CLASS, width=40, font=('calibri', 12))
    lbl_marks = tk.Label(midView, text="Marks", font=('calibri', 12), bg="#6d046c", fg="#f2f2f2")
    entry_marks = tk.Entry(midView, textvariable=MARKS, width=40, font=('calibri', 12))
    lbl_grade = tk.Label(midView, text="Grade", font=('calibri', 12), bg="#6d046c", fg="#f2f2f2")
    entry_grade = tk.Entry(midView, textvariable=GRADE, width=40, font=('calibri', 12))
    lbl_sex = tk.Label(midView, text="Sex", font=('calibri', 12), bg="#6d046c", fg="#f2f2f2")
    entry_sex = tk.Entry(midView, textvariable=SEX, width=40, font=('calibri', 12))
    lbl_city = tk.Label(midView, text="City", font=('calibri', 12), bg="#6d046c", fg="#f2f2f2")
    entry_city = tk.Entry(midView, textvariable=CITY, width=40, font=('calibri', 12))

    btn_save = tk.Button(midView, text="Save", activebackground="#6d046c", relief=tk.FLAT,
                         activeforeground="#f2f2f2", bg="#f2f2f2", fg="#6d046c", font=('calibri', 12),
                         width=10, height=1, cursor="hand2", command=lambda: Insert())

    lbl_roll.grid(row=0, column=0, padx=10, pady=10)
    entry_roll.grid(row=0, column=1, padx=10, pady=10, ipady=4)
    lbl_name.grid(row=1, column=0, padx=10, pady=10)
    entry_name.grid(row=1, column=1, padx=10, pady=10, ipady=4)
    lbl_class.grid(row=2, column=0, padx=10, pady=10)
    entry_class.grid(row=2, column=1, padx=10, pady=10, ipady=4)
    lbl_marks.grid(row=3, column=0, padx=10, pady=10)
    entry_marks.grid(row=3, column=1, padx=10, pady=10, ipady=4)
    lbl_grade.grid(row=4, column=0, padx=10, pady=10)
    entry_grade.grid(row=4, column=1, padx=10, pady=10, ipady=4)
    lbl_sex.grid(row=5, column=0, padx=10, pady=10)
    entry_sex.grid(row=5, column=1, padx=10, pady=10, ipady=4)
    lbl_city.grid(row=6, column=0, padx=10, pady=10)
    entry_city.grid(row=6, column=1, padx=10, pady=10, ipady=4)
    btn_save.grid(row=7, column=1, padx=10, pady=20)


# ===========================================INSERT DATA WINDOW END HERE=======================================


# ===========================================EDIT DATA WINDOW START HERE=======================================
def ShowEditWindow():
    global EditWindow
    EditWindow = tk.Toplevel()
    EditWindow.title("Student Management System")
    dwidth = 640
    dheight = 560
    x = (screen_width / 2) - (dwidth / 2)
    y = (screen_height / 2) - (dheight / 2)
    EditWindow.geometry("%dx%d+%d+%d" % (dwidth, dheight, x, y))
    EditWindow.resizable(0, 0)
    EditWindow.config(bg="#6d046c")
    # InsertWindow.overrideredirect(True)
    EditWindow.grid_columnconfigure(0, weight=1)

    # ==============================================TOP VIEW FRAME===============================================
    topView = tk.Frame(EditWindow, width=dwidth, bg="#6d046c")
    topView.grid(row=0, column=0, pady=10)

    lbl_title = tk.Label(topView, text="Edit Data", font=('calibri', 16, 'bold'), bg="#6d046c", fg="#f2f2f2")
    lbl_title.grid(row=0, column=0, pady=10)

    # ==============================================MID VIEW FRAME===============================================
    midView = tk.Frame(EditWindow, width=dwidth, bg="#6d046c")
    midView.grid(row=1, column=0, pady=10)

    lbl_roll = tk.Label(midView, text="Roll No", font=('calibri', 12), bg="#6d046c", fg="#f2f2f2")
    entry_roll = tk.Entry(midView, textvariable=ROLL, width=40, font=('calibri', 12))
    lbl_name = tk.Label(midView, text="Name", font=('calibri', 12), bg="#6d046c", fg="#f2f2f2")
    entry_name = tk.Entry(midView, textvariable=NAME, width=40, font=('calibri', 12))
    lbl_class = tk.Label(midView, text="Class", font=('calibri', 12), bg="#6d046c", fg="#f2f2f2")
    entry_class = tk.Entry(midView, textvariable=CLASS, width=40, font=('calibri', 12))
    lbl_marks = tk.Label(midView, text="Marks", font=('calibri', 12), bg="#6d046c", fg="#f2f2f2")
    entry_marks = tk.Entry(midView, textvariable=MARKS, width=40, font=('calibri', 12))
    lbl_grade = tk.Label(midView, text="Grade", font=('calibri', 12), bg="#6d046c", fg="#f2f2f2")
    entry_grade = tk.Entry(midView, textvariable=GRADE, width=40, font=('calibri', 12))
    lbl_sex = tk.Label(midView, text="Sex", font=('calibri', 12), bg="#6d046c", fg="#f2f2f2")
    entry_sex = tk.Entry(midView, textvariable=SEX, width=40, font=('calibri', 12))
    lbl_city = tk.Label(midView, text="City", font=('calibri', 12), bg="#6d046c", fg="#f2f2f2")
    entry_city = tk.Entry(midView, textvariable=CITY, width=40, font=('calibri', 12))

    btn_save = tk.Button(midView, text="Save", activebackground="#6d046c", relief=tk.FLAT,
                         activeforeground="#f2f2f2", bg="#f2f2f2", fg="#6d046c", font=('calibri', 12),
                         width=10, height=1, cursor="hand2", command=lambda: Update())

    lbl_roll.grid(row=0, column=0, padx=10, pady=10)
    entry_roll.grid(row=0, column=1, padx=10, pady=10, ipady=4)
    lbl_name.grid(row=1, column=0, padx=10, pady=10)
    entry_name.grid(row=1, column=1, padx=10, pady=10, ipady=4)
    lbl_class.grid(row=2, column=0, padx=10, pady=10)
    entry_class.grid(row=2, column=1, padx=10, pady=10, ipady=4)
    lbl_marks.grid(row=3, column=0, padx=10, pady=10)
    entry_marks.grid(row=3, column=1, padx=10, pady=10, ipady=4)
    lbl_grade.grid(row=4, column=0, padx=10, pady=10)
    entry_grade.grid(row=4, column=1, padx=10, pady=10, ipady=4)
    lbl_sex.grid(row=5, column=0, padx=10, pady=10)
    entry_sex.grid(row=5, column=1, padx=10, pady=10, ipady=4)
    lbl_city.grid(row=6, column=0, padx=10, pady=10)
    entry_city.grid(row=6, column=1, padx=10, pady=10, ipady=4)
    btn_save.grid(row=7, column=1, padx=10, pady=20)
    entry_roll.configure(state=tk.DISABLED)
    Edit()


# ===========================================EDIT DATA WINDOW END HERE=======================================


# ===========================================GLOBAL FUNCTIONS========================================================
def Database():
    global conn, cursor
    try:
        conn = cx_Oracle.connect("nixrajput/hackerx000@localhost:1521/orcl")
    except cx_Oracle.DatabaseError as exception:
        msg = "Failed to connect to Oracle DB " + str(exception)
        print(msg)
    cursor = conn.cursor()


def Minimize():
    rootWindow.iconify()


def Exit2():
    exit(1)


def ShowHome():
    rootWindow.withdraw()
    HomeWindow()


def Minimize2():
    Home.iconify()


def Exit():
    exit(1)


def ShowData():
    Database()
    try:
        cursor.execute("SELECT * FROM student ORDER BY rollno")
    except cx_Oracle.DatabaseError as exception:
        print(str(exception))
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=data)
    cursor.close()
    conn.close()


def Insert():
    Database()
    roll = (int(ROLL.get()))
    name = (str(NAME.get()))
    sclass = (str(CLASS.get()))
    marks = (float(MARKS.get()))
    grade = (str(GRADE.get()))
    sex = (str(SEX.get()))
    city = (str(CITY.get()))

    sql_insert_data = "insert into student (ROLLNO, NAME, CLASS, MARKS, GRADE, SEX, CITY) values (:srollno, :sname, " \
                      ":sclass, :smarks, :sgrade, :ssex, :scity) "
    try:
        cursor.execute(sql_insert_data,
                       {'srollno': roll, 'sname': name, 'sclass': sclass, 'smarks': marks, 'sgrade': grade, 'ssex': sex,
                        'scity': city})
        ROLL.set("")
        NAME.set("")
        CLASS.set("")
        MARKS.set("")
        GRADE.set("")
        SEX.set("")
        CITY.set("")
        tkMessagebox.showinfo("Success", "Data Added Successfully!")
        print("Data Added Successfully!")
    except cx_Oracle.DatabaseError as exception:
        print(str(exception))
        msg = str(exception)
        tkMessagebox.showerror("Error", msg)
    conn.commit()
    cursor.close()
    conn.close()
    Reset()


def Reset():
    tree.delete(*tree.get_children())
    ShowData()


def Tick():
    global time1
    time2 = time.strftime('%H:%M:%S')
    if time2 != time1:
        time1 = time2
        lbl_time.config(text=time2)
    lbl_time.after(200, Tick)


def Search():
    print("Searching...")
    search = str(SEARCH.get())
    if SEARCH.get() != "":
        tree.delete(*tree.get_children())
        Database()
        sql_search_data = "SELECT * FROM student WHERE name LIKE '% :s %' "
        try:
            cursor.execute(sql_search_data, {'s': search})
        except cx_Oracle.DatabaseError as exception:
            print(str(exception))
            msg = str(exception)
            tkMessagebox.showerror("Error", msg)
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=data)
        cursor.close()
        conn.close()
        print("Searching Finished...")


def Delete():
    if not tree.selection():
        print("ERROR")
    else:
        curItem = tree.focus()
        content = (tree.item(curItem))
        selectedItem = content['values']
        tree.delete(curItem)
        Database()
        sql_delete_data = "DELETE FROM student WHERE rollno = :d"
        try:
            cursor.execute(sql_delete_data, {'d': selectedItem[1]})
        except cx_Oracle.DatabaseError as exception:
            print(str(exception))
        conn.commit()
        cursor.close()
        conn.close()


def Edit():
    if not tree.selection():
        print("ERROR: NOT SELECTED")
        tkMessagebox.showwarning("Error", "Item Not Selected!")
    else:
        curItem = tree.focus()
        content = (tree.item(curItem))
        selectedItem = content['values']
        NAME.set(selectedItem[0])
        ROLL.set(selectedItem[1])
        CLASS.set(selectedItem[2])
        MARKS.set(selectedItem[3])
        GRADE.set(selectedItem[4])
        SEX.set(selectedItem[5])
        CITY.set(selectedItem[6])


def Update():
    name = (str(NAME.get()))
    roll = (str(ROLL.get()))
    sclass = (str(CLASS.get()))
    marks = (str(MARKS.get()))
    grade = (str(GRADE.get()))
    sex = (str(SEX.get()))
    city = (str(CITY.get()))

    Database()
    sql_update_data = "UPDATE student SET name= :uname, rollno= :uroll, class= :uclass, marks= :umarks, " \
                      "grade= :ugrade, sex= :usex, city= :ucity WHERE rollno= :d"
    try:
        cursor.execute(sql_update_data, {'uname': name, 'uroll': roll, 'uclass': sclass, 'umarks': marks,
                                         'ugrade': grade, 'usex': sex, 'ucity': city, 'd': roll})

        tkMessagebox.showinfo("Success", "Data Updated Successfully!")
        print("Data Added Successfully!")

    except cx_Oracle.DatabaseError as exception:
        print(str(exception))
        msg = str(exception)
        tkMessagebox.showerror("Error", msg)
    conn.commit()
    cursor.close()
    conn.close()
    Reset()


def Login(event=None):
    global admin_id
    username = (str(USERNAME.get()))
    password = (str(PASSWORD.get()))
    Database()
    if USERNAME.get == "" or PASSWORD.get() == "":
        tkMessagebox.showwarning("Error", "Please complete the required field!")
    else:
        sql_login_admin = "SELECT * FROM admin WHERE username = :uname AND password = :upass"
        cursor.execute(sql_login_admin, {'uname': username, 'upass': password})
        if cursor.fetchone() is not None:
            cursor.execute(sql_login_admin, {'uname': username, 'upass': password})
            data = cursor.fetchone()
            admin_id = data[0]
            USERNAME.set("")
            PASSWORD.set("")
            ShowHome()
        else:
            tkMessagebox.showerror("Error", "Invalid Username or Password!")
            USERNAME.set("")
            PASSWORD.set("")


# ======================================================INITIALIZATION===============================================
if __name__ == '__main__':
    App()
