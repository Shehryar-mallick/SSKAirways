import sqlite3
class Employee:
    """
    This class contains all the data base of the employees

    it is further inherited by five child classes
    """
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
        conn.commit()'''

    def records(self):
        print('this class contains all th records')
class Pilots(Employee):
    ''':PILOTS:

    this class is a child class of employee and contain a single method

    '''
    conn = sqlite3.connect('Employee.db')
    c = conn.cursor()
    pilot_list = []

    def records(self):
        ''':RECORDS:

        thise method is used to call the records from the data base of the pilots

        '''
        with conn:
            c.execute("SELECT * FROM employees WHERE post ='pilot'")
            data = c.fetchall()
            for row in data:
                self.pilot_list.append(' FIRST:     ' + row[0] + '      LAST:    ' + row[1] + '     SALARY:   ' + str(
                    row[2]) + '    PLANE:      ' + row[3] + '      POST:       ' + row[4])
            return (self.pilot_list)


class Sky_marshall(Employee):
    ''':SKYMARSHALL:

    this class is a child class of employee and contain a single method

    '''

    conn = sqlite3.connect('Employee.db')
    c = conn.cursor()
    sky_marshall_list = []

    def records(self):
        ''':RECORDS:

        thise method is used to call the records from the data base of the skymarshall

        '''

        with conn:
            c.execute("SELECT * FROM employees WHERE post='sky marshall'")
            data = c.fetchall()
            for row in data:
                self.sky_marshall_list.append(
                    ' FIRST:     ' + row[0] + '      LAST:    ' + row[1] + '     SALARY:   ' + str(
                        row[2]) + '    PLANE:      ' + row[3] + '      POST:       ' + row[4])
            return (self.sky_marshall_list)


class Airhostess(Employee):
    ''':AIR HOSTESS:

    this class is a child class of employee and contain a single method

    '''

    conn = sqlite3.connect('Employee.db')
    c = conn.cursor()
    airhostess_list = []

    def records(self):
        ''':RECORDS:

        thise method is used to call the records from the data base of the airhostess

        '''

        c.execute("SELECT * FROM employees WHERE post='airhostess'")
        data = c.fetchall()
        for row in data:
            self.airhostess_list.append(' FIRST:     ' + row[0] + '      LAST:    ' + row[1] + '     SALARY:   ' + str(
                row[2]) + '    PLANE:      ' + row[3] + '      POST:       ' + row[4])
        return (self.airhostess_list)


class Janitor(Employee):
    ''':JANITOR:

    this class is a child class of employee and contain a single method

    '''

    conn = sqlite3.connect('Employee.db')
    c = conn.cursor()
    janitor_list = []

    def records(self):
        ''':RECORDS:

        thise method is used to call the records from the data base of the janitor

        '''

        c.execute("SELECT * FROM employees WHERE post ='janitor'")
        data = c.fetchall()
        # print('FOLLOWING ARE THE JANITORS')
        for row in data:
            self.janitor_list.append(' FIRST:     ' + row[0] + '      LAST:    ' + row[1] + '     SALARY:   ' + str(
                row[2]) + '    PLANE:      ' + row[3] + '      POST:       ' + row[4])
        return (self.janitor_list)


class Aviator(Employee):
    ''':AVIATOR:

    this class is a child class of employee and contain a single method

    '''

    conn = sqlite3.connect('Employee.db')
    c = conn.cursor()
    aviator_list = []

    def records(self):
        ''':RECORDS:

        thise method is used to call the records from the data base of the aviator

        '''

        c.execute("SELECT * FROM employees WHERE post ='aviator'")
        data = c.fetchall()
        # print('FOLLOWING ARE THE AVIATORS')
        for row in data:
            self.aviator_list.append(' FIRST:     ' + row[0] + '      LAST:    ' + row[1] + '     SALARY:   ' + str(
                row[2]) + '    PLANE:      ' + row[3] + '      POST:       ' + row[4])
        return (self.aviator_list)
