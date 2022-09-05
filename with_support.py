
class SomeResource:
    def open(self):
        print("opened up.....")
    def close(self):
        print("closingup conection....")

class MyClass:
    def __init__(self):
        self.some_resource =  None

    def __enter__(self):
        if self.some_resource:
            raise RuntimeError("resource already open")
            
        self.some_resource =  SomeResource()
        self.some_resource.open()
        return self.some_resource
    
    def __exit__(self,exception_type, exception_val, traceback):
        self.some_resource.close()
        self.some_resource = None
        

foo_resource = MyClass()

with foo_resource as f:
    print(f"perform some stuff with {f}")

#RESULT:
# opened up.....
# perform some stuff with <__main__.SomeResource object at 0x7fa07ae2dbe0>
# closingup conection....