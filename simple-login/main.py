'''
Kyle Wilson
11/9/15
Design Patterns
Simple Form Login
'''





import webapp2   # using web app as a browser

class MainHandler(webapp2.RequestHandler):
    def get(self):
        page_head = '''<!DOCTYPE HTML>
<html>
    <head>
    <title>Login!</title>
    </head>
    <body>'''





        page_body = '''<form method="GET">
            <label>First Name: </label><input type="text" name="first" />
            <label>Last Name: </label><input type="text" name="last" />
            <label>Email: </label><input type="text" name="email" />
            <input type="submit: value="Submit" />'''

        page_close = '''
        </form>
    </body>
</html>'''
        if self.request.GET:  #if get does exist then print the material
            first = self.request.GET['first']    #This is storing form info within a variable and then send it out
            last = self.request.GET['last']       #This is storing form info within a variable and then send it out
            email = self.request.GET['email']    #This is storing form info within a variable and then send it out
            self.response.write(page_head + user + ' ' + email + page_body + page_close)
        else:
            self.response.write(page_head + page_body + page_close)              #this prints info onto the page, this is publish





#dont touch this
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
