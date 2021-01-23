from tkinter import *

class Royal_Rental_Services:
    #Rental_name_entry = None

    def __init__(self):
        global name_entry
        global location_entry
        global credit_entry
        self.Rental_window = Tk()
        self.Rental_window.geometry('1700x1000')
        self.Rental_window.title('ROYAL RENTAL SERVICES LTD')
        self.royal_img = PhotoImage(file='royallogo1.png')
        self.rental_frame = Frame(self.Rental_window , height=1000,width=1700 , bg='BLACK')
        self.rental_frame.place(x=0,y=0)
        self.royal_label = Label(self.rental_frame, image=self.royal_img, bg="BLACK")
        self.royal_label.place(x=0,y=0)

        self.name_label = Label(self.rental_frame , text='NAME',bg='BLACK',fg='GOLD')
        self.name_label.place(x=100,y=500)

        self.location_label = Label(self.rental_frame , text='LOCATION',bg='BLACK',fg='GOLD')
        self.location_label.place(x=100,y=550)

        self.credit_label = Label(self.rental_frame , text='CREDIT CARD NO',bg='BLACK',fg='GOLD')
        self.credit_label.place(x=100,y=600)

        name_entry = Entry()
        name_entry.place(x=220,y=500)

        location_entry = Entry()
        location_entry.place(x=220,y=550)

        credit_entry = Entry()
        credit_entry.place(x=220,y=600)

        self.instruction_label = Label(self.rental_frame , bg='BLACK',fg='GOLD',text='ISNTRUCTION:\n\nThe Royal Rental Service LTD only operates within 500m radius\n\nCarefully choose from the given two classes\n\nCharges of economy class is 5$ per 50meter\n\nCharges of business class is 10$ per 50meter\n\nOnly four passangers max are allowed\n\nFare may vary depending upon various factors such as traffic,waiting time etc\n\nOnce you book the ride your bill will be dispatched to the respective credit card no you entered\n\nFor any query you can contact our helpline no:123456789\n\nThankyou for choosing Royal Rental Services LTD a proud partner of SSK airways')
        self.instruction_label.place(x=800,y=500)

        self.eco_button=Button(self.rental_frame , text='ECONOMY', bg='BLACK' , fg='GOLD' , command = self.economy)
        self.eco_button.place(x=100,y=650)

        self.business_button=Button(self.rental_frame , text='BUSINESS', bg='BLACK' , fg='GOLD' , command=self.business)
        self.business_button.place(x=220,y=650)

        self.quit_button = Button(self.rental_frame,text='QUIT',bg='BLACK',fg="GOLD",command=self.Rental_window.destroy)
        self.quit_button.place(x=100,y=700)

        #self.map_img = PhotoImage(file='map1.png')
        #self.map_label = Label(self.rental_frame , bg='BLACK',image=self.map_img)
        #self.map_label.place(x=600,y=500)

        self.Rental_window.mainloop()

    def economy(self):
        a = name_entry.get()
        b = location_entry.get()
        c = credit_entry.get()
        self.eco_window = Tk()
        self.eco_window.geometry('700x700')
        self.eco_frame = Frame(self.eco_window , bg='BLACK' , height=700 , width=700)
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
        a = name_entry.get()
        b = location_entry.get()
        c = credit_entry.get()
        self.business_window = Tk()
        self.business_window.geometry('700x700')
        self.business_frame = Frame(self.business_window , bg='BLACK' , height=700 , width=700)
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
        self.eco_window.destroy()
        self.Rental_window.destroy()

    def business_quit(self):
        self.business_window.destroy()
        self.Rental_window.destroy()

ob = Royal_Rental_Services()