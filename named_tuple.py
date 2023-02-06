# assuming you have an orm class which you created a method which
# returns more than a value like so

class SomeDbORM:
    username =  "fridaw"
    user_type = "hey"
    profile =  object()

    def get_user(self):
        return  self.profile, self.user_type

# you could accessing the result of get_user like so
db_helper =  SomeDbORM()
profile = db_helper.get_user()[0]
user_type =  db_helper.get_user()[1]
print(profile, user_type)
#RESULT:  <object object at 0x7efda9d5dd70> hey

# OR you could destructure like so
profile, user_type =  db_helper.get_user()

# but what if tomorrow you changed the get_user function to return an extra
# caculated attribute for instance, then you have to change your code if you've
# distructured like the above plus accessing by index could also affect code readability

# Using a recipe that utilize the property decorator and namedtuple
# could improve this code with little overhead like so

from collections import namedtuple

UserInfo =  namedtuple("UserInfo",["profile", "user_type"])

class SomeDbORM:
    username =  "fridaw"
    user_type = "hey"
    profile =  object()

    @property
    def user_(self):
        return  UserInfo(self.profile, self.user_type)

# you can then do this which seem more elegant
db_helper =  SomeDbORM()
print(db_helper.user_.profile, db_helper.user_type)
#RESULT: <object object at 0x7efda9d5dd80> hey