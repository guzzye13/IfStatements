# The if-elif chain
# When needed to test more than two possible situations
age = 18
if age < 4: # if the test passes, an appropriate message is printed
    price = 0
elif age < 18: # another if test, runs only if the previous test failed
    price = 5
elif age < 65:
    price = 10
elif age > 65:
    price = 2

print("Your admission cost is $" + str(price) + ".") # can only concatenate str not int
