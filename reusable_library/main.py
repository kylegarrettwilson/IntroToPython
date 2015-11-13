'''
Kyle Wilson
Project reusable library
11-11-15
'''



import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
       











app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
