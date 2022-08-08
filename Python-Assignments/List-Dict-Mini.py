#1.	Return all the duplicate values from list of arraylist


from collections import Counter

l1 = [[1,1,3,2],[9,8,8,1],[0,4,5,0,0,1,4]]

l2=[]

lengthofl1 = len(l1)

for r in range(lengthofl1):
    l2=l1[r]
    counts = dict(Counter(l2))
    duplicates = {key:value for key, value in counts.items() if value > 1}
    print("Duplicate Element : Count--> ",duplicates)

print("\n")


#2.	Merge two lists as shown below

list1 = ["Hello", "take"]

list2 = ["Dear", "sir"]

list3 = []

for str1 in list1:
    word1 = str1
    
    for str2 in list2:

        word2= str2

        word3 = str1 + " " + str2 
        list3.append(word3)


print ("New list : ",list3)

print("\n")


#3.	 Given a nested list extend it by adding the sub list ["h", "i", "j"] 

list4 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
sublist=["h", "i", "j"]


for str4 in sublist:
    list4[2][1][2].append(str4)

print("Merged list : ", list4)

print("\n")

#4.	Map the dictionary in the following manner

list5 = ['Ten', 'Twenty', 'Thirty']
list6 = [10, 20, 30]

dict_map = dict(zip(list5, list6))
print("New Dict is : ", dict_map)

print("\n")


#5.	 Merge following two Python dictionaries into one

dict_1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict_2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

dict_3 = {**dict_1, **dict_2}
print("Merged Dict is : ", dict_3)

print("\n")

#6.	 Rename key city to location in the following dictionary

dict_4 = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}

dict_4['location'] = dict_4.pop('city')
print("Updated Keys are : ",dict_4.keys())

print("\n")

#7.	Convert Dictionary to list

dict_5= {'HuEx': [1, 3, 4], 'is': [7, 6], 'best': [4, 5]}
  
list5 = []
for key, val in dict_5.items():
    list5.append([key] + val)
  
print("New List from Dict is :" + str(list5))






    
