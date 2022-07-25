# in if-elif-else chain if python fins one test that passes, it skips the rest of the tests
# beneficial for one specific condition
# using if statements makes sense to use when more than one condition could be True
# and when you want to act on every condition that is True.

requested_toppings = ['mushrooms', 'extra cheese', 'green peppers']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings: # another if statement so the test can run whether its true or false.
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished making your pizza!")



# USING A LOOP TO ANNOUNCE EACH TOPPING AS ITS ADDED TO THE PIZZA
print("\n\t\t********** Using a loop **********")
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print("Adding " + requested_topping + ".")

print("\nFinished making your pizza!")



# USING MULTIPLE LISTS
print("\n\t\t********** Using Multiple Lists **********")
available_toppings = ['mushrooms','olives','green peppers',
                      'pepperoni','pineapple','extra cheese']

requested_toppings = ['mushrooms','french fries','extra cheese']

for requested_topping in requested_toppings: # we loop through the list of requested toppings.
    if requested_topping in available_toppings: # check if each requested topping is in the list of available toppings.
        print("Adding " + requested_topping + ".")
    else: # If it is not on the list of available toppings the else block runs
        print("Sorry, we dont have " + requested_topping + ".")

print("\nFinished making your pizza!")