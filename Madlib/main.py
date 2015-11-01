parlor_name = raw_input("Enter a proper noun (restaurant) ")

food_name = raw_input("Enter a noun (food) ")

tossed_name = raw_input("Enter a verb ")

toppings_count = raw_input("Enter a number ")

free_count = raw_input("Enter a number ")

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


def pizza_count(x, y):
    coupon = x - y
    return coupon

a = pizza_count(free_count, 4)
print "You get " + str(a) + " free pizza coupons!"







