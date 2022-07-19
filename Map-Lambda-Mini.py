
# Lambda program

x = lambda a,b,c,x: (a*(x ** 2))+(b*x)+ c

print("The output of the equation is : ",x(1,1,1,1))

# Map program

list1 = ["Alaska", "Alabama", "Arizona", "Arkansas", "Colorado", "Montana", "Nevada"]

list2 = list(map(lambda x: x.lower().count("a"), list1))

print("number of time 'A' and 'a' occured is : ",list2)
