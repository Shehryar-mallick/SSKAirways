import sqlite3
from tkinter import *
import tkinter.messagebox
from ssk_module1_flights import *
from ssk_module2_overloading import *
from ssk_module3_help import *
from ssk_module4_employees import *
from ssk_module5_aggregation import *

class incorrect_username_or_password(Exception):
    """This is a class for generating exception."""
    pass


class main_page:
    """This is a class for all the GUI operations."""

    def __init__(self,master):

        '''
                this contructor opens the main window of the project

                :METHOD CONTAINS:

                frame=1 ; label=2 ; button=2'''
        self.master=master
        master.title("SSK AIRWAYS")
        master.geometry('900x1000')
        master.config(bg='white')
        self.logo_label = Label(master, image=img3, bd=0, bg='white')
        self.logo_label.pack()
        self.creatorstext = StringVar()
        self.creatorstext.set(obj_sskairways)
        self.creatorslabel = Label(master, bg="white",fg='blue', textvariable=self.creatorstext, font='times 16 underline ')
        self.creatorslabel.place(x=23,y=650)
        self.passenger_button = Button(master, image=img2, command=self.passenger_login, bd=0, bg="#EBF2F8")
        self.passenger_button.place(x=200, y=400)
        self.organization_button = Button(master, image=img1,command=self.organization_login, bd=0, bg="#EBF2F8")
        self.organization_button.place(x=500, y=400)

    def passenger_login(self):

        ''':PASSENGER_LOGIN:
                the purpose of this method is to display the passenger login and passenger can login
                in it.

                when you press the passenger button in master  this method is called

                :METHOD CONTAINS:

                frame=1 ; label=3 ; button=3'''

        self.passenger_login_frame = Frame(self.master, width=1000, height=900, bg='white')
        self.passenger_login_frame.place(x=0, y=0)
        self.passenger_login_frame.tkraise()
        self.passenger_icon = Label(self.passenger_login_frame, image = img7, bd=0, bg='white')
        self.passenger_icon.place(x=350, y=10)
        self.username_label = Label(self.passenger_login_frame, text='Username', font=('Berlin Sans FB', 16), bg='#EBF2F8')
        self.username_label.place(x=405, y=200)
        self.passenger_username_entry = Entry(self.passenger_login_frame, bg='white', relief='sunken', highlightcolor='#D2E0F1',
                                       highlightthickness=1, highlightbackground='#D8D6D7', font=('Tw Cen MT', 14))
        self.passenger_username_entry.place(x=350, y=240)
        self.password_label = Label(self.passenger_login_frame, text='Password', font=('Berlin Sans FB', 16), bg='#EBF2F8')
        self.password_label.place(x=405, y=280)
        self.passenger_password_entry = Entry(self.passenger_login_frame, bg='white', show='*', relief='sunken',
                                       highlightcolor='#D2E0F1', highlightthickness=1, highlightbackground='#D8D6D7',
                                       font=('Tw Cen MT', 14))
        self.passenger_password_entry.place(x=350, y=320)
        self.passenger_password_entry.bind('<Return>',self.check_login )
        self.login_button = Button(self.passenger_login_frame, image = img5, bd=0, bg='#EBF2F8')
        self.login_button.bind('<Button-1>',self.check_login)
        self.login_button.place(x=354, y=420)
        self.cancel_button = Button(self.passenger_login_frame, image = img4,command=self.passenger_login_frame.destroy, bd=0, bg='#EBF2F8')
        self.cancel_button.place(x=354, y=460)
        self.signup_button = Button(self.passenger_login_frame, image = img6 ,command=self.signup_gui, bd=0, bg='#EBF2F8')
        self.signup_button.place(x=490, y=350)
    def signup_gui(self):

        ''':SIGNUP_GUI:
                the purpose of this method is to display the sign up window in the passenger
                login frame.

                when you press the signup button in passenger login frame this method is called

                :METHOD CONTAINS:

                frame=1 ; label=17 ; button=1'''
        self.passenger_signup_frame = Toplevel(self.passenger_login_frame)
        self.passenger_signup_frame.geometry('900x1000')
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
        self.check_password_label = Label(self.passenger_signup_frame, text='Check Password', font=('Berlin Sans FB', 16),
                                    bg='#EBF2F8')
        self.check_password_label.place(x=378, y=310)
        self.passenger_check_password_entry1 = Entry(self.passenger_signup_frame, bg='white', show='*', relief='sunken',
                                               highlightcolor='#D2E0F1', highlightthickness=1,
                                               highlightbackground='#D8D6D7',
                                               font=('Tw Cen MT', 14))
        self.passenger_check_password_entry1.place(x=350, y=350)
        self.passenger_check_password_entry1.bind('<Return>',self.sign_up )
        self.signup_button1 = Button(self.passenger_signup_frame, image=img9, bd=0, bg='#EBF2F8')
        self.signup_button1.bind('<Button-1>', self.sign_up)
        self.signup_button1.place(x=405, y=390)
        self.cancel_button1 = Button(self.passenger_signup_frame,image=img8, command=self.passenger_signup_frame.destroy,  bd=0, bg='#EBF2F8')
        self.cancel_button1.place(x=360, y=450)


    def sign_up(self,a=None):

        ''':SIGNUP:
                        the purpose of this method is to sign up the passenger, passenger username
                        and password saved in the text file using filing

                        This method is called when the signup button in passenger sigup frame is pressed.'''

        file = open('database1.txt', 'a+')
        l = []
        flag = 0
        while True:
            fr = open('database1.txt', "r")
            for line in fr:
                if self.passenger_username_entry1.get() in line:
                    flag = 1

            if flag == 1:
                tkinter.messagebox.showerror('ERROR', 'Username exists....Use any other username')
                self.passenger_signup_frame.destroy()


            fr.close()
            if self.passenger_password_entry1.get() == self.passenger_check_password_entry1.get():
                l.append(self.passenger_username_entry1.get() + ":" + self.passenger_password_entry1.get())
                file.write(self.passenger_username_entry1.get() + ":" + self.passenger_password_entry1.get())
                file.write('\n')
                file.close()
                self.credit_card_signup()
                break
            else:
                tkinter.messagebox.showerror('ERROR', 'Password Does Not Match!')
                break

    def check_login(self,a):
        ''':CHECK_LOGIN:
                        the purpose of this method is to check whether the passenger entered the right
                        username and password,ater the checking is done a new frame passenger section
                        opens which contain some buttons

                        Exception handling also done in this method

                        when you press the login button in passenger login frame this method is called

                        :METHOD CONTAINS:

                        frame=1 ; label=2 ; button=5'''
        data = self.passenger_username_entry.get() + ":" + self.passenger_password_entry.get()
        fr = open('database1.txt', "r")

        try:
            self.flag = 0
            for line in fr:
                if data == line[:-1]:
                    self.flag = 1
                    break

            if self.flag == 1:
                tkinter.messagebox.showinfo('Welcome', 'Welcome')

                self.passenger_section = Frame(self.passenger_login_frame, width=1000, height=900, bg='white')
                self.passenger_section.place(x=0, y=0)
                self.passenger_section.tkraise()
                self.view_label = Label(self.passenger_section, image=view_img)
                self.view_label.place(x=0, y=200)

                self.welcome_label = Label(self.passenger_section, bg='white', image=img3)
                self.welcome_label.place(x=0, y=0)
                self.flightbutton = Button(self.passenger_section, text="Flights", command=self.flightswindow,
                                               image=flight_button_img, bg='white')
                self.flightbutton.place(x=40, y=300)
                self.helpbutton = Button(self.passenger_section, text='Help Corner', font='SegoeUI', bg="white",
                                             command=self.helpcornerwindow, image=phelp_button_img)
                self.helpbutton.place(x=220, y=300)
                self.royalrentalbutton = Button(self.passenger_section, text='Royal rentals',
                                                    command=self.mainrental, image=royal_button_img, bg='white')
                self.royalrentalbutton.place(x=400, y=300)
                self.booking_button = Button(self.passenger_section, image=booking, command=self.book_flight)
                self.booking_button.place(x=580, y=300)
                self.back_button = Button(self.passenger_section, command=self.passenger_login_frame.destroy,
                                              image=passanger_quit_img, bg='white')
                self.back_button.place(x=760, y=300)

            else:
                raise incorrect_username_or_password

        except incorrect_username_or_password:
                tkinter.messagebox.showerror('ERROR', 'Incorrect Username or Password!')



        fr.close()

    def credit_card_signup(self):

        ''':CREDIT_CARD_SIGNUP:
                        the purpose of this method is to card details from the passenger.

                        :METHOD CONTAINS:

                        frame=1 ; label=7 ; button=2'''
        data=IntVar()
        data1=IntVar()
        data2 = IntVar()
        self.credit_card_frame = Frame(self.passenger_signup_frame, width=1000, height=900, bg='#EBF2F8')
        self.credit_card_frame.place(x=0, y=0)
        self.credit_card_frame.tkraise()
        self.creditcard_label = Label(self.credit_card_frame, image=img13)
        self.creditcard_label.place(x=350, y=10)
        self.firstname_label = Label(self.credit_card_frame, text='Firstname', font=('Berlin Sans FB', 19),
                                     bg='#EBF2F8')
        self.firstname_label.place(x=186, y=200)
        self.passenger_firstname_entry = Entry(self.credit_card_frame, bg='white', relief='sunken',
                                               highlightcolor='#D2E0F1',
                                               highlightthickness=1, highlightbackground='#D8D6D7',
                                               font=('Tw Cen MT', 14))
        self.passenger_firstname_entry.place(x=300, y=200)
        self.lastname_label = Label(self.credit_card_frame, text='Lastname', font=('Berlin Sans FB', 19),
                                    bg='#EBF2F8')
        self.lastname_label.place(x=186, y=250)
        self.passenger_lastname_entry = Entry(self.credit_card_frame, bg='white', relief='sunken',
                                              highlightcolor='#D2E0F1',
                                              highlightthickness=1, highlightbackground='#D8D6D7',
                                              font=('Tw Cen MT', 14))
        self.passenger_lastname_entry.place(x=300, y=250)
        self.ac_label = Label(self.credit_card_frame, text='Account Number', font=('Berlin Sans FB', 19),
                               bg='#EBF2F8')
        self.ac_label.place(x=100, y=300)
        self.passenger_ac_entry = Entry(self.credit_card_frame, bg='white', relief='sunken',
                                         highlightcolor='#D2E0F1',
                                         highlightthickness=1, highlightbackground='#D8D6D7',
                                         font=('Tw Cen MT', 14),textvariable=data)
        self.passenger_ac_entry.place(x=300, y=300)
        self.cc_label = Label(self.credit_card_frame, text='Country, City', font=('Berlin Sans FB', 19),
                              bg='#EBF2F8')
        self.cc_label.place(x=155, y=350)
        self.passenger_cc_entry = Entry(self.credit_card_frame, bg='white', relief='sunken',
                                        highlightcolor='#D2E0F1',
                                        highlightthickness=1, highlightbackground='#D8D6D7',
                                        font=('Tw Cen MT', 14))
        self.passenger_cc_entry.place(x=300, y=350)
        self.postal_code_label = Label(self.credit_card_frame, text='Postal Code', font=('Berlin Sans FB', 19),
                                       bg='#EBF2F8')
        self.postal_code_label.place(x=163, y=400)
        self.passenger_postal_code_entry = Entry(self.credit_card_frame, bg='white', relief='sunken',
                                                 highlightcolor='#D2E0F1',
                                                 highlightthickness=1, highlightbackground='#D8D6D7',
                                                 font=('Tw Cen MT', 14),textvariable=data1)
        self.passenger_postal_code_entry.place(x=300, y=400)
        self.expiry_date_label = Label(self.credit_card_frame, text='Expiry Date', font=('Berlin Sans FB', 19),
                                       bg='#EBF2F8')
        self.expiry_date_label.place(x=168, y=450)
        self.passenger_expiry_date_entry = Entry(self.credit_card_frame, bg='white', relief='sunken',
                                                 highlightcolor='#D2E0F1',
                                                 highlightthickness=1, highlightbackground='#D8D6D7',
                                                 font=('Tw Cen MT', 14),textvariable=data2)
        self.passenger_expiry_date_entry.place(x=300, y=450)
        self.ok_button = Button(self.credit_card_frame, text='OK',command=self.credit_close,image=img14, bd=0, bg='#EBF2F8')
        self.ok_button.place(x=300, y=500)
        self.cancel_button = Button(self.credit_card_frame, command=self.credit_card_frame.destroy,image=img8, bd=0, bg='#EBF2F8')
        self.cancel_button.place(x=300, y=590)

    def credit_close(self):
        self.credit_card_button()
        self.credit_card_frame.destroy()
        self.passenger_signup_frame.destroy()

    def credit_card_button(self):

        ''':CREDIT_CARD_BUTTON:
                        the purpose of this method is to save the credit details in the text file enterd
                        by the passenger using filing

                        when you press the ok button in credit card frame this method is called'''

        l = []
        while True:
            file = open("creditcard.txt", "a+")
            file.write('\n')
            file.write('---------------------------------------------------------------------------------------------------------')
            file.write('\n')
            file.write('Username : ')
            file.write(self.passenger_username_entry1.get())
            file.write('\n')
            file.write('Firstname : ')
            file.write( self.passenger_firstname_entry.get())
            file.write('\n')
            file.write('Lastname : ')
            file.write( self.passenger_lastname_entry.get())
            file.write('\n')
            file.write('Account Number : ')
            file.write( self.passenger_ac_entry.get())
            file.write('\n')
            file.write('Country and city : ')
            file.write( self.passenger_cc_entry.get())
            file.write('\n')
            file.write('Expiry Date : ')
            file.write( self.passenger_expiry_date_entry.get())
            file.write('\n')
            file.write('---------------------------------------------------------------------------------------------------------')
            file.close()
            fr = open('database1.txt', 'r')
            for line in fr:
                flag = 0
                if self.passenger_username_entry1.get() in line:
                    flag = 1
                    if flag == 1:
                        tkinter.messagebox.showinfo('SUCCESS', 'Account Created!')
                        self.passenger_login()

                    else:
                        tkinter.messagebox.showerror('ERROR', 'Try Again')
            fr.close()
            break

    name_entry = None
    passport_entry = None
    credit_entry = None
    var1 = None
    var2 = None
    var3 = None
    var4 = None
    var5 = None
    var6 = None
    var7 = None
    var8 = None
    var9 = None
    def book_flight(self):
        ''':BOOK FLIGHT

        the purpose of this method is to allow the user to book a flight

        :METHOD CONTAINS:

        frame=1 ; labels=4 ; entry=4 ; checkbuttons=9 ; buttons=2'''
        global name_entry
        global passport_entry
        global credit_entry
        global destination_entry
        global var1
        global var2
        global var3
        global var4
        global var5
        global var6
        global var7
        global var8
        global var9

        self.booking_frame = Frame(self.passenger_section,height='900',width='1000')
        self.booking_frame.place(x=0,y=0)
        self.booking_frame.tkraise()

        self.booking_logo_label = Label(self.booking_frame,image=booking_logo)
        self.booking_logo_label.place(x=0,y=0)

        self.book_name = Label(self.booking_frame,text='NAME',font=('castellar' , 12),bg='gold')
        self.book_name.place(x=50,y=50)

        self.book_passport = Label(self.booking_frame,text='PASSPORT NO',font=('castellar' , 12),bg='gold')
        self.book_passport.place(x=50,y=100)

        self.book_credit = Label(self.booking_frame,text='CREDIT CARD NO',font=('castellar' , 12),bg='gold')
        self.book_credit.place(x=50,y=200)

        name_entry = Entry(self.booking_frame, font=('castellar' , 12),bg='white')
        name_entry.place(x=250,y=50)

        passport_entry = Entry(self.booking_frame, font=('castellar' , 12))
        passport_entry.place(x=250,y=100)

        credit_entry = Entry(self.booking_frame, font=('castellar' , 12))
        credit_entry.place(x=250,y=200)

        var1 = IntVar()
        var2 = IntVar()
        var3 = IntVar()
        var4 = IntVar()
        var5 = IntVar()
        var6 = IntVar()
        var7 = IntVar()
        var8 = IntVar()
        var9 = IntVar()


        self.business_check = Checkbutton(self.booking_frame,text='BUSINESS',font=('castellar',12),variable=var1, onvalue=1,bg='orange')
        self.business_check.place(x=50,y=300)

        self.economy_check = Checkbutton(self.booking_frame,text='ECONOMY',font=('castellar',12),variable=var2, onvalue=1,bg='orange')
        self.economy_check.place(x=200,y=300)

        self.jeddah_check = Checkbutton(self.booking_frame,text='JEDDAH',font=('castellar',12),variable=var3, onvalue=1,bg='light grey')
        self.jeddah_check.place(x=50,y=350)

        self.frankfurt_check = Checkbutton(self.booking_frame,text='FRANKFURT',font=('castellar',12),variable=var4, onvalue=1,bg='light grey')
        self.frankfurt_check.place(x=50,y=400)

        self.toronto_check = Checkbutton(self.booking_frame,text='TORONTO',font=('castellar',12),variable=var5, onvalue=1,bg='light grey')
        self.toronto_check.place(x=50,y=450)

        self.newyork_check = Checkbutton(self.booking_frame,text='NEW-YORK',font=('castellar',12),variable=var6, onvalue=1,bg='light grey')
        self.newyork_check.place(x=50,y=500)

        self.dubai_check = Checkbutton(self.booking_frame,text='DUBAI',font=('castellar',12),variable=var7, onvalue=1,bg='light grey')
        self.dubai_check.place(x=50,y=550)

        self.london_check = Checkbutton(self.booking_frame,text='LONDON',font=('castellar',12),variable=var8, onvalue=1,bg='light grey')
        self.london_check.place(x=50,y=600)

        self.dhaka_check = Checkbutton(self.booking_frame,text='DHAKA',font=('castellar',12),variable=var9, onvalue=1,bg='light grey')
        self.dhaka_check.place(x=50,y=650)

        self.enter_button=Button(self.booking_frame,text='ENTER',font=('castellar',12),command=self.final_booking,bg='grey')
        self.enter_button.place(x=450,y=600)

        self.back_button = Button(self.booking_frame,image=passanger_quit_img,command=self.booking_frame.destroy)
        self.back_button.place(x=700,y=700)

    def final_booking(self):
        ''':FINAL BOOKING:
        the purpose of this method is to display the final results of the input given in
        the booking frame.

        when you press the enter button in booking frame this method is called

        :METHOD CONTAINS:

        frame=1 ; label=17 ; button=1'''
        self.name = name_entry.get()
        self.passport = passport_entry.get()
        self.credit = credit_entry.get()
        self.var1 = [var1.get(),'business class']
        self.var2 = [var2.get(),'economy class']
        self.var3 = [var3.get(),'JEDDAH','BOEING 74700','28/5/2019','09:00 PM']
        self.var4 = [var4.get(),'FRANKFURT','BOEING 777300','29/5/2019','12:00 PM']
        self.var5 = [var5.get(),'TORONTO','AIR BUS A340-600','30/5/2019','11:00 AM']
        self.var6 = [var6.get(),'NEW-YORK','AIR BUS A380PLUS ','31/5/2019','05:30 PM']
        self.var7 = [var7.get(),'DUBAI','SHAHEEN 7631','1/6/2019','03:45 AM']
        self.var8 = [var8.get(),'LONDON','B-2 SPIRIT','2/6/2019','12:00 AM']
        self.var9 = [var9.get(),'DHAKA','BD 700 GLOBAL EXPRESS','3/6/2019','03:15 PM']

        self.going = [self.var1,self.var2]
        self.destination = [self.var3,self.var4,self.var5,self.var6,self.var7,self.var8,self.var9]

        for a in self.going:
            if a[0] == 1:
                self.travel = (a[1])
                for b in self.destination:
                    if b[0] == 1:
                        self.destination = b[1]
                        self.plane = b[2]
                        self.date = b[3]
                        self.time = b[4]
                        break

        self.final_booking_frame = Frame(self.booking_frame,width=900,height=1000)
        self.final_booking_frame.place(x=0,y=0)
        self.final_booking_frame.tkraise()
        self.final_img = Label(self.final_booking_frame,image=booking_final)
        self.final_img.place(x=0,y=0)

        self.final_name = Label(self.final_booking_frame,text=self.name,font=('castellar',8),bg='light blue')
        self.final_name.place(x=180,y=537)

        self.flight_label = Label(self.final_booking_frame,text=self.plane,font=('castellar',8),bg='light blue')
        self.flight_label.place(x=185,y=380)

        self.gate = Label(self.final_booking_frame,text='GATE 1',font=('castellar',8),bg='light blue')
        self.gate.place(x=185,y=400)

        self.date_label = Label(self.final_booking_frame,text=self.date,font=('castellar',8),bg='light blue')
        self.date_label.place(x=185,y=420)

        self.time_label = Label(self.final_booking_frame,text=self.time,font=('castellar',8),bg='light blue')
        self.time_label.place(x=185,y=440)

        self.starting_written = Label(self.final_booking_frame,text='KARACHI',font=('castellar',8),bg='light blue')
        self.starting_written.place(x=185,y=470)

        self.final_travel = Label(self.final_booking_frame,text=self.travel,font=('castellar',8),bg='light blue')
        self.final_travel.place(x=180,y=520)

        self.final_destination = Label(self.final_booking_frame,text=self.destination,font=('castellar',8),bg='light blue')
        self.final_destination.place(x=185,y=490)

        self.final_name2 = Label(self.final_booking_frame,text=self.name,font=('castellar',8),bg='light blue')
        self.final_name2.place(x=780,y=465)

        self.flight_label2 = Label(self.final_booking_frame,text=self.plane,font=('castellar',8),bg='light blue')
        self.flight_label2.place(x=780,y=305)

        self.gate2 = Label(self.final_booking_frame,text='GATE 1',font=('castellar',8),bg='light blue')
        self.gate2.place(x=780,y=325)

        self.date_label2 = Label(self.final_booking_frame,text=self.date,font=('castellar',8),bg='light blue')
        self.date_label2.place(x=780,y=350)

        self.time_label2 = Label(self.final_booking_frame,text=self.time,font=('castellar',8),bg='light blue')
        self.time_label2.place(x=780,y=370)

        self.starting_written2 = Label(self.final_booking_frame,text='KARACHI',font=('castellar',8),bg='light blue')
        self.starting_written2.place(x=780,y=400)

        self.final_travel2 = Label(self.final_booking_frame,text=self.travel,font=('castellar',8),bg='light blue')
        self.final_travel2.place(x=780,y=447)

        self.final_destination2 = Label(self.final_booking_frame,text=self.destination,font=('castellar',8),bg='light blue')
        self.final_destination2.place(x=780,y=425)

        self.back_button = Button(self.final_booking_frame,image=passanger_quit_img,command=self.booking_frame.destroy)
        self.back_button.place(x=10,y=600)

    def organization_login(self):

        ''':ORGANIZATION_LOGIN:
                        the purpose of this method is to display the login window in the organization
                        login frame.

                        when you press the organiztion button in master frame this method
                        is called

                        :METHOD CONTAINS:

                        frame=1 ; label=3 ; button=2'''
        self.organization_login_frame = Frame(self.master, width=1000, height=900, bg='#EBF2F8')
        self.organization_login_frame.place(x=0, y=0)
        self.organization_login_frame.tkraise()
        self.organization_icon = Label(self.organization_login_frame, image = img10, bd=0, bg='#EBF2F8')
        self.organization_icon.place(x=350, y=10)
        self.username_label = Label(self.organization_login_frame, text='Username', font=('Berlin Sans FB', 16), bg='#EBF2F8')
        self.username_label.place(x=405, y=200)
        self.organization_username_entry = Entry(self.organization_login_frame, bg='white', relief='sunken', highlightcolor='#D2E0F1',
                                       highlightthickness=1, highlightbackground='#D8D6D7', font=('Tw Cen MT', 14))
        self.organization_username_entry.place(x=350, y=240)
        self.password_label = Label(self.organization_login_frame, text='Password', font=('Berlin Sans FB', 16), bg='#EBF2F8')
        self.password_label.place(x=405, y=280)
        self.organization_password_entry = Entry(self.organization_login_frame, bg='white', show='*', relief='sunken',
                                       highlightcolor='#D2E0F1', highlightthickness=1, highlightbackground='#D8D6D7',
                                       font=('Tw Cen MT', 14))
        self.organization_password_entry.place(x=350, y=320)
        self.organization_password_entry.bind('<Return>',self.check_login_organization)
        self.login_button = Button(self.organization_login_frame, image = img12, bd=0, bg='#EBF2F8')
        self.login_button.bind('<Button-1>',self.check_login_organization)
        self.login_button.place(x=354, y=395)
        self.cancel_button = Button(self.organization_login_frame, image = img11,command=self.organization_login_frame.destroy, bd=0, bg='#EBF2F8')
        self.cancel_button.place(x=354, y=435)

    def check_login_organization(self,events):

        ''':CHECK_LOGIN_ORGANIZATION:
                        the purpose of this method is to check the whether the admin written the right
                        username and password and after checking it it opens to a new frame organization
                        frame which contain some buttons

                        when you press the login button in organization login frame this method is called

                        :METHOD CONTAINS:

                        frame=1 ; label=2 ; button=4'''
        try:
            if self.organization_username_entry.get() == 'admin' and self.organization_password_entry.get() == 'password':
                tkinter.messagebox.showinfo('Welcome','Welcome Admin')
                self.organiztion_section = Frame(self.organization_login_frame, width=1000, height=900, bg='#EBF2F8')
                self.organiztion_section.place(x=0, y=0)
                self.organiztion_section.tkraise()
                self.welcome_label = Label(self.organiztion_section, image=img3)
                self.welcome_label.place(x=0, y=0)
                self.org_label = Label(self.organiztion_section, image=org_img)
                self.org_label.place(x=0, y=245)
                self.emp_button = Button(self.organiztion_section, image=org_peeps, command=self.Main)
                self.emp_button.place(x=130, y=300)
                self.flightbutton = Button(self.organiztion_section, image=schedule, command=self.org_flights,
                                           bg='white')
                self.flightbutton.place(x=300, y=300)
                self.plane_button = Button(self.organiztion_section, image=plane, command=self.our_planes)
                self.plane_button.place(x=450, y=300)
                self.back_button = Button(self.organiztion_section, image=passanger_quit_img,
                                          command=self.organiztion_section.destroy)
                self.back_button.place(x=600, y=300)


            else:
                raise incorrect_username_or_password

        except incorrect_username_or_password:
            tkinter.messagebox.showinfo('ERROR', 'Incorrect Username or Password')

    def end_organization(self):

        ''':END_ORGANIZATION:
                                the purpose of this method is to move in the organization login frame.

                                when you press the cancel button in organization login frame
                                 this method is called'''
        self.organization_login()

    def our_planes(self):
        ''':OUR PLNAES:
        this method is called when the planes button existing in the organization login frame is pressed

        the purpose of this method is to show all the planes of our airline

        :METHOD CONTAINS:

        frame=1 ; label=3 ;button=1'''
        self.plane_frame = Frame(self.organiztion_section , width=1000 , height=900)
        self.plane_frame.place(x=0,y=0)
        self.plane_frame.tkraise()
        self.plane_img_label1 = Label(self.plane_frame,image=our_plane1)
        self.plane_img_label1.place(x=0,y=0)
        self.plane_img_label2 = Label(self.plane_frame,image=our_plane2)
        self.plane_img_label2.place(x=450,y=0)
        self.plane_img_label3 = Label(self.plane_frame,image=our_plane3)
        self.plane_img_label3.place(x=450,y=270)
        self.quit = Button(self.plane_frame,command=self.plane_frame.destroy,image=passanger_quit_img)
        self.quit.place(x=700,y=500)
        Aeroplanes().aeroplane('BD-700 Global Express', 'Boeing 747-400', 'Airbus A340-600', 'Boeing 777-300',
                               'Airbus A380plus', 'B-2 Spirit', 'Shaheen 7631')



    def org_flights(self):

        """
                Displays the days on which the flights are scheduled.

                It contains:
                    Toplevels=1 , Buttons=1 , Labels=5
                """
        self.totaltop = Toplevel(self.organiztion_section, bg='#edfffe')
        self.totaltop.geometry('1200x900')

        self.totalnoticelabel = Label(self.totaltop, text='THE COMPLETE SCHEDULE FOR THE FLIGHTS IS',
                                      font='Helvetica 15 underline bold', fg='dark blue', bg='#edfffe')
        self.totalnoticelabel.pack(side=TOP)

        self.theflights = Flights().TotalSchedule()

        self.closetotaltop = Button(self.totaltop, image=close2img, command=self.totaltop.destroy)
        self.closetotaltop.pack(side=RIGHT)

        for a in Flights().totallist:
            self.totalspace1 = Label(self.totaltop,
                                     text='-------------------------------------------------------------------------------------------',
                                     bg='#edfffe')
            self.totallabel = Label(self.totaltop, text=a, font='times 15 bold', fg='black', bg='orange')
            self.totalspace2 = Label(self.totaltop,
                                     text='-------------------------------------------------------------------------------------------',
                                     bg='#edfffe')
            self.totalspace3 = Label(self.totaltop,
                                     text='-------------------------------------------------------------------------------------------',
                                     bg='#edfffe')
            self.totalspace1.pack()
            self.totallabel.pack()
            self.totalspace2.pack()
            self.totalspace3.pack()

    def flightswindow(self):
        """
        Displays the window containing all flights related information.

        It is subdivided into 4 categories namely Days, Dates, Time and Total Schedule.

        It contains:
            Frames=1 , Buttons=5 , Labels=2
        """

        self.flightframe = Frame(self.passenger_section, width=1000, height=900, bg='#F6F6F6')
        self.flightframe.place(x=0, y=0)
        self.flightframe.tkraise()

        self.toplabel = Label(self.flightframe, image=fortopimg)
        self.toplabel.place(x=0, y=0)

        self.flightwindowlabel = Label(self.flightframe, image=flightwindowimg)
        self.flightwindowlabel.place(x=0, y=200)

        self.daybutton = Button(self.flightframe, image=dayimg, bg='grey', command=self.dayswindow)
        self.daybutton.place(x=100, y=250)

        self.datebutton = Button(self.flightframe, image=dateimg, bg='grey', command=self.datewindow)
        self.datebutton.place(x=300, y=250)

        self.timebutton = Button(self.flightframe, image=timeimg, bg='grey', command=self.timewindow)
        self.timebutton.place(x=500, y=250)

        self.totalbutton = Button(self.flightframe, image=totalimg, bg='grey', command=self.totalwindow)
        self.totalbutton.place(x=700, y=250)

        self.backflightwindowbutton = Button(self.flightframe, image=back1img, bg='grey',
                                             command=self.flightframe.destroy)
        self.backflightwindowbutton.place(x=450, y=580)

    def dayswindow(self):
        """
        Displays the days on which the flights are scheduled.

        It contains:
            Toplevels=1 , Buttons=1 , Labels=5
        """
        self.daytop = Toplevel(self.flightframe, bg='#edfffe')
        self.daytop.geometry('1000x900')

        self.daynoticelabel = Label(self.daytop, text='   FLIGHTS HAVE BEEN SCHEDULED IN THE FOLLOWING DAYS',
                                    font='Helvetica 15 underline bold', fg='dark blue', bg='#edfffe')
        self.daynoticelabel.pack(side=TOP)

        self.theflights = Flights().Day()

        self.closedaytop = Button(self.daytop, image=close1img, command=self.daytop.destroy)
        self.closedaytop.pack(side=RIGHT)

        for a in Flights().daylist:
            self.dayspace1 = Label(self.daytop,
                                   text='-------------------------------------------------------------------------------------------',
                                   bg='#edfffe')
            self.daylabel = Label(self.daytop, text=a, font='times 17 bold', fg='black', bg='orange')
            self.dayspace2 = Label(self.daytop,
                                   text='-------------------------------------------------------------------------------------------',
                                   bg='#edfffe')
            self.dayspace3 = Label(self.daytop,
                                   text='-------------------------------------------------------------------------------------------',
                                   bg='#edfffe')
            self.dayspace1.pack()
            self.daylabel.pack()
            self.dayspace2.pack()
            self.dayspace3.pack()

    def datewindow(self):
        """
        Displays the dates on which the flights are scheduled.

        It contains:
            Toplevels=1 , Buttons=1 , Labels=5
        """

        self.datetop = Toplevel(self.flightframe, bg='#edfffe')
        self.datetop.geometry('1000x900')

        self.datenoticelabel = Label(self.datetop, text='   FLIGHTS HAVE BEEN SCHEDULED ON THE FOLLOWING DATES',
                                     font='Helvetica 15 underline bold', fg='dark blue', bg='#edfffe')
        self.datenoticelabel.pack(side=TOP)

        self.theflights = Flights().Date()

        self.closedatetop = Button(self.datetop, image=close2img, command=self.datetop.destroy)
        self.closedatetop.pack(side=RIGHT)

        for a in Flights().datelist:
            self.datespace1 = Label(self.datetop,
                                    text='-------------------------------------------------------------------------------------------',
                                    bg='#edfffe')
            self.datelabel = Label(self.datetop, text=a, font='times 17 bold', fg='black', bg='orange')
            self.datespace2 = Label(self.datetop,
                                    text='-------------------------------------------------------------------------------------------',
                                    bg='#edfffe')
            self.datespace3 = Label(self.datetop,
                                    text='-------------------------------------------------------------------------------------------',
                                    bg='#edfffe')
            self.datespace1.pack()
            self.datelabel.pack()
            self.datespace2.pack()
            self.datespace3.pack()

    def timewindow(self):
        """
        Displays the time on which the flights are scheduled.

        It contains:
            Toplevels=1 , Buttons=1 , Labels=5
        """

        self.timetop = Toplevel(self.flightframe, bg='#edfffe')
        self.timetop.geometry('1000x900')

        self.timenoticelabel = Label(self.timetop, text='   FLIGHTS HAVE BEEN SCHEDULED ON THE FOLLOWING TIMES',
                                     font='Helvetica 15 underline bold', fg='dark blue', bg='#edfffe')
        self.timenoticelabel.pack(side=TOP)

        self.theflights = Flights().Time()

        self.closetimetop = Button(self.timetop, image=close1img, command=self.timetop.destroy)
        self.closetimetop.pack(side=RIGHT)

        for a in Flights().timelist:
            self.timespace1 = Label(self.timetop,
                                    text='-------------------------------------------------------------------------------------------',
                                    bg='#edfffe')
            self.timelabel = Label(self.timetop, text=a, font='times 17 bold', fg='black', bg='orange')
            self.timespace2 = Label(self.timetop,
                                    text='-------------------------------------------------------------------------------------------',
                                    bg='#edfffe')
            self.timespace3 = Label(self.timetop,
                                    text='-------------------------------------------------------------------------------------------',
                                    bg='#edfffe')
            self.timespace1.pack()
            self.timelabel.pack()
            self.timespace2.pack()
            self.timespace3.pack()

    def totalwindow(self):
        """
        Displays the scheduled days,dates,time,name of aeroplanes and their destination.

        It contains:
            Toplevels=1 , Buttons=1 , Labels=5
        """

        self.totaltop = Toplevel(self.flightframe, bg='#edfffe')
        self.totaltop.geometry('1200x900')

        self.totalnoticelabel = Label(self.totaltop, text='THE COMPLETE SCHEDULE FOR THE FLIGHTS IS',
                                      font='Helvetica 15 underline bold', fg='dark blue', bg='#edfffe')
        self.totalnoticelabel.pack(side=TOP)

        self.theflights = Flights().TotalSchedule()

        self.closetotaltop = Button(self.totaltop, image=close2img, command=self.totaltop.destroy)
        self.closetotaltop.pack(side=RIGHT)

        for a in Flights().totallist:
            self.totalspace1 = Label(self.totaltop,
                                     text='-------------------------------------------------------------------------------------------',
                                     bg='#edfffe')
            self.totallabel = Label(self.totaltop, text=a, font='times 15 bold', fg='black', bg='orange')
            self.totalspace2 = Label(self.totaltop,
                                     text='-------------------------------------------------------------------------------------------',
                                     bg='#edfffe')
            self.totalspace3 = Label(self.totaltop,
                                     text='-------------------------------------------------------------------------------------------',
                                     bg='#edfffe')
            self.totalspace1.pack()
            self.totallabel.pack()
            self.totalspace2.pack()
            self.totalspace3.pack()

    def helpcornerwindow(self):
        """
        Displays the window on which the flights are scheduled.

        It is subdivided into 3 categories namely Contact Us, FAQs and Map.

        It contains:
            Toplevels=1 , Buttons=1 , Labels=5
        """

        self.helpframe = Frame(self.passenger_section , width=1000, height=900)
        self.helpframe.place(x=0, y=0)
        self.helpframe.tkraise()

        self.toplabel = Label(self.helpframe, image=fortopimg)
        self.toplabel.place(x=0, y=0)

        self.helpwindowlabel = Label(self.helpframe, image=helpwindowimg)
        self.helpwindowlabel.place(x=0, y=200)

        self.contactbutton = Button(self.helpframe, image=contactusimg, command=self.contactuswindow)
        self.contactbutton.place(x=120, y=300)

        self.faqbutton = Button(self.helpframe, image=faqimg, command=self.faqswindow)
        self.faqbutton.place(x=420, y=300)

        self.mapbutton = Button(self.helpframe, image=mapbuttonimg, command=self.mapwindow)
        self.mapbutton.place(x=120, y=530)

        self.backhelpwindowbutton = Button(self.helpframe, image=back2img, command=self.helpframe.destroy)
        self.backhelpwindowbutton.place(x=420, y=530)

    def contactuswindow(self):
        """
        Displays various sources through which we can contact the respective officer.

        It contains:
            Toplevels=1 , Buttons=1 , Labels=2
        """

        self.contactustop = Toplevel(self.helpframe)
        self.contactustop.geometry('1000x900')

        self.bgimglabel = Label(self.contactustop, image=forbg1img)
        self.bgimglabel.place(x=0, y=0)

        self.thehelpcorner = HelpCorner().contact_us()
        self.contacttext = StringVar()
        self.contacttext.set(self.thehelpcorner)
        self.contactuslabel = Label(self.contactustop, textvariable=self.contacttext, font=('Times', 18, 'bold'),
                                    bg='#f3f99f', fg='blue')
        self.contactuslabel.place(x=80, y=100)

        self.closecontactus = Button(self.contactustop, image=close1img, command=self.contactustop.destroy)
        self.closecontactus.place(x=500, y=600)

    def faqswindow(self):
        """
        Displays different Questions and their Answers which can guide or assist the passengers.

        It contains:
            Toplevels=1 , Buttons=1 , Labels=3
        """

        self.faqstop = Toplevel(self.helpframe)
        self.faqstop.geometry('1000x900')

        self.bgimglabel = Label(self.faqstop, image=forbg3img)
        self.bgimglabel.place(x=0, y=0)

        self.faqsheadinglabel = Label(self.faqstop, text="FAQS", fg='white', bg='#046dae',
                                      font='elephant 35 underline bold')
        self.faqsheadinglabel.place(x=450, y=10)

        self.thehelpcorner = HelpCorner().FAQs()
        self.faqstext = StringVar()
        self.faqstext.set(self.thehelpcorner)
        self.faqslabel = Label(self.faqstop, textvariable=self.faqstext, font='times 16 bold italic', justify='left',
                               fg='white', bg='#046dae')
        self.faqslabel.place(x=16, y=85)

        self.closefaqs = Button(self.faqstop, image=close2img, command=self.faqstop.destroy)
        self.closefaqs.place(x=460, y=610)

    def mapwindow(self):
        """
        Displays the map to the SSK Airways office.

        It contains:
            Toplevels=1 , Buttons=1 , Labels=3
        """

        self.maptop = Toplevel(self.helpframe, bg='#EBF2F8')
        self.maptop.geometry('1000x900')

        self.bgimglabel = Label(self.maptop, image=forbg2img)
        self.bgimglabel.place(x=0, y=0)

        self.thehelpcorner = HelpCorner().Map()
        self.maptext = StringVar()
        self.maptext.set(self.thehelpcorner)
        self.maplabel = Label(self.maptop, textvariable=self.maptext, fg='dark blue', bg='#9cd1fd',
                              font='times 18 underline bold')
        self.maplabel.place(x=400, y=60)

        self.mapimglabel = Label(self.maptop, image=mapimg, bg='black')
        self.mapimglabel.place(x=200, y=130)

        self.closemap = Button(self.maptop, image=close1img, command=self.maptop.destroy)
        self.closemap.place(x=500, y=600)

    def mainrental(self):
        ''':MAIN RENTAL:

        this method is used to call the window of royal rental services

        :METHOD CONTAINS:

        toplevel=1 ; label=6 ; entry=2 ; button=3 '''
        global name_entry
        global location_entry
        global credit_entry
        self.Rental_window = Toplevel(self.passenger_section,bg='black')
        self.Rental_window.geometry('1000x900')
        self.Rental_window.title('ROYAL RENTAL SERVICES LTD')

        self.royal_label = Label(self.Rental_window, image=royal_img, bg="BLACK")
        self.royal_label.place(x=0,y=0)

        self.name_label = Label(self.Rental_window , text='NAME',bg='BLACK',fg='GOLD')
        self.name_label.place(x=100,y=400)

        self.location_label = Label(self.Rental_window , text='LOCATION',bg='BLACK',fg='GOLD')
        self.location_label.place(x=100,y=450)

        self.credit_label = Label(self.Rental_window, text='CREDIT CARD NO',bg='BLACK',fg='GOLD')
        self.credit_label.place(x=100,y=500)

        name_entry = Entry(self.Rental_window)
        name_entry.place(x=210,y=400)

        location_entry = Entry(self.Rental_window)
        location_entry.place(x=210,y=450)

        credit_entry = Entry(self.Rental_window)
        credit_entry.place(x=210,y=500)

        self.instruction_label = Label(self.Rental_window , bg='BLACK',fg='GOLD',text='INSTRUCTION:\n\nThe Royal Rental Service LTD only operates within 500m radius\n\nCarefully choose from the given two classes\n\nCharges of economy class is 5$ per 50meter\n\nCharges of business class is 10$ per 50meter\n\nOnly four passangers max are allowed\n\nFare may vary depending upon various factors such as traffic,waiting time etc\n\nOnce you book the ride your bill will be dispatched to the respective credit card no you entered\n\nFor any query you can contact our helpline no:123456789\n\nThankyou for choosing Royal Rental Services LTD a proud partner of SSK airways')
        self.instruction_label.place(x=495,y=403)

        self.blank_label=Label(self.Rental_window,bg='Black',fg='Gold',text='')
        self.blank_label.place(x=1,y=600)

        self.eco_button=Button(self.Rental_window , text='ECONOMY', bg='BLACK' , fg='GOLD' , command = self.economy)
        self.eco_button.place(x=100,y=600)

        self.business_button=Button(self.Rental_window , text='BUSINESS', bg='BLACK' , fg='GOLD' , command=self.business)
        self.business_button.place(x=220,y=600)

        self.quit_button = Button(self.Rental_window,text='QUIT',bg='BLACK',fg="GOLD",command=self.Rental_window.destroy)
        self.quit_button.place(x=160,y=650)

    def economy(self):
        ''':ECONOMY:

        this method is called when we press the economy button in the royal main method

        this method will display all the input given in the royal main window

        :METHOD CONTAINS:

        frame=1 ; label=9 ; button=1'''
        a = name_entry.get()
        b = location_entry.get()
        c = credit_entry.get()
        self.eco_frame = Frame(self.Rental_window , bg='BLACK' , height=1000 , width=1000)
        self.eco_frame.tkraise()
        self.eco_frame.place(x=0,y=0)
        self.name_label = Label(self.eco_frame , text='YOUR RIDE HAS BEEN BOOKED BY THE NAME:' ,bg='BLACK',fg="GOLD")
        self.name_label.place(x=100,y=100)
        self.name_label_given = Label(self.eco_frame, text=a , bg='BLACK' , fg='gold')
        self.name_label_given.place(x=400, y=100)
        self.location_label_given = Label(self.eco_frame, text=b , bg='black',fg='gold')
        self.location_label_given.place(x=400, y=200)
        self.credit_label_given = Label(self.eco_frame, text=c , bg='black',fg='gold')
        self.credit_label_given.place(x=400, y=300)
        self.location_label = Label(self.eco_frame , text='YOUR DROP OFF DESTINATION IS:', bg='black',fg='gold')
        self.location_label.place(x=100,y=200)
        self.credit_label = Label(self.eco_frame , text='YOUR CREDIT CARD NO IS:', bg='black',fg='gold')
        self.credit_label.place(x=100,y=300)
        self.class_label = Label(self.eco_frame , text='YOU HAVE CHOSEN ECONOMY CLASS', bg='black',fg='gold')
        self.class_label.place(x=100,y=400)
        self.label = Label(self.eco_frame , text="THANKYOU FOR USING ROYAL RENTAL SERVICES LTD", bg='black',fg='gold')
        self.label.place(x=100,y=500)
        self.charges_label = Label(self.eco_frame,text='CHARGES:\n\nTHE CHARGES OF ECONOMY CLASS ARE 5$ PER 50 METERS WHICH MIGHT VARY', bg='black',fg='gold')
        self.charges_label.place(x=100,y=550)
        self.back_button = Button(self.eco_frame , text='DONE' , bg='black',fg='gold',command=self.quit)
        self.back_button.place(x=100,y=650)

    def business(self):
        ''':BUSINESS:

        this method is called when we press the business button in the royal main method

        this method will display all the input given in the royal main window

        :METHOD CONTAINS:

        frame=1 ; label=9 ; button=1'''

        a = name_entry.get()
        b = location_entry.get()
        c = credit_entry.get()
        self.business_frame = Frame(self.Rental_window, bg='BLACK' , height=1000 , width=1000)
        self.business_frame.tkraise()
        self.business_frame.place(x=0,y=0)
        self.name_label = Label(self.business_frame , text='YOUR RIDE HAS BEEN BOOKED BY THE NAME:' ,bg='BLACK',fg="GOLD")
        self.name_label.place(x=100,y=100)
        self.name_label_given = Label(self.business_frame, text=a , bg='BLACK' , fg='gold')
        self.name_label_given.place(x=400, y=100)
        self.location_label_given = Label(self.business_frame, text=b , bg='black',fg='gold')
        self.location_label_given.place(x=400, y=200)
        self.credit_label_given = Label(self.business_frame, text=c , bg='black',fg='gold')
        self.credit_label_given.place(x=400, y=300)
        self.location_label = Label(self.business_frame , text='YOUR DROP OFF DESTINATION IS:', bg='black',fg='gold')
        self.location_label.place(x=100,y=200)
        self.credit_label = Label(self.business_frame , text='YOUR CREDIT CARD NO IS:', bg='black',fg='gold')
        self.credit_label.place(x=100,y=300)
        self.class_label = Label(self.business_frame , text='YOU HAVE CHOSEN ECONOMY CLASS', bg='black',fg='gold')
        self.class_label.place(x=100,y=400)
        self.label = Label(self.business_frame , text="THANKYOU FOR USING ROYAL RENTAL SERVICES LTD", bg='black',fg='gold')
        self.label.place(x=100,y=500)
        self.charges_label = Label(self.business_frame,text='CHARGES:\n\nTHE CHARGES OF BUSINESS CLASS ARE 10$ PER 50 METERS WHICH MIGHT VARY', bg='black',fg='gold')
        self.charges_label.place(x=100,y=550)

        self.back_button = Button(self.business_frame , text='DONE' , bg='black',fg='gold',command=self.business_quit)
        self.back_button.place(x=100,y=650)

    def quit(self):
        '''it is used to quit the economy window'''
        self.eco_frame.destroy()

    def business_quit(self):
        '''this method is used to quit the business window '''
        self.business_frame.destroy()

    def Main(self):
        ''':MAIN:

        this method contains all the necessary buttons which upon pressing would accessn the database of the employees

        :METHOD CONTAINS:

        frame=1 ; label=2 ; buttons=6'''

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

        self.marshall_img = PhotoImage(file='marshall1.png')
        sky_marshall_button = Button(self.emp_frame, command=self.sky_marshall_records, bg='white',
                                     image=self.marshall_img)
        sky_marshall_button.place(x=160, y=270)

        self.hostess_img = PhotoImage(file='airhostess1.png')
        self.arihostess_button = Button(self.emp_frame, command=self.air_hostess_records, bg='white',
                                        image=self.hostess_img)
        self.arihostess_button.place(x=310, y=270)

        self.aviator_img = PhotoImage(file='aviator1.png')
        self.aviator_button = Button(self.emp_frame, command=self.aviator_records, bg='white', image=self.aviator_img)
        self.aviator_button.place(x=480, y=270)

        self.janitor_img = PhotoImage(file='jani.png')
        self.janitor_button = Button(self.emp_frame, command=self.janitor_records, bg='white', image=self.janitor_img)
        self.janitor_button.place(x=630, y=270)

        self.quit_img = PhotoImage(file='quitbutton.png')
        self.quit_button = Button(self.emp_frame, command=self.quit_emp, image=self.quit_img)
        self.quit_button.place(x=780, y=270)

    def quit_emp(self):
        ''':QUIT EMP:

        this method will end the emp frame

        '''
        self.emp_frame.destroy()

    pilot_record_frame = None

    def pilot_records(self):
        ''':PILOT RECORDS:

        this method contains all the inforamtion about the pilots
        to be dispalyed to the organization

        :METHOD CONTAINS:

        window=1 ; button=1 ; label=14

        '''
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
        '''this method is used to end the pilot window'''
        pilot_records_frame.destroy()

    sky_marshall_records_frame = None

    def sky_marshall_records(self):
        ''':SKY MARSHALL RECORDS:

        this method contains all the inforamtion about the sky marshall
        to be dispalyed to the organization

        :METHOD CONTAINS:

        window=1 ; button=1 ; label=7

        '''

        global sky_marshall_records_frame

        sky_marshall_records_frame = Tk()
        sky_marshall_records_frame.title('SKY MARSHALLS')
        self.marshallobj = Sky_marshall().records()

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
        '''this method is used to end the sky marshall window'''

        sky_marshall_records_frame.destroy()

    hostess_record_window = None

    def air_hostess_records(self):
        ''':AIR HOSTESS RECORDS:

        this method contains all the inforamtion about the air hostess
        to be dispalyed to the organization

        :METHOD CONTAINS:

        window=1 ; button=1 ; label=14

        '''

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
        '''this method is used to end the air hostess window'''

        hostess_record_window.destroy()

    janitor_records_window = None

    def janitor_records(self):
        ''':JANITOR RECORDS:

        this method contains all the inforamtion about the janitor
        to be dispalyed to the organization

        :METHOD CONTAINS:

        window=1 ; button=1 ; label=7

        '''

        global janitor_records_window

        janitor_records_window = Tk()
        janitor_records_window.title('JANITORS')
        self.janitorobj = Janitor().records()

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
        '''this method is used to end the air hostess window'''

        janitor_records_window.destroy()

    aviator_records_window = None

    def aviator_records(self):
        ''':AVIATOR RECORDS:

        this method contains all the inforamtion about the aviator
        to be dispalyed to the organization

        :METHOD CONTAINS:

        window=1 ; button=1 ; label=7

        '''

        global aviator_records_window

        aviator_records_window = Tk()
        aviator_records_window.title('JANITORS')
        self.aviatorobj = Aviator().records()

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
        '''this method is used to end the aviator window'''

        aviator_records_window.destroy()

if __name__ == '__main__':
    root=None
    try:
        #a=Passenger_Accounts()
        #a.passenger_login()
        root = Tk()
        img1 = PhotoImage(file='organization_logo.png')
        img2 = PhotoImage(file='passenger_logo.png')
        img3 = PhotoImage(file='logo1a.png')
        img4 = PhotoImage(file='cancel-button.png')
        img5 = PhotoImage(file='login-button.png')
        img6 = PhotoImage(file='signup-button.png')
        img7 = PhotoImage(file='passanger-icon.png')
        img8 = PhotoImage(file='cancel-button.png')
        img9 = PhotoImage(file='signup-button.png')
        img10 = PhotoImage(file='organization-icon.png')
        img11 = PhotoImage(file='cancel-button.png')
        img12 = PhotoImage(file='login-button.png')
        img13 = PhotoImage(file='creditcard-image.png')
        img14 = PhotoImage(file='ok-button.png')
        img15 = PhotoImage(file='creditcard-image.png')
        mapimg = PhotoImage(file='map.png')
        timeimg = PhotoImage(file='time.png')
        fortopimg = PhotoImage(file='fortop.png')
        flightwindowimg = PhotoImage(file='flightwindow.png')
        helpwindowimg = PhotoImage(file='helpwindow.png')
        dayimg = PhotoImage(file='day.png')
        dateimg = PhotoImage(file='date.png')
        totalimg = PhotoImage(file='total.png')
        back1img = PhotoImage(file='back1.png')
        back2img = PhotoImage(file='back2.png')
        back3img = PhotoImage(file='back3.png')
        close1img = PhotoImage(file='close1.png')
        close2img = PhotoImage(file='close2.png')
        contactusimg = PhotoImage(file='contactus.png')
        faqimg = PhotoImage(file='faq.png')
        mapbuttonimg = PhotoImage(file='mapbutton.png')
        forbg1img = PhotoImage(file='forbg1.png')
        forbg2img = PhotoImage(file='forbg2.png')
        forbg3img = PhotoImage(file='forbg3.png')
        royal_img = PhotoImage(file='royallogo.png')
        royal_button_img = PhotoImage(file='royallogobutton.png')
        phelp_button_img = PhotoImage(file='help1.png')
        flight_button_img = PhotoImage(file='travel.png')
        passanger_quit_img = PhotoImage(file='quitbutton.png')
        view_img = PhotoImage(file='view.png')
        schedule = PhotoImage(file='schedule.png')
        org_peeps = PhotoImage(file='orgemp.png')
        plane = PhotoImage(file='planes.png')
        org_img = PhotoImage(file='org_img.png')
        booking = PhotoImage(file='ticket.png')
        booking_logo = PhotoImage(file='travelling.png')
        booking_final = PhotoImage(file='ticket_img.png')
        our_plane1 = PhotoImage(file='our plane1.png')
        our_plane2 = PhotoImage(file='our plane2.png')
        our_plane3 = PhotoImage(file='our plane3.png')
        a = main_page(root)
        root.mainloop()
    except Exception as error:
        root.withdraw()
        tkinter.messagebox.showerror("Error", error)
    else:
        pass
    finally:
        tkinter.messagebox.showinfo('SSKAIRWAYS', 'THANK YOU FOR VISITING\nWE HOPE TO SEE YOU AGAIN ;) \n************************************************')