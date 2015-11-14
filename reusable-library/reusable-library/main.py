'''
Kyle Wilson
Project reusable library
11-11-15
'''

import cgi
from google.appengine.api import users
import webapp2
from library import CarData, FavoriteCars  #importing both classes
from result_page import ResultsPage, FormPage



class MainHandler(webapp2.RequestHandler):  #make this user input using a form
    def get(self):
        self.response.write(FormPage)

class Guestbook(webapp2.RequestHandler):
    def post(self):


        p = ResultsPage()
        lib = FavoriteCars()   # lib is the instance


        cd1 = CarData()       # first instance
        cd1.type = self.response.write(cgi.escape(self.request.get('type')))
        cd1.year = self.response.write(cgi.escape(self.request.get('year')))
        cd1.manufactor = self.response.write(cgi.escape(self.request.get('manufactor')))
        lib.add_car(cd1)    #adding to the library

        cd2 = CarData()       # second instance
        cd2.type = self.response.write(cgi.escape(self.request.get('type')))
        cd2.year = self.response.write(cgi.escape(self.request.get('year')))
        cd2.manufactor = self.response.write(cgi.escape(self.request.get('manufactor')))
        lib.add_car(cd2)    #adding to the library






        p.body = lib.compile_cars() + lib.calc_time()
        self.response.write(p.print_out()) #prints the big string



app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/sign', Guestbook),
], debug=True)
