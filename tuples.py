# TUPLES:   ordered , immutable, allows duplicate elements

# differance b/w list and tuple.Tuple is more efficient when working with large data sets
import sys
my_list=[1,2,3,"hassan","ali",True]
my_tuple=(1,2,3,"hassan","ali",True)
print(sys.getsizeof(my_list),"bytes")   #104bytes of size
print(sys.getsizeof(my_tuple),"bytes")  #88bytes of size (less than the size of the list good enough for ompimization with large data)

import timeit
print(timeit.timeit(stmt="[1,2,3,'hassan','ali',True]",number=10000000)) # take 1.415 seconds to make
print(timeit.timeit(stmt='(1,2,3,"hassan","ali",True)',number=10000000)) # take 0.36 seconds to make so more optimized

mytuple=("john","MAX",23,True,"hashmat","wick")
item=mytuple[1]
print(item)

halfList=mytuple[2:4]   # slicing include num  first count means item at 2 count will not be included but at 4 will be included
print(halfList)


names=("HASSAN",) #if we placed comma for single name in round brackets it will become tupe otherwise it will be str or single entity
typeOfNames=type(names)
print(typeOfNames)



# unpacking tuple
tuplee="waqar",18,"Gujrat"
name,age,city=tuplee
print(name)
print(age)
print(city)




# # write a program to check the duplication of the item 
nums = (10, 20, 30, 40, 50, 60, 60, 70, 80)
nums_list=list(nums)
unique_elements = []

duplicates=[]
for num in nums_list:
    if num in unique_elements:
        duplicates.append(num)
    else:
        unique_elements.append(num) 
print("UNIQUE ELEMENTS:",unique_elements)
print("DUPLICATE ELEMENTS:",duplicates)  