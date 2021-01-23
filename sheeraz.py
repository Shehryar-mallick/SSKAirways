def add():
    x = int(input('enter any no:'))
    y = int(input('enter 2nd no:'))
    print('THE RESULT IS:',x+y,'\n*****************************')
def sub():
    x = int(input('enter any no:'))
    y = int(input('enter 2nd no:'))
    print('THE RESULT IS:',x-y,'\n*****************************')
def mul():
    x = int(input('enter any no:'))
    y = int(input('enter 2nd no:'))
    print('THE RESULT IS:',x*y,'\n*****************************')
def div():
    x = int(input('enter any no:'))
    y = int(input('enter 2nd no:'))
    print('THE RESULT IS:',x/y,'\n*****************************')

while 1:
    try:
        choice = str(input(
            'FOR ADDING TWO NUMBERS PRESS A\nFOR SUBTRACTION PRESS B\nFOR MULTIPLICATION PRESS C\nFOR DIVISION PRESS D\nIF YOU WISH TO EXIT PRESS E\nENTER CHOICE:'))

        if choice == 'A':
            add()

        elif choice == 'B':
            sub()

        elif choice == 'C':
            mul()

        elif choice == 'D':
            div()

        elif choice == 'E':
            print('NOW EXITING\nA PROJECT BY SHEERAZ MALLICK & ABDULLAH KHAN')
            break

    except ValueError:
        print('************************************\nwrong input please try again :)\n************************************')

    except ZeroDivisionError:
        print('***********************************\ndenomenator cannot be zero\n*********************************')
