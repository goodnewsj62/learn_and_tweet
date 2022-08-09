from email.policy import default
import json


class Car:
    def __init__(self,model,color,speed) -> None:
        self.model = model
        self.color = color
        self.speed = speed

def serialize(obj):
    output = {"class_name": type(obj).__name__}
    output.update(**obj.__dict__)
    return output


car_a = Car("X801-5","red","30000km/hr")

result = json.dumps(car_a,default= serialize)
print(result)
# RESULT: {"class_name": "Car", "model": "X801-5", "color": "red", "speed": "30000km/hr"}

def deserialize(dict_obj):
    class_name =dict_obj.pop("class_name", None)
    if class_name:
        class_ = globals().get(class_name)
        instance =class_.__new__(class_) # Make an instance without calling __init__
        for key, value in dict_obj.items():
            setattr(instance, key,value)
        return instance
    return

result = json.loads(result, object_hook=deserialize)
print(result)
print(result.color)
# RESULT: <__main__.Car object at 0x7f31be016d30>
# RESULT: red


