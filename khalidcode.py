from tkinter import *
import os
import sqlite3
import tkinter.messagebox


class main_page:
    def __init__(self, master):
        self.master = master
        master.title("SSK AIRWAYS")
        master.geometry('900x600')
        master.config(bg='sky blue')
        self.logo_label = Label(master, image=img3, bd=0, bg='#EBF2F8')
        self.logo_label.pack()
        self.passenger_button = Button(master, image=img2, command=self.passenger_login, bd=0, bg="#EBF2F8")
        self.passenger_button.place(x=200, y=400)
        self.organization_button = Button(master, image=img1, command=self.organization_login, bd=0, bg="#EBF2F8")
        self.organization_button.place(x=500, y=400)

    def passenger_login(self):
        # img24=PhotoImage(file='login-button.png')
        # img14=PhotoImage(file='cancel-button.png')
        self.passenger_login_frame = Frame(self.master, width=900, height=600, bg='#EBF2F8')
        self.passenger_login_frame.place(x=0, y=0)
        self.passenger_login_frame.tkraise()
        self.passenger_icon = Label(self.passenger_login_frame, image=img7, bd=0, bg='#EBF2F8')
        self.passenger_icon.place(x=350, y=10)
        self.username_label = Label(self.passenger_login_frame, text='Username', font=('Berlin Sans FB', 16),
                                    bg='#EBF2F8')
        self.username_label.place(x=405, y=200)
        self.passenger_username_entry = Entry(self.passenger_login_frame, bg='white', relief='sunken',
                                              highlightcolor='#D2E0F1',
                                              highlightthickness=1, highlightbackground='#D8D6D7',
                                              font=('Tw Cen MT', 14))
        self.passenger_username_entry.place(x=350, y=240)
        self.password_label = Label(self.passenger_login_frame, text='Password', font=('Berlin Sans FB', 16),
                                    bg='#EBF2F8')
        self.password_label.place(x=405, y=280)
        self.passenger_password_entry = Entry(self.passenger_login_frame, bg='white', show='*', relief='sunken',
                                              highlightcolor='#D2E0F1', highlightthickness=1,
                                              highlightbackground='#D8D6D7',
                                              font=('Tw Cen MT', 14))
        self.passenger_password_entry.place(x=350, y=320)
        self.passenger_password_entry.bind('<Return>', self.check_login)
        self.login_button = Button(self.passenger_login_frame, image=img5, bd=0, bg='#EBF2F8')
        self.login_button.bind('<Button-1>', self.check_login)
        self.login_button.place(x=357, y=420)
        self.cancel_button = Button(self.passenger_login_frame, image=img4, command=self.passenger_login_frame.destroy,
                                    bd=0, bg='#EBF2F8')
        self.cancel_button.place(x=357, y=460)
        self.signup_button = Button(self.passenger_login_frame, image=img6, command=self.signup_gui, bd=0, bg='#EBF2F8')
        self.signup_button.place(x=500, y=350)

    def signup_gui(self):
        self.passenger_signup_frame = Frame(self.passenger_login_frame, width=900, height=600, bg='#EBF2F8')
        self.passenger_signup_frame.place(x=0, y=0)
        self.passenger_signup_frame.tkraise()
        self.username_label = Label(self.passenger_signup_frame, text='Username', font=('Berlin Sans FB', 16),
                                    bg='#EBF2F8')
        self.username_label.place(x=405, y=150)
        self.passenger_username_entry1 = Entry(self.passenger_signup_frame, bg='white', relief='sunken',
                                               highlightcolor='#D2E0F1',
                                               highlightthickness=1, highlightbackground='#D8D6D7',
                                               font=('Tw Cen MT', 14))
        self.passenger_username_entry1.place(x=350, y=190)
        self.password_label = Label(self.passenger_signup_frame, text='Password', font=('Berlin Sans FB', 16),
                                    bg='#EBF2F8')
        self.password_label.place(x=405, y=230)
        self.passenger_password_entry1 = Entry(self.passenger_signup_frame, bg='white', show='*', relief='sunken',
                                               highlightcolor='#D2E0F1', highlightthickness=1,
                                               highlightbackground='#D8D6D7',
                                               font=('Tw Cen MT', 14))
        self.passenger_password_entry1.place(x=350, y=270)
        self.check_password_label = Label(self.passenger_signup_frame, text='Check Password',
                                          font=('Berlin Sans FB', 16),
                                          bg='#EBF2F8')
        self.check_password_label.place(x=378, y=310)
        self.passenger_check_password_entry1 = Entry(self.passenger_signup_frame, bg='white', show='*', relief='sunken',
                                                     highlightcolor='#D2E0F1', highlightthickness=1,
                                                     highlightbackground='#D8D6D7',
                                                     font=('Tw Cen MT', 14))
        self.passenger_check_password_entry1.place(x=350, y=350)
        self.passenger_check_password_entry1.bind('<Return>', self.check_login)
        self.login_button.bind('<Button-1>', self.check_login)
        self.login_button.place(x=370, y=420)
        self.cancel_button1 = Button(self.passenger_signup_frame, image=img8,
                                     command=self.passenger_signup_frame.destroy, bd=0, bg='#EBF2F8')
        self.cancel_button1.place(x=355, y=460)
        self.signup_button1 = Button(self.passenger_signup_frame, image=img9, command=self.sign_up, bd=0, bg='#EBF2F8')
        self.signup_button1.place(x=405, y=390)

    def sign_up(self):
        file = open('database.txt', "a+")
        l = []
        while True:
            file = open("database.txt", "a+")
            file.write('\n')
            file.write(self.passenger_username_entry1.get())
            file.write('\n')
            file.write(self.passenger_password_entry1.get())
            file.close()
            fr = open('database.txt', 'r')
            for line in fr:
                print(line)
                flag = 0
                if self.passenger_username_entry1.get() in line:
                    flag = 1
                    if flag == 1:
                        l.append(line)

                    else:
                        tkinter.messagebox.showerror('ERROR', 'Username Exists!')
            fr.close()
            break

    def check_login(self, s):
        self.file = open('database.txt', "r")
        self.file.readline()
        flag = 0
        for data in self.file:
            print(data)
            if self.passenger_username_entry.get() in data and self.passenger_password_entry.get() in data:
                flag = 1
                break
            if flag == 0:
                self.passenger_section = Frame(self.passenger_login_frame, width=900, height=600, bg='#EBF2F8')
                self.passenger_section.place(x=0, y=0)
                self.passenger_section.tkraise()
                # self. = Button(self.passenger_section,  bd=0, bg='#EBF2F8')
                # self..place(x=355, y=460)
                # self. = Button(self.passenger_section, bd=0, bg='#EBF2F8')
                # self..place(x=355, y=460)
                # self. = Button(self.passenger_section, bd=0, bg='#EBF2F8')
                # self..place(x=355, y=460)
                # self. = Button(self.passenger_section, bd=0, bg='#EBF2F8')
                # self..place(x=355, y=460)
                # self. = Button(self.passenger_section, bd=0, bg='#EBF2F8')
                # self..place(x=355, y=460)
                # self. = Button(self.passenger_section, bd=0, bg='#EBF2F8')
                # self..place(x=355, y=460)
                # self. = Button(self.passenger_section, bd=0, bg='#EBF2F8')
                # self..place(x=355, y=460)

            else:
                tkinter.messagebox.showerror('ERROR', 'Incorrect Username or Password!')
        self.file.close()

    def organization_login(self):
        self.organization_login_frame = Frame(self.master, width=900, height=600, bg='#EBF2F8')
        self.organization_login_frame.place(x=0, y=0)
        self.organization_login_frame.tkraise()
        self.organization_icon = Label(self.organization_login_frame, image=img10, bd=0, bg='#EBF2F8')
        self.organization_icon.place(x=350, y=10)
        self.username_label = Label(self.organization_login_frame, text='Username', font=('Berlin Sans FB', 16),
                                    bg='#EBF2F8')
        self.username_label.place(x=405, y=200)
        self.organization_username_entry = Entry(self.organization_login_frame, bg='white', relief='sunken',
                                                 highlightcolor='#D2E0F1',
                                                 highlightthickness=1, highlightbackground='#D8D6D7',
                                                 font=('Tw Cen MT', 14))
        self.organization_username_entry.place(x=350, y=240)
        self.password_label = Label(self.organization_login_frame, text='Password', font=('Berlin Sans FB', 16),
                                    bg='#EBF2F8')
        self.password_label.place(x=405, y=280)
        self.organization_password_entry = Entry(self.organization_login_frame, bg='white', show='*', relief='sunken',
                                                 highlightcolor='#D2E0F1', highlightthickness=1,
                                                 highlightbackground='#D8D6D7',
                                                 font=('Tw Cen MT', 14))
        self.organization_password_entry.place(x=350, y=320)
        self.organization_password_entry.bind('<Return>', self.check_login_organization)
        self.login_button = Button(self.organization_login_frame, image=img12, bd=0, bg='#EBF2F8')
        self.login_button.bind('<Button-1>', self.check_login_organization)
        self.login_button.place(x=370, y=420)
        self.cancel_button = Button(self.organization_login_frame, image=img11,
                                    command=self.organization_login_frame.destroy, bd=0, bg='#EBF2F8')
        self.cancel_button.place(x=370, y=460)

    def check_login_organization(self, events):
        if self.organization_username_entry.get() == 'admin' and self.organization_password_entry.get() == 'password':
            self.organiztion_section = Frame(self.organization_login_frame, width=900, height=600, bg='#EBF2F8')
            self.organiztion_section.place(x=0, y=0)
            self.organiztion_section.tkraise()
            # self. = Button(self.organiztion_section, bd=0, bg='#EBF2F8')
            # self..place(x=355, y=460)
            # self. = Button(self.organiztion_section, bd=0, bg='#EBF2F8')
            # self..place(x=355, y=460)
            # self. = Button(self.organiztion_section, bd=0, bg='#EBF2F8')
            # self..place(x=355, y=460)
            # self. = Button(self.organiztion_section, bd=0, bg='#EBF2F8')
            # self..place(x=355, y=460)
            # self. = Button(self.organiztion_section, bd=0, bg='#EBF2F8')
            # self..place(x=355, y=460)
            # self. = Button(self.organiztion_section, bd=0, bg='#EBF2F8')
            # self..place(x=355, y=460)
            # self. = Button(self.organiztion_section, bd=0, bg='#EBF2F8')
            # self..place(x=355, y=460)
            self.emp_button = Button(self.organiztion_section, text='button', command=self.Main)
            self.emp_button.place(x=0, y=0)

    def Main(self):
        self.emp_frame = Frame(self.organiztion_section, height=1000, width=900, bg='white')
        self.emp_frame.place(x=0, y=0)
        self.emp_frame.tkraise()
        self.welcome_img = PhotoImage(file='logo1a.png')
        self.emp_label = Label(self.emp_frame, image=self.welcome_img, bg='white')
        self.emp_label.place(x=0, y=0)
        self.emp_img = PhotoImage(file='emp1.png')
        self.emp_label2 = Label(self.emp_frame, image=self.emp_img, bg='white')
        self.emp_label2.place(x=0, y=300)

        self.pilot_img = PhotoImage(file='pilot1.png')
        self.pilot_button = Button(self.emp_frame, command=self.pilot_records, image=self.pilot_img)
        self.pilot_button.place(x=10, y=270)

        # self.pilot_button.config(image=pilot_img)
        # self.emp_button = Button(self.emp_frame, text='PILOTS',command=self.pilot_records)
        # self.emp_button.place(x=100,y=200)

        self.marshall_img = PhotoImage(file='marshall1.png')
        sky_marshall_button = Button(self.emp_frame, command=self.sky_marshall_records, bg='white',
                                     image=self.marshall_img)
        sky_marshall_button.place(x=160, y=270)

        # sky_marshall_button.config(image=marshall_img)

        self.hostess_img = PhotoImage(file='airhostess1.png')
        self.arihostess_button = Button(self.emp_frame, command=self.air_hostess_records, bg='white',
                                        image=self.hostess_img)
        self.arihostess_button.place(x=310, y=270)

        # arihostess_button.config(image=hostess_img)
        self.aviator_img = PhotoImage(file='aviator1.png')
        self.aviator_button = Button(self.emp_frame, command=self.aviator_records, bg='white', image=self.aviator_img)
        self.aviator_button.place(x=480, y=270)

        self.janitor_img = PhotoImage(file='jani.png')
        self.janitor_button = Button(self.emp_frame, command=self.janitor_records, bg='white', image=self.janitor_img)
        self.janitor_button.place(x=630, y=270)

        self.quit_img = PhotoImage(file='quitbutton.png')
        self.quit_button = Button(self.emp_frame, command=quit, image=self.quit_img)
        self.quit_button.place(x=780, y=270)

    pilot_record_frame = None

    def pilot_records(self):
        global pilot_records_frame
        pilot_records_frame = Tk()
        pilot_records_frame.title('PILOTS')
        self.pilotobj = Pilots().records()
        back_button = Button(pilot_records_frame, text='BACK', command=self.pilot_del_button)
        back_button.pack(side=TOP)
        for a in Pilots().pilot_list:
            self.pilot_records_label = Label(pilot_records_frame, text=a, bg='SKY BLUE')
            self.pilot_space_label1 = Label(pilot_records_frame,
                                            text='________________________________________________________________________________________')
            self.pilot_space_label2 = Label(pilot_records_frame,
                                            text='****************************************************************************************')
            self.pilot_records_label.pack()
            self.pilot_space_label1.pack()
            self.pilot_space_label2.pack()

    def pilot_del_button(self):
        pilot_records_frame.destroy()

    sky_marshall_records_frame = None

    def sky_marshall_records(self):

        global sky_marshall_records_frame

        sky_marshall_records_frame = Tk()
        sky_marshall_records_frame.title('SKY MARSHALLS')
        self.marshallobj = Sky_marshall().records()
        # self.abc = StringVar()
        # self.abc.set(self.pilotobj)
        back_button = Button(sky_marshall_records_frame, text='BACK', command=self.marshall_del_button)
        back_button.pack(side=TOP)
        for a in Sky_marshall().sky_marshall_list:
            self.sky_marshall_space_label4 = Label(sky_marshall_records_frame, text='')
            self.sky_marshall_space_label4.pack()
            self.sky_marshall_records_label = Label(sky_marshall_records_frame, text=a, bg='SKY BLUE')
            self.sky_marshall_space_label1 = Label(sky_marshall_records_frame,
                                                   text='________________________________________________________________________________________')
            self.sky_marshall_space_label2 = Label(sky_marshall_records_frame,
                                                   text='****************************************************************************************')
            self.sky_marshall_records_label.pack()
            self.sky_marshall_space_label1.pack()
            self.sky_marshall_space_label2.pack()
            self.sky_marshall_space_label3 = Label(sky_marshall_records_frame, text='')
            self.sky_marshall_space_label2.pack()

    def marshall_del_button(self):
        sky_marshall_records_frame.destroy()

    hostess_record_window = None

    def air_hostess_records(self):
        global hostess_record_window
        hostess_record_window = Tk()
        hostess_record_window.title('AIRHOSTESS')
        self.hostessobj = Airhostess().records()
        back_button = Button(hostess_record_window, text='BACK', command=self.hostess_del_button)
        back_button.pack(side=TOP)
        for a in Airhostess().airhostess_list:
            self.hostess_records_label = Label(hostess_record_window, text=a, bg='SKY BLUE')
            self.hostess_space_label1 = Label(hostess_record_window,
                                              text='________________________________________________________________________________________')
            self.hostess_space_label2 = Label(hostess_record_window,
                                              text='****************************************************************************************')
            self.hostess_records_label.pack()
            self.hostess_space_label1.pack()
            self.hostess_space_label2.pack()

    def hostess_del_button(self):
        hostess_record_window.destroy()

    janitor_records_window = None

    def janitor_records(self):

        global janitor_records_window

        janitor_records_window = Tk()
        janitor_records_window.title('JANITORS')
        self.janitorobj = Janitor().records()
        # self.abc = StringVar()
        # self.abc.set(self.pilotobj)
        back_button = Button(janitor_records_window, text='BACK', command=self.janitor_del_button)
        back_button.pack(side=TOP)
        for a in Janitor().janitor_list:
            self.janitor_space_label4 = Label(janitor_records_window, text='')
            self.janitor_space_label4.pack()
            self.janitor_records_label = Label(janitor_records_window, text=a, bg='SKY BLUE')
            self.janitor_space_label1 = Label(janitor_records_window,
                                              text='________________________________________________________________________________________')
            self.janitor_space_label2 = Label(janitor_records_window,
                                              text='****************************************************************************************')
            self.janitor_records_label.pack()
            self.janitor_space_label1.pack()
            self.janitor_space_label2.pack()
            self.janitor_space_label3 = Label(janitor_records_window, text='')
            self.janitor_space_label2.pack()

    def janitor_del_button(self):
        janitor_records_window.destroy()

    aviator_records_window = None

    def aviator_records(self):

        global aviator_records_window

        aviator_records_window = Tk()
        aviator_records_window.title('JANITORS')
        self.aviatorobj = Aviator().records()
        # self.abc = StringVar()
        # self.abc.set(self.pilotobj)
        back_button = Button(aviator_records_window, text='BACK', command=self.aviator_del_button)
        back_button.pack(side=TOP)
        for a in Aviator().aviator_list:
            self.aviator_space_label4 = Label(aviator_records_window, text='')
            self.aviator_space_label4.pack()
            self.aviator_records_label = Label(aviator_records_window, text=a, bg='SKY BLUE')
            self.aviator_space_label1 = Label(aviator_records_window,
                                              text='________________________________________________________________________________________')
            self.aviator_space_label2 = Label(aviator_records_window,
                                              text='****************************************************************************************')
            self.aviator_records_label.pack()
            self.aviator_space_label1.pack()
            self.aviator_space_label2.pack()
            self.aviator_space_label3 = Label(aviator_records_window, text='')
            self.aviator_space_label2.pack()

    def aviator_del_button(self):
        aviator_records_window.destroy()


class Employee:
    def __init__(self):
        global conn
        global c
        conn = sqlite3.connect('Employee.db')
        c = conn.cursor()
        '''c.execute("""CREATE TABLE employees(first text, last text, salary integer, plane text,post text)""")
        c.execute("INSERT INTO employees VALUES(?,?,?,?,?)", ('USMAN', 'ALI', 30000, 'BOEING 747-400' ,'sky marshall'))
        c.execute("INSERT INTO employees VALUES(?,?,?,?,?)", ('ALI', 'KHAN', 30000, 'BOEING 777-300' ,'sky marshall'))
        c.execute("INSERT INTO employees VALUES(?,?,?,?,?)", ('SOHAIB', 'AHMED', 30000, 'AIRBUS A340-600' , 'sky marshall'))
        c.execute("INSERT INTO employees VALUES(?,?,?,?,?)", ('AMJAD', 'MIRZA', 35000,'AIRBUS A380 PLUS', 'sky marshall'))
        c.execute("INSERT INTO employees VALUES(?,?,?,?,?)", ('FAROOQ', 'AZAM', 35000, 'SHAHEEN 7631' , 'sky marshall'))
        c.execute("INSERT INTO employees VALUES(?,?,?,?,?)", ('JAMSHEED', 'DOHI', 40000, 'B-2 SPIRIT' ,'sky marshall'))
        c.execute("INSERT INTO employees VALUES(?,?,?,?,?)", ('MOHSIN', 'ALI', 40000, 'GLOBAL EXPRESS','sky marshall'))
        c.execute("INSERT INTO employees VALUES(?,?,?,?,?)", ('SARA', 'HAMEED', 50000, 'BOEING 747-400', 'pilot'))
        c.execute("INSERT INTO employees VALUES(?,?,?,?,?)", ('ASAD', 'MIRZA', 50000, 'BOEING 747-400', 'pilot'))
        c.execute("INSERT INTO employees VALUES(?,?,?,?,?)", ('FURQAN', 'NISAR', 50000,'BOEING 777-300', 'pilot'))
        c.execute("INSERT INTO employees VALUES(?,?,?,?,?)", ('AHSAN', 'KHAN', 50000, 'BOEING 777-300', 'pilot'))
        c.execute("INSERT INTO employees VALUES(?,?,?,?,?)", ('NOMAN', 'KHAN', 55000,'AIRBUS A340-600', 'pilot'))
        c.execute("INSERT INTO employees VALUES(?,?,?,?,?)", ('BISMAH', 'FAROOQI',55000,'AIRBUS A340-600', 'pilot'))
        c.execute("INSERT INTO employees VALUES(?,?,?,?,?)", ('UROOJ', 'AHMED',55000,'AIRBUS A380 PLUS', 'pilot'))
        c.execute("INSERT INTO employees VALUES(?,?,?,?,?)", ('KHUZAIMA', 'HANFI',55000,'AIRBUS A380 PLUS', 'pilot'))
        c.execute("INSERT INTO employees VALUES(?,?,?,?,?)", ('JIBRAN', 'NASIR',55000,'SHAHEEN 7631', 'pilot'))
        c.execute("INSERT INTO employees VALUES(?,?,?,?,?)", ('WAQAR', 'ZAKA',60000,'SHAHEEN 7631', 'pilot'))
        c.execute("INSERT INTO employees VALUES(?,?,?,?,?)", ('BILAL', 'ASHRAF',60000,'B-2 SPIRIT', 'pilot'))
        c.execute("INSERT INTO employees VALUES(?,?,?,?,?)", ('MOIZ', 'ALI', 60000,'B-2 SPIRIT', 'pilot'))
        c.execute("INSERT INTO employees VALUES(?,?,?,?,?)", ('ALI', 'AHMED', 60000,'GLOBAL EXPRESS', 'pilot'))
        c.execute("INSERT INTO employees VALUES(?,?,?,?,?)", ('SOHAIB', 'AHMED',60000,'GLOBAL EXPRESS', 'pilot'))
        c.execute("INSERT INTO employees VALUES(?,?,?,?,?)", ('ASMA', 'ARIF', 25000, 'BOEING 747-400', 'airhostess'))
        c.execute("INSERT INTO employees VALUES(?,?,?,?,?)", ('ZARA', 'ABBAS',25000, 'BOEING 747-400', 'airhostess'))
        c.execute("INSERT INTO employees VALUES(?,?,?,?,?)", ('SAIMA', 'SHAHEEN',25000,'BOEING 777-300', 'airhostess'))
        c.execute("INSERT INTO employees VALUES(?,?,?,?,?)", ('SULTANA', 'ISHAQ',25000,'BOEING 777-300', 'airhostess'))
        c.execute("INSERT INTO employees VALUES(?,?,?,?,?)", ('UMAIMA', 'ERUM',25000,'AIRBUS A340-600', 'airhostess'))
        c.execute("INSERT INTO employees VALUES(?,?,?,?,?)", ('ZUNAIR', 'AHMED',25000,'AIRBUS A340-600', 'airhostess'))
        c.execute("INSERT INTO employees VALUES(?,?,?,?,?)", ('AMBER', 'ABBAS',25000,'AIRBUS A380 PLUS', 'airhostess'))
        c.execute("INSERT INTO employees VALUES(?,?,?,?,?)", ('SARA', 'KHAN', 30000,'AIRBUS A380 PLUS', 'airhostess'))
        c.execute("INSERT INTO employees VALUES(?,?,?,?,?)", ('MEESHA', 'SHAFI',30000,'SHAHEEN 7631', 'airhostess'))
        c.execute("INSERT INTO employees VALUES(?,?,?,?,?)", ('MAHNOOR', 'AZAM',30000,'SHAHEEN 7631', 'airhostess'))
        c.execute("INSERT INTO employees VALUES(?,?,?,?,?)", ('SAMEENA', 'FAROOQI',30000,'B-2 SPIRIT', 'airhostess'))
        c.execute("INSERT INTO employees VALUES(?,?,?,?,?)", ('MARIUM', 'AURANGZAB',30000,'B-2 SPIRIT', 'airhostess'))
        c.execute("INSERT INTO employees VALUES(?,?,?,?,?)", ('FATIMA', 'KAMAL',30000,'GLOBAL EXPRESS', 'airhostess'))
        c.execute("INSERT INTO employees VALUES(?,?,?,?,?)", ('ZULIKHA', 'BANO',30000,'GLOBAL EXPRESS', 'airhostess'))
        c.execute("INSERT INTO employees VALUES(?,?,?,?,?)", ('IMRAN', 'ISAML', 10000,'BOEING 747-400', 'janitor'))
        c.execute("INSERT INTO employees VALUES(?,?,?,?,?)", ('ISHAQ', 'GUL', 10000,'BOEING 777-300', 'janitor'))
        c.execute("INSERT INTO employees VALUES(?,?,?,?,?)", ('WALEED', 'KHAN', 10000,'AIRBUS A340-600', 'janitor'))
        c.execute("INSERT INTO employees VALUES(?,?,?,?,?)", ('AJMAL', 'SAEED', 10000,'AIRBUS A380 PLUS', 'janitor'))
        c.execute("INSERT INTO employees VALUES(?,?,?,?,?)", ('GHUFRAN', 'AZAM', 15000,'SHAHEEN 7631', 'janitor'))
        c.execute("INSERT INTO employees VALUES(?,?,?,?,?)", ('HAMEED', 'AHMED', 15000,'B-2 SPIRIT', 'janitor'))
        c.execute("INSERT INTO employees VALUES(?,?,?,?,?)", ('SAMAD', 'KHAN', 15000,'GLOBAL EXPRESS', 'janitor'))
        c.execute("INSERT INTO employees VALUES(?,?,?,?,?)", ('AZMAT', 'HUSSAIN', 20000,'BOEING 747-400', 'aviator'))
        c.execute("INSERT INTO employees VALUES(?,?,?,?,?)", ('KHALIQ', 'REHMAN', 20000,'BOEING 777-300', 'aviator'))
        c.execute("INSERT INTO employees VALUES(?,?,?,?,?)", ('SHAIQ', 'SHAIQ', 20000,'AIRBUS A340-600', 'aviator'))
        c.execute("INSERT INTO employees VALUES(?,?,?,?,?)", ('KHAWAJA', 'FAREED', 22000,'AIRBUS A380 PLUS', 'aviator'))
        c.execute("INSERT INTO employees VALUES(?,?,?,?,?)", ('JAWERIA', 'ANAS', 25000,'SHAHEEN 7631', 'aviator'))
        c.execute("INSERT INTO employees VALUES(?,?,?,?,?)", ('JAMSHEED', 'KHAN', 25000,'B-2 SPIRIT', 'aviator'))
        c.execute("INSERT INTO employees VALUES(?,?,?,?,?)", ('ZIA', 'TABSSUM', 25000,'GLOBAL EXPRESS', 'aviator'))
        conn.commit()
ob = Employee()'''


class Pilots(Employee):
    conn = sqlite3.connect('Employee.db')
    c = conn.cursor()
    pilot_list = []

    def records(self):
        with conn:
            c.execute("SELECT * FROM employees WHERE post ='pilot'")
            data = c.fetchall()
            # print('FOLLOWING ARE THE PILOTS')
            for row in data:
                self.pilot_list.append(' FIRST:     ' + row[0] + '      LAST:    ' + row[1] + '     SALARY:   ' + str(
                    row[2]) + '    PLANE:      ' + row[3] + '      POST:       ' + row[4])
            return (self.pilot_list)


# ob = Pilots().records()


class Sky_marshall(Employee):
    conn = sqlite3.connect('Employee.db')
    c = conn.cursor()
    sky_marshall_list = []

    def records(self):
        with conn:
            c.execute("SELECT * FROM employees WHERE post='sky marshall'")
            data = c.fetchall()
            # print('FOLLOWING ARE THE SKY MARSHALLS')
            for row in data:
                self.sky_marshall_list.append(
                    ' FIRST:     ' + row[0] + '      LAST:    ' + row[1] + '     SALARY:   ' + str(
                        row[2]) + '    PLANE:      ' + row[3] + '      POST:       ' + row[4])
            return (self.sky_marshall_list)


# ob = Sky_marshall().records()

class Airhostess(Employee):
    conn = sqlite3.connect('Employee.db')
    c = conn.cursor()
    airhostess_list = []

    def records(self):
        c.execute("SELECT * FROM employees WHERE post='airhostess'")
        data = c.fetchall()
        # print('FOLLOWING ARE THE AIRHOSTESS')
        for row in data:
            self.airhostess_list.append(' FIRST:     ' + row[0] + '      LAST:    ' + row[1] + '     SALARY:   ' + str(
                row[2]) + '    PLANE:      ' + row[3] + '      POST:       ' + row[4])
        return (self.airhostess_list)


class Janitor(Employee):
    conn = sqlite3.connect('Employee.db')
    c = conn.cursor()
    janitor_list = []

    def records(self):
        c.execute("SELECT * FROM employees WHERE post ='janitor'")
        data = c.fetchall()
        # print('FOLLOWING ARE THE JANITORS')
        for row in data:
            self.janitor_list.append(' FIRST:     ' + row[0] + '      LAST:    ' + row[1] + '     SALARY:   ' + str(
                row[2]) + '    PLANE:      ' + row[3] + '      POST:       ' + row[4])
        return (self.janitor_list)


class Aviator(Employee):
    conn = sqlite3.connect('Employee.db')
    c = conn.cursor()
    aviator_list = []

    def records(self):
        c.execute("SELECT * FROM employees WHERE post ='aviator'")
        data = c.fetchall()
        # print('FOLLOWING ARE THE AVIATORS')
        for row in data:
            self.aviator_list.append(' FIRST:     ' + row[0] + '      LAST:    ' + row[1] + '     SALARY:   ' + str(
                row[2]) + '    PLANE:      ' + row[3] + '      POST:       ' + row[4])
        return (self.aviator_list)


# ob = Employee_GUI().Main()


if __name__ == '__main__':
    root = Tk()
    img1 = PhotoImage(file='organization_logo.png')
    img2 = PhotoImage(file='passenger_logo.png')
    img3 = PhotoImage(file='logo.png')
    img4 = PhotoImage(file='cancel-button.png')
    img5 = PhotoImage(file='login-button.png')
    img6 = PhotoImage(file='signup-button.png')
    img7 = PhotoImage(file='passanger-icon.png')
    img8 = PhotoImage(file='cancel-button.png')
    img9 = PhotoImage(file='signup-button.png')
    img10 = PhotoImage(file='organization-icon.png')
    img11 = PhotoImage(file='cancel-button.png')
    img12 = PhotoImage(file='login-button.png')
    a = main_page(root)
    root.mainloop()
#     root.mainloop()
#
#
#
# a=Passenger_Accounts()
# a.passenger_login()
