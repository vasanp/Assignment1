# Convert a number to positive if it's negative in the list

list1=[-1000, 500, -600, 700, 5000, -90000, -17500]

list2= list(filter(lambda x: True if x>0 else False, map(lambda x: x*-1, list1)))

print("New list with coverted values : ",list2)

#Using zip and dict functions create a dictionary

list3=["Netflix", "Hulu", "Sling", "Hbo"]
list4=[198, 166, 237, 125]


result= dict(zip(list3,list4))

print("Final Key-Valu Pair : ",result)


# Program using reduce function

from functools import reduce

list5=[9,6,5,5,4]

def multiply(x, y):
    return x * y

result1 = reduce(multiply, list5)

print("Final Result : ",result1)
