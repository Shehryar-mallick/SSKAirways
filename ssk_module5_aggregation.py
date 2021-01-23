class Creator1:
    """This is a class which is a content for the Aggregation."""

    def __init__(self,name1):
        """
        A Parameterized Constructor which takes a name.

        :param name1: Name of first person who is the creator of SSK Airways.
        """

        self.name1=name1
    def creator(self):
        """
        A method to reserve the name given in the previous constructor.

        :return:
            Returns the name of the 1 of the 3 creators of SSK Airways.
        """

        return self.name1

class Creator2:
    """This is a class which is a content for Aggregation."""

    def __init__(self,name2):
        """
        A Parameterized Constructor which takes a name.

        :param name1: Name of second person who is the creator of SSK Airways.
        """
        self.name2=name2
    def creator(self):
        """
        A method to reserve the name given in the previous constructor.

        :return:
            Returns the name of the 2nd of the 3 creators of SSK Airways.
        """
        return self.name2

class Creator3:
    """This is a class which is a content for Aggregation."""

    def __init__(self,name3):
        """
        A Parameterized Constructor which takes a name.

        :param name1: Name of third person who is the creator of SSK Airways.
        """
        self.name3=name3

    def creator(self):
        """
        A method to reserve the name given in the previous constructor.

        :return:
            Returns the name of the 3rd of the 3 creators of SSK Airways.
        """
        return self.name3

class SSKAirways:
    """This is a class which is a container of the three contents for Aggregation."""

    def __init__(self,name1,name2,name3,year):
        """
        A Paramterized Constructor which takes three names and a year

        :param name1: This parameter accounts for the object of 1st content i.e Creator1 class.
        :param name2: This parameter accounts for the object of 2nd content i.e Creator2 class.
        :param name3: This parameter accounts for the object of 3rd content i.e Creator3 class.
        :param year: This parameter is the year on which SSK Airways is established.
        """

        self.name1=name1
        self.name2=name2
        self.name3=name3
        self.year=year
    def __str__(self):
        """A built-in method which is overloaded to return the statements (in the form of a string)."""

        return '{},{} and {} are the Creators of SSK Airways which is established in {} ©'.format(self.name1.creator(),self.name2.creator(),self.name3.creator(),self.year)


obj_creator1 = Creator1('Mr.Saad')
obj_creator2 = Creator2('Mr.Shehryar')
obj_creator3 = Creator3('Mr.Khalid')
obj_sskairways = SSKAirways(obj_creator1, obj_creator2, obj_creator3, 2019)
