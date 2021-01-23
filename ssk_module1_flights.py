import sqlite3
class Flights:
    """This is a class which has all the data related to the schedules of flights."""

    def __init__(self):
        """
        Default Construct of the Flights class

        It creates or connects the database file so that we can enter all the data that is
        related to the flights as much as we want. The commit() command puts all the data into the database.
        """

        self.connection = sqlite3.connect('Flights.db')
        self.cursor = self.connection.cursor()

        #self.cursor.execute('CREATE TABLE flights (day TEXT,date TEXT,time TEXT,aeroplanes TEXT,destinations TEXT)')
        #self.cursor.execute('INSERT INTO flights VALUES(?,?,?,?,?)', ('Monday', '28/5/2019', '9:00 PM','Boeing 747-400','Karachi-Jeddah'))
        #self.cursor.execute('INSERT INTO flights VALUES(?,?,?,?,?)', ('Tuesday', '29/5/2019', '12:40 PM','Boeing 777-300','Karachi-Frankfurt'))
        #self.cursor.execute('INSERT INTO flights VALUES(?,?,?,?,?)', ('Wednesday', '30/5/2019', '11:00 AM','Airbus A340-600','Karachi-Toronto'))
        #self.cursor.execute('INSERT INTO flights VALUES(?,?,?,?,?)', ('Thursday', '31/5/2019', '5:30 PM','Airbus A380plus','Karachi-New York'))
        #self.cursor.execute('INSERT INTO flights VALUES(?,?,?,?,?)', ('Friday', '1/6/2019', '3:45 AM','Shaheen 7631','Karachi-Dubai'))
        #self.cursor.execute('INSERT INTO flights VALUES(?,?,?,?,?)', ('Saturday', '2/6/2019', '12:00 AM','B-2 Spirit','Karachi-London'))
        #self.cursor.execute('INSERT INTO flights VALUES(?,?,?,?,?)', ('Sunday', '3/6/2019', '3:15 PM','BD-700 Global Express','Karachi-Dhaka'))
        #self.connection.commit()

    daylist = []

    def Day(self):
        """
        A method to access all the data of the database and then appends the data of Days in
        a list initialized earlier.

        :return:
            A list containing all the days on which flights are scheduled.
        """

        self.cursor.execute('SELECT * FROM flights')
        rows = self.cursor.fetchall()
        for row in rows:
            self.daylist.append(row[0])
        return self.daylist

    datelist = []

    def Date(self):
        """
        A method to access all the data of the database and then appends the data of Dates in
        a list initialized earlier.

        :return:
            A list containing all the dates on which flights are scheduled.
        """

        self.cursor.execute('SELECT * FROM flights')
        rows = self.cursor.fetchall()
        for row in rows:
            self.datelist.append(row[1])
        return self.datelist

    timelist = []

    def Time(self):
        """
        A method to access all the data of the database and then appends the data of various Times in
        a list initialized earlier.

        :return:
            A list containing different Times on which flights are scheduled.
        """

        self.cursor.execute('SELECT * FROM flights')
        rows = self.cursor.fetchall()
        for row in rows:
            self.timelist.append(row[2])
        return self.timelist

    totallist = []

    def TotalSchedule(self):
        """
        A method to access all the data of the database and then appends the data of every category in
        a list initialized earlier.

        :return:
            A list containing all the scheduled days, dates, times, names of aeroplanes and their destinations.
        """

        self.cursor.execute('SELECT * FROM flights')
        rows = self.cursor.fetchall()
        for row in rows:
            self.totallist.append(
                'DAY:%s   DATE:%s   TIME:%s   AEROPLANES:%s  DESTINATION:%s' % (row[0], row[1], row[2], row[3], row[4]))
        return self.totallist

