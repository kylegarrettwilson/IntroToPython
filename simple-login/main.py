
import webapp2   # using web app as a browser

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')





#dont touch this
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
