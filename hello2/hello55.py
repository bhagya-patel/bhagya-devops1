#note down
# sets are mutable
# but in the sets element are immutable

collection = set()
collection.add(1)
collection.add(2)
collection.add("bhagya ")
collection.add((1,2,3))
collection.add(3)

collection.remove(3)
print(collection)

collection.pop()    #delete any random
print(collection)

collection.clear()
print(collection)