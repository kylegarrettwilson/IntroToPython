parlor_name = raw_input("Enter a proper noun (restaurant) ")

food_name = raw_input("Enter a noun (food) ")

action_name = raw_input("Run or jump? ")

toppings_count = raw_input("Enter a number ")

free_count = int(raw_input("Enter a number "))

customer_count = raw_input("Enter a number ")


print "Hello and welcome to ", parlor_name


if toppings_count <= 5:
    supply = "ALL"
    print "You get " + supply + " the topping you want!"
else:
    print "You don't get any toppings"


if free_count > 80:
    returning = "FREQUENT"
    print "You are a " + returning + " customer so your pizza is free!"
else:
    print "You must be new around here, give us a good tip."


def pizzaCount(x, y):
    coupon = x - y
    return coupon

a = pizzaCount(free_count, 30)
print "You get " + str(a) + " free pizza coupons!"


toppings = ["olives" , "cheese", "bacon"]
toppings.append(food_name)
print "The toppings we have available are ", toppings


verb = dict()
verb = {"run":"jump", "jump":"run"}
print "We love to " + verb[action_name] + " over your pizza!"











