# supposed you have a list of dictionaries and you want to sort
# by a key... Naturally you follow this approach
my_list =  [
    {"name": "routebirds", "topic": "python", "duration":"1hr" },
    {"name": "justice", "topic": "java", "duration":"2hr" },
    {"name": "bob", "topic": "design patterns", "duration":"1hr" }
]

sorted_list =  sorted(my_list,  key=lambda x: x["name"])
print(sorted_list)
# RESULT: [{'name': 'bob', 'topic': 'design patterns', 'duration': '1hr'},
#  {'name': 'justice', 'topic': 'java', 'duration': '2hr'}, 
# {'name': 'routebirds', 'topic': 'python', 'duration': '1hr'}]

# but you could also use the itemgetter function from operator module
# which is a bit faster and better instead of lambda 
from operator import itemgetter

sorted_list =  sorted(my_list, key=itemgetter("name"))
print(sorted_list)

# you could also sort by two fields
my_list.append({"name": "bob", "topic": "affiliate marketting", "duration":"1hr" })
sorted_list =  sorted(my_list, key=itemgetter("name", "topic"))
print(sorted_list)
# RESULT: [{'name': 'bob', 'topic': 'affiliate marketting', 'duration': '1hr'}, 
# {'name': 'bob', 'topic': 'design patterns', 'duration': '1hr'}, 
# {'name': 'justice', 'topic': 'java', 'duration': '2hr'}, {'name': 'routebirds', 'topic': 'python', 'duration': '1hr'}]
