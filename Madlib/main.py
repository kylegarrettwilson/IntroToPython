'''
The first thing I want to do is gather all of the info from the user and then run that input
through various calculations in order to print out the madlib at the end.

I am going to use raw_input to prompt the user to enter a number or string

Then I am going to do a simple print and the parlor name to start off the madlib

After that I am using two if else statements to determine what the next lines of the madlib will be.
As you can see, I used conditional statements working with numbers entered by the user to
calculate the next two lines.

I then did a definition function to calculate what the next print line will be

After that I did an array which starts out with three toppings and then adds the string the user entered
at the beginning by using a .append method

Then I did a dictionary which took the key from what the user entered and printed out the value
for the specific key

Finally I did a while loop to loop through how many customers there has been that day
including the user
'''



parlor_name = raw_input("Enter a proper noun (restaurant) ")    #This is using a raw input to prompt the user for an input

food_name = raw_input("Enter a noun (food) ")  # This one asks for a string

action_name = raw_input("Run or jump? ")   # This one asks for a string

toppings_count = raw_input("Enter a number ")  # This one asks for a number

free_count = int(raw_input("Enter a number "))   # This one asks for a number

customer_count = int(raw_input("Enter a number "))   # This one asks for a number


print "Hello and welcome to ", parlor_name   # This is a simple print of the parlor name entered above to start the madlib


if toppings_count <= 5:    # This is an if else statement. If the user entered 5 or less then it prints the first line
    supply = "ALL"   # This is a fun way to inject a value into the print function
    print "You get " + supply + " the topping you want!"
else:
    print "You don't get any toppings"  # This is the result if the user entered more then a 5


if free_count > 80:   # This is another conditional statement that uses the free_count from above. If user enters anything greater then 80 then it prints the first line
    returning = "FREQUENT"
    print "You are a " + returning + " customer so your pizza is free!"
else:
    print "You must be new around here, give us a good tip." # this is what will print if the user enters anything less than 80


def pizzaCount(x, y):  # I love these! This is a definition which basically takes two input and does a little math with them
    coupon = x - y  # this is the free_count (x) minus the 30 (y).
    return coupon  # return the coupon result from above to use down below

a = pizzaCount(free_count, 30)  # This is the input for the definition and I put it in a variable so I can call that in the print below
print "You get " + str(a) + " free pizza coupons!" # The variable a will be an integer so it must be converted to a string for this print to work


toppings = ["olives" , "cheese", "bacon"]  # This is an array that holds three values
toppings.append(food_name)  #This is adding one more to the array above by inputing what the user typed at the beginning
print "The toppings we have available are ", toppings  # This then prints the string and the array together


verb = dict()   # this is a definition. It will print a value based on the key inputted by the user
verb = {"run":"jump", "jump":"run"}  # the two keys the user could have input was run or jump, I then flip flopped the values for each
print "We love to " + verb[action_name] + " over your pizza!"   #This is what determines the value that will be printed by using the verb[action_name] call from the users input above



i = customer_count # this is a while loop that is making i the quantity of the users input from above
while i<10:   # while i is less then 10
    print "You are the " + str(i) + " customer of the day!"  #print this but string the i number
    i = i+1 # then add one to the last i number












