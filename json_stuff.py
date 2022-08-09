import json
from collections import OrderedDict

jobj = {"a":"almond","b":"bicycle"}
s = json.dumps(jobj)


# here the OrderDict objects will be passed in a list of tuple [("key","value"),]
# and instead of a normal dict object an ordereddict object is obtained 
result = json.loads(s,object_pairs_hook=OrderedDict)
print(result)
#RESULT: OrderedDict([('a', 'almond'), ('b', 'bicycle')])

class MyJson:
    def __init__(self,dict_object) -> None:
        self.__dict__ = dict_object


# here MyJson ill be passed the jobj loaded dict back like so {"a":"almond","b":"bicycle"}
# i have then used the dictionary to set the __dict__ dunder method making MyJson object
# have a attributes a and b

result = json.loads(s,object_hook=MyJson)
print(result)
print(result.a)
#RESULT: <__main__.MyJson object at 0x7fa138e88be0>
#RESULT: almond
