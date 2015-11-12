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

    <style>
        body{
        width: 100%;
        background-color: grey;
        }
        form{
        width: 200px;
        margin: 0 auto;
        text-align: center;
        padding: 15px;
        font-size: 2em;
        border: 2px solid white;
        background-color: black;
        color: white;



    </style>

    </head>
    <body>'''





        page_body = '''<form method="GET">
            <label>First Name: </label><input type="text" name="first" /><br>
            <label>Last Name: </label><input type="text" name="last" /><br>
            <label>Email: </label><input type="text" name="email" /><br>
            <input type="radio" name="gender" value="male" checked>Male
            <br>
            <input type="radio" name="gender" value="female">Female
            <br>
            <select name="eye">
                <option value="blue">Blue eyes</option>
                <option value="brown">Brown eyes</option>
                <option value="green">Green eyes</option>
            </select>
            <input type="submit" value="Submit" />'''

        page_close = '''
        </form>
    </body>
</html>'''
        if self.request.GET:  #if get does exist then print the material
            first = self.request.GET['first']    #This is storing form info within a variable and then sending it out
            last = self.request.GET['last']       #This is storing form info within a variable and then sending it out
            email = self.request.GET['email']    #This is storing form info within a variable and then sending it out
            check = self.request.GET['gender']   #This is storing form info within a variable and then sending it out
            select = self.request.GET['eye']     #This is storing form info within a variable and then sending it out
            self.response.write(page_head + first + ' ' + last + ' ' + email + ' ' + check + ' ' + select + ' ' + page_close)
        else:
            self.response.write(page_head + page_body + page_close)              #this prints info onto the page, this is publish





#dont touch this
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
