from tkinter import *
import tkinter.messagebox
class Aeroplanes:
    """This is a class which demonstrates the Method Overloading in Python."""

    def aeroplane(self, name1=None, *args):
        """
        A method to indicate Method Overloading by calling when giving no arguments and calling when arguments given.

        :param name1: Initialized as None which could take the name of an aeroplane.
        :param args: If more aeroplane names are to be inserted then this parameter is useful.

        :return:
            Name of aeroplane(s) if argument(s) is/are passed.
            A single statement of Not Availability when no argument is passed.
        """
        #
        # self.name1 = name1
        # if name1 is not None:
        #      #print('AEROPLANE:%s' % (name1.title()))
        #      tkinter.messagebox.showinfo('planes',name1)
        # else:
        #      print('No plane available right now')
        self.l = []
        for arg in args:
            if arg is not None:
                #print('AEROPLANE:' + arg)
                self.l.append(arg)

            else:
                break

        tkinter.messagebox.showinfo('planes', 'the planes are: '+ str(self.l))

#Aeroplanes().aeroplane()
#Aeroplanes().aeroplane('BD-700 Global Express','Boeing 747-400','Airbus A340-600','Boeing 777-300','Airbus A380plus','B-2 Spirit','Shaheen 7631')