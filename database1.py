import sqlite3
from tkinter import *


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
    pilot_list=[]
    def records(self):
        with conn:
            c.execute("SELECT * FROM employees WHERE post ='pilot'")
            data =c.fetchall()
        #print('FOLLOWING ARE THE PILOTS')
            for row in data:
                self.pilot_list.append(' FIRST:     ' + row[0] + '      LAST:    ' + row[1]+ '     SALARY:   ' + str(row[2]) + '    PLANE:      ' + row[3] + '      POST:       ' + row[4])
            return ( self.pilot_list)
#ob = Pilots().records()



class Sky_marshall(Employee):
    conn = sqlite3.connect('Employee.db')
    c = conn.cursor()
    sky_marshall_list = []
    def records(self):
        with conn:
            c.execute("SELECT * FROM employees WHERE post='sky marshall'")
            data =c.fetchall()
        #print('FOLLOWING ARE THE SKY MARSHALLS')
            for row in data:
                self.sky_marshall_list.append(' FIRST:     ' + row[0] + '      LAST:    ' + row[1]+ '     SALARY:   ' + str(row[2]) + '    PLANE:      ' + row[3] + '      POST:       ' + row[4])
            return( self.sky_marshall_list)

#ob = Sky_marshall().records()

class Airhostess(Employee):
    conn = sqlite3.connect('Employee.db')
    c = conn.cursor()
    airhostess_list = []
    def records(self):
        c.execute("SELECT * FROM employees WHERE post='airhostess'")
        data =c.fetchall()
        #print('FOLLOWING ARE THE AIRHOSTESS')
        for row in data:
            self.airhostess_list.append(' FIRST:     ' + row[0] + '      LAST:    ' + row[1]+ '     SALARY:   ' + str(row[2]) + '    PLANE:      ' + row[3] + '      POST:       ' + row[4])
        return (self.airhostess_list)

class Janitor(Employee):
    conn = sqlite3.connect('Employee.db')
    c = conn.cursor()
    janitor_list = []
    def records(self):
        c.execute("SELECT * FROM employees WHERE post ='janitor'")
        data =c.fetchall()
        #print('FOLLOWING ARE THE JANITORS')
        for row in data:
            self.janitor_list.append(' FIRST:     ' + row[0] + '      LAST:    ' + row[1]+ '     SALARY:   ' + str(row[2]) + '    PLANE:      ' + row[3] + '      POST:       ' + row[4])
        return (self.janitor_list)

class Aviator(Employee):
    conn = sqlite3.connect('Employee.db')
    c = conn.cursor()
    aviator_list = []
    def records(self):
        c.execute("SELECT * FROM employees WHERE post ='aviator'")
        data =c.fetchall()
        #print('FOLLOWING ARE THE AVIATORS')
        for row in data:
            self.aviator_list.append(' FIRST:     ' + row[0] + '      LAST:    ' + row[1]+ '     SALARY:   ' + str(row[2]) + '    PLANE:      ' + row[3] + '      POST:       ' + row[4])
        return (self.aviator_list)



class Employee_GUI(Pilots,Sky_marshall,Janitor,Airhostess,Aviator):
    emp_main = Tk()
    emp_main.geometry('900x1000')
    emp_main.title('EMPLOYEE WINDOW')

    def Main(self):
        self.emp_frame = Frame(self.emp_main, height=1000 , width=1000)
        self.emp_frame.place(x=0,y=0)
        self.emp_frame.tkraise()
        self.welcome_img = PhotoImage(file='2ndsem9a.png')
        self.emp_label = Label(self.emp_frame ,image=self.welcome_img)
        self.emp_label.place(x=0,y=0)
        #self.emp_button = Button(self.emp_frame, text='PILOTS',command=self.pilot_records)
        #self.emp_button.place(x=100,y=200)

        pilot_button = Button(self.emp_frame , command=self.pilot_records)
        pilot_button.place(x=100, y=200)
        pilot_img = PhotoImage(file='2ndsem1a.png')
        pilot_button.config(image=pilot_img)

        sky_marshall_button = Button(self.emp_frame , command=self.sky_marshall_records)
        sky_marshall_button.place(x=400,y=200)
        marshall_img = PhotoImage(file='2ndsem2.png')
        sky_marshall_button.config(image=marshall_img)

        arihostess_button = Button(self.emp_frame , command=self.air_hostess_records)
        arihostess_button.place(x=700,y=200)
        hostess_img = PhotoImage(file='2ndsem6.png')
        arihostess_button.config(image=hostess_img)

        aviator_button = Button(self.emp_frame , command=self.aviator_records)
        aviator_button.place(x=250,y=400)
        aviator_img = PhotoImage(file='2ndsem4.png')
        aviator_button.config(image=aviator_img)

        janitor_button = Button(self.emp_frame, command=self.janitor_records)
        janitor_button.place(x=550,y=400)
        janitor_img = PhotoImage(file='2ndsem5.png')
        janitor_button.config(image=janitor_img)

        quit_button = Button(self.emp_frame, command=quit)
        quit_button.place(x=400,y=600)
        quit_img = PhotoImage(file='2ndsem7.png')
        quit_button.config(image=quit_img)

        self.emp_main.mainloop()

    pilot_record_frame = None
    def pilot_records(self):
        global  pilot_records_frame
        pilot_records_frame = Tk()
        pilot_records_frame.title('PILOTS')
        self.pilotobj = Pilots().records()
        back_button = Button(pilot_records_frame,text='BACK',command=self.pilot_del_button)
        back_button.pack(side=TOP)
        for a in self.pilot_list:
            self.pilot_records_label = Label(pilot_records_frame , text=a,bg='SKY BLUE')
            self.pilot_space_label1 = Label(pilot_records_frame, text='________________________________________________________________________________________')
            self.pilot_space_label2 = Label(pilot_records_frame, text='****************************************************************************************')
            self.pilot_records_label.pack()
            self.pilot_space_label1.pack()
            self.pilot_space_label2.pack()
    def pilot_del_button(self):
        pilot_records_frame.destroy()


    sky_marshall_records_frame = None
    def sky_marshall_records(self):

        global  sky_marshall_records_frame

        sky_marshall_records_frame = Tk()
        sky_marshall_records_frame.title('SKY MARSHALLS')
        self.marshallobj = Sky_marshall().records()
        #self.abc = StringVar()
        #self.abc.set(self.pilotobj)
        back_button = Button(sky_marshall_records_frame,text='BACK',command=self.marshall_del_button)
        back_button.pack(side=TOP)
        for a in self.sky_marshall_list:
            self.sky_marshall_space_label4 = Label(sky_marshall_records_frame, text='')
            self.sky_marshall_space_label4.pack()
            self.sky_marshall_records_label = Label(sky_marshall_records_frame , text=a,bg='SKY BLUE')
            self.sky_marshall_space_label1 = Label(sky_marshall_records_frame, text='________________________________________________________________________________________')
            self.sky_marshall_space_label2 = Label(sky_marshall_records_frame, text='****************************************************************************************')
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
        back_button = Button(hostess_record_window,text='BACK',command=self.hostess_del_button)
        back_button.pack(side=TOP)
        for a in self.airhostess_list:
            self.hostess_records_label = Label(hostess_record_window , text=a,bg='SKY BLUE')
            self.hostess_space_label1 = Label(hostess_record_window, text='________________________________________________________________________________________')
            self.hostess_space_label2 = Label(hostess_record_window, text='****************************************************************************************')
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
        #self.abc = StringVar()
        #self.abc.set(self.pilotobj)
        back_button = Button(janitor_records_window,text='BACK',command=self.janitor_del_button)
        back_button.pack(side=TOP)
        for a in self.janitor_list:
            self.janitor_space_label4 = Label(janitor_records_window, text='')
            self.janitor_space_label4.pack()
            self.janitor_records_label = Label(janitor_records_window , text=a,bg='SKY BLUE')
            self.janitor_space_label1 = Label(janitor_records_window, text='________________________________________________________________________________________')
            self.janitor_space_label2 = Label(janitor_records_window, text='****************************************************************************************')
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
        #self.abc = StringVar()
        #self.abc.set(self.pilotobj)
        back_button = Button(aviator_records_window,text='BACK',command=self.aviator_del_button)
        back_button.pack(side=TOP)
        for a in self.aviator_list:
            self.aviator_space_label4 = Label(aviator_records_window, text='')
            self.aviator_space_label4.pack()
            self.aviator_records_label = Label(aviator_records_window , text=a,bg='SKY BLUE')
            self.aviator_space_label1 = Label(aviator_records_window, text='________________________________________________________________________________________')
            self.aviator_space_label2 = Label(aviator_records_window, text='****************************************************************************************')
            self.aviator_records_label.pack()
            self.aviator_space_label1.pack()
            self.aviator_space_label2.pack()
            self.aviator_space_label3 = Label(aviator_records_window, text='')
            self.aviator_space_label2.pack()
    def aviator_del_button(self):
        aviator_records_window.destroy()


ob = Employee_GUI().Main()





