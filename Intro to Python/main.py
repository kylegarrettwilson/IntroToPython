print "Hello World"

first_name = "Kermit"
last_name = "piggy"
print first_name

#response = raw_input("Enter your name  ")
#print "Hello there, ", response

birth_year = 1989
current_year = 2015
age = current_year - birth_year
#print "you are " + str(age) + " years old"


budget = raw_input()

if budget > 100:
    brand = "nike"
    print "Yay" + brand + "shoes!"
elif budget > 70:
    print "we can get some generics"
else:
    print "No cool shoes for you"


characters = ["chuck", "luke", "sam", "noi"]
characters.append("kyle")
print characters

movies = dict()   #dictionary object
movies = {"star wars":"darth vader", "silence of the lambs":"hannibal lecter"}
print movies["star wars"]  # will print darth vader


i = 0
while i<9:
    print "the count is", i
    i = i+1


for i in range(0,10):
    print "the count is", i
    i = i+1



rappers = ["MGK", "Biggie", "Nas"]
for r in rappers:
    print r







def calcArea(h, w):
    area = h * w
    return area

a = calcArea(20, 40)
print a








weight = 200
height = 68
message = '''
your height is {height} and your weight is {weight}
'''
message = message.format(**locals())
print message













