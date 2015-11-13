class FavoriteCars(object):
    def __init__(self):
        self.__car_list = []

        #to do list:
        #create an array for info
        #add to that array
        #display a list of cars at the end
        #calculate time span

    def add_car(self, c): #will accept the new car
        self.__car_list.append(c)  #appending the c into the car list array
        print c.type


    def compile_cars(self):
        output = ''
        # for loop to cycle through the array
        for car in self.__car_list:
            output += 'Car: ' + car.type + 'Built: ' + str(car.year) + 'Manufacture: ' + car.manufactor + '<br />'
        return output


    def calc_time(self):
        years = []
        for car in self.__car_list:
            years.append(car.year)

        years.sort() # sorting the dates high to low

        num = len(years) - 1
        span = years[num] - years[0] #last year minus the first year
        return 'The cars you entered span a total of ' + str(span) + ' years.' # now calc_time represents the number created here














class CarData(object):
    def __init__(self):
        self.type = ''
        self.__year = 0  # check for valid year
        self.manufactor = ''

    @property   #getter
    def year(self):  #write only
        return self.__year  #this will put it into the compiler

    @year.setter   #setter
    def year(self, y):  #recieving the year
        if y > 2014:  #if date is not valid
            print "Error, invalid date entered"
        else:
            self.__year = y  #printed if the date is validated
