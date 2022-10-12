from types import MethodType


class Foo:
    x = "cls attr"

    def som(self):
        pass


foo_obj = Foo()
print(foo_obj.som)
# RESULT: <bound method Foo.som of <__main__.Foo object at 0x7fdf0cbda070>>

# you find out that the function som of obj foo_obj is a bound method
# now say we just create a func outside the class


def myfunc(first_arg, x):
    print(type(first_arg), first_arg, x, first_arg.x)


# remember in python everything is an object...
# here i am accessing the get method of the non-data descriptor  of function myfunc

bound_method = myfunc.__get__(foo_obj)

print(bound_method)
bound_method("passed in")
# RESULT: <bound method myfunc of <__main__.Foo object at 0x7fdf0cbda070>>
# RESULT: <class '__main__.Foo'> <__main__.Foo object at 0x7fdf0cbda070> passed in cls attr
# from the result you can see the class variable x and the passed in variable
# the first argment is the object passed to the function

bound_mtd = MethodType(myfunc, foo_obj)
print(bound_mtd)
bound_mtd("passed in")
# you could also implement this using the types.MethodType
# <bound method myfunc of <__main__.Foo object at 0x7fdf0cbda070>>
# <class '__main__.Foo'> <__main__.Foo object at 0x7fdf0cbda070> passed in cls attr

# conclusion:
# to understand better i have droped links to resources and the python docs
# please share and follow for more
