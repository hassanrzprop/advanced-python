# set is ordered , mutable and no repition
myset={1,2,3,1,2}
print(myset) # no repition

set1=set("hello")
print(set1) 

set2={}    # this will count empty dictionary
set3=set() # this will count empty set
set3.add(1)
set3.add(2)
set3.add(3)
set3.remove(3)
print(set3) 

# loop on sets 
for i in set3:
    print(i)
# if on sets
if 2 in set3:
    print("yes")

odds={1,3,5,7,9}
even={2,4,6,8}
prime={2,3,5,7,11}
# unions of odd even and prime
u= odds.union(even.union(prime))
print(u)

# intersection of odd and even
i= odds.intersection(even)
print(i)


setA={1,2,3,4,5,6,7,8,9}
setB={1,2,3,10,11,12}

#1)
diff= setA.difference(setB)    # means element which are not in set B {4,5,6,7,8,9}
print(diff)

# 2)
diff2=setB.symmetric_difference(setA) # means element of B which are not in set A and Elements of set A which are not in SET B {4,5,6,7,8,9,10,11,12}
print(diff2)

# # 3) 
# setA.update(setB)
# print(setA) # add all elements of both sets to A

# # 4)
# setA.intersection_update(setB)  # add number of elements to SET A which are common in both sets
# print(setA) 


# # 5)
# setA.difference_update(setB) 
# print(setA)

# 6)
setA.symmetric_difference_update(setB)    # add both diiferences of set a and set b will added to set a {2,3,4,5,6,7,8,9,10,11,12}
print(setA)