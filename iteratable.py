class ReverseIterator:
    def __init__(self) -> None:
        self._items = [] 

    def append_item(self, item):
        self._items.append(item)
    
    def __iter__(self):
        return self

    def __next__(self):
        if len(self._items) != 0:
            return self._items.pop()
        else:
            raise StopIteration

iteratable_obj = ReverseIterator()
iteratable_obj.append_item(1)
iteratable_obj.append_item("oshey")
iteratable_obj.append_item(lambda x: x)
iteratable_obj.append_item({1,2,3})

for item in iteratable_obj:
    print(item)
#result:
# {1, 2, 3}
# <function <lambda> at 0x7f891ef5f280>
# oshey
# 1