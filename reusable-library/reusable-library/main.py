'''
Kyle Wilson
Project reusable library
11-11-15
'''



import webapp2
from form_page import FormPage
from library import CarData, FavoriteCars  #importing both classes
from result_page import ResultsPage


class MainHandler(webapp2.RequestHandler):  #make this user input using a form
    def get(self):

        #two different page views
        #page for class

        p = ResultsPage()
        lib = FavoriteCars()   # lib is the instance
        form = FormPage
        f = self.request.GET['name']
        q = self.request.GET['year']
        r = self.request.GET['manufactor']


        cd1 = CarData()       # first instance
        cd1.type = f
        cd1.year = q
        cd1.manufactor = r
        lib.add_car(cd1)    #adding to the library

        cd2 = CarData()       # second instance
        cd2.type = f
        cd2.year = q
        cd2.manufactor = r
        lib.add_car(cd2)    #adding to the library



        p.body = lib.compile_cars() + lib.calc_time()
        self.response.write(p.print_out()) #prints the big string

















app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
