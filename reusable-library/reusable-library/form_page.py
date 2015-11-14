class FormPage(object):
    def __init__(self):
        self.__title = "Welcome"
        self.css = "css/styles.css"
        self.__head = """
<!DOCTYPE HTML>
<html>
    <head>
    <title></title>


    </head>
    <body>"""


        self.body = """<form name="search" action="/reusable-library/main.py" method="post">
            <label>Car Name: </label><input type="text" name="name" /><br>
            <label>Year: </label><input type="text" name="year" /><br>
            <label>Manufacture: </label><input type="text" name="manufactor" /><br>
            <input type="submit" value="Submit" /></form>"""

        self.__error = ''
        self.__close = """

    </body>
</html>
        """

        def print_out(self):
            all = self.__head + self.body + self.__error + self.__close
            return all
