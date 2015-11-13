class CarData(object):
    def __init__(self):
        self.type = ''
        self.__year = 0  # check for valid year
        self.manufactor = ''

    @property   #getter
    def year(self):  #write only
        pass

    @year.setter   #setter
    def year(self, y):  #recieving the year
        if y > 2014:  #if date is not valid
            print "Error, invalid date entered"
        else:
            self.__year = y  #printed if the date is validated
