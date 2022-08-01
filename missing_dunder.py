
# You could subclass the python dict 
# and provide a missing dunder method that will cause the 
# dictonary to return a value when you try accessing a key that is not in the dictionary 

class Mdict(dict):
    def __missing__(self,key):
        return  "key: "+key


# demonstration
mydict = Mdict({"x":1,"y":2})
print(mydict["z"])
# RESULT:
# key: z



mydict = dict({"x":1,"y":2})
print(mydict["z"])
#RESULT:
# Original exception was:
# Traceback (most recent call last):
#   File "missing_dunder.py", line 13, in <module>
#     print(mydict["z"])
# KeyError: 'z'