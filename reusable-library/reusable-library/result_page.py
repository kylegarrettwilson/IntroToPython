FormPage = """
<!DOCTYPE HTML>
<html>
    <head>
    </head>
    <body>
        <form action="/sign" method="post">
            <label>Car Name: </label><input type="text" name="type" /><br>
            <label>Year: </label><input type="text" name="year" /><br>
            <label>Manufactor: </label><input type="text" name="manufactor" /><br>
            <div><input type="submit" value="sign guestbook"></div>
        </form>
    </body>
</html>
"""






class ResultsPage(object):
    def __init__(self):
        self.__title = "Welcome"
        self.css = "css/styles.css"
        self.__head = """
<!DOCTYPE HTML>
<html>
    <head>
        <title>Enter your information</title>
        <link href="css/styles.css" rel="stylesheet" type="text/css" />
    </head>
    <body>
        """

        self.body = ""
        self.__error = ''
        self.__close = """
    </body>
</html>
        """

    def print_out(self):
        all = self.__head + self.body + self.__error + self.__close
        return all










