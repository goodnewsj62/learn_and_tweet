def get_unique_items(items, key=None):
    seen = set() #stores unique values

    if key is not None and not callable(key):
        #to check if key passed is a function
        raise ValueError("key has to be a function")
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)
            
list(get_unique_items([1,2,1,4,5,8,5]))
#>>>[1,2,4,5,8]

list_of_dict = [{"foo":1},{"foo":2},{"foo":1}]
list(get_unique_items(list_of_dict, key=lambda x: x["foo"]))
#>>>[{"foo":1},{"foo":2}]
