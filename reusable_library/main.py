'''
Kyle Wilson
Project reusable library
11-11-15
'''



import webapp2
from library import CarData

class MainHandler(webapp2.RequestHandler):
    def get(self):
        cd1 = CarData()
        cd1.type = "mustang"
        cd1.year = 2008
        cd1.manufactor = "ford"














app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
