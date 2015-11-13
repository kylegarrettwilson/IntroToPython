'''
Kyle Wilson
Project reusable library
11-11-15
'''



import webapp2
from library import CarData, FavoriteCars  #importing both classes
from result_page import ResultsPage

class MainHandler(webapp2.RequestHandler):  #make this user input using a form
    def get(self):

        #two different page views
        #page for class

        p = ResultsPage()
        lib = FavoriteCars()   # lib is the instance


        cd1 = CarData()       # first instance
        cd1.type = "mustang"
        cd1.year = 2008
        cd1.manufactor = "ford"
        lib.addCar(cd1)    #adding to the library

        cd2 = CarData()       # second instance
        cd2.type = "batcar"
        cd2.year = 2003
        cd2.manufactor = "batman"
        lib.addCar(cd2)    #adding to the library


        p.body = lib.compileCars()
        self.response.write(p.print_out()) #prints the big string

















app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
