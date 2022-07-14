# if you want to round a number in python you could
# use the round function 

# normal
some_float= 25.945
result = round(some_float, 2)

print("output: ",result)
# output: 25.95

#changing some_float to:
some_float =  25.935
result = round(some_float,2)

print("output: ", result)
# output: 25.93
# this is because 3 is an odd number, but 5 which is a middle number 
# is not rounded to turn 3 to 4  to clearify:

print("output: ", round(25.937, 2)) #output: 25.94

# it is also possible to add a negative num
print("output: ", round(12345, -1)) #ouput: 12340
# -1 rounds to the nearest tens, -2 hundred and so on

print("output: ", round(12345, -2)) #output: 12300