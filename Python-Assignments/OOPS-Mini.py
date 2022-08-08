from itertools import combinations
from collections import Counter

class StringClass:

    def __init__(self, name):
        self.name = name

    def strlength(self):
        print("Length of string is: ", len(self.name))

    def listofchr(self):
        return list(self.name)

str1 = "748270"

obj1 = StringClass(str1)

obj1.strlength()

listchr = obj1.listofchr()

print("List of characters : ", listchr)


class PairsPossible(StringClass):

    def __init__(self, name):
        StringClass.__init__(self, name)

    def storingpair(self):

        spair = list (combinations (listchr, 2))

        print("Possiblel Pairs are : ", spair)

    def listofchr2(self):
        return list(self.name)

str2="20083782"

obj2 = PairsPossible(str2)
obj2.storingpair()


class SearchCommonElements(PairsPossible):

    def __init__(self, name):
        PairsPossible.__init__(self, name)

    def commonelements(self):
        
        dict1 = Counter(str1)
        dict2 = Counter(str2)
 
        commonDict = dict1 & dict2

        if len(commonDict) == 0:
            print (-1)
            return
 
        commonChars = list(commonDict.elements()) 

        print ("Common Elements are : ",commonChars)
        


obj3 = SearchCommonElements("96554")

obj3.commonelements()


class EqualSumPairs(SearchCommonElements):
    
        def __init__(self, name):
            SearchCommonElements.__init__(self, name)

        def countofpairs(self):
            spair = list (combinations (listchr, 2))
            return(len(spair))

obj4 = EqualSumPairs("4413")
print ("Number of pairs formed in class PairsPossible : ", obj4.countofpairs())
        
    

    
