# dictionary:*** keyvalue pair , unordered, mutable
mydict: dict={"Name":"Hassan","Age":18,"City":"Faisalabad"}
print(mydict)
# ----------------------------------------
# method 2

mydict2=dict(Name="Hassan",Age=18,City="Faisalabad")
print(mydict2)

# -----------------------------------------'
# identify specific value
value= mydict2["Name"]
print(value)

# -----------------------------------------
# pushing value in dictionary mydict2
mydict2["email"]="hassan@gmail.com"
print(mydict2)
# -----------------------------------------
# deleting value in dictionary mydict2
del mydict2["Name"]
print(mydict2)
# we can use another method pop to remove
mydict2.pop("Age")
print(mydict2)
# popitem to remove last key value
mydict2.popitem()
print(mydict2)



# write a program to del location a value to a dictionary 

dataDict: dict = {"company":"devloop", "value":"100M","employees":"300","location":"ISB"}
inputValue="location"
if inputValue in dataDict:
    del dataDict["location"]
else:
    print(f"Nothing found like {inputValue}"  )  


# ----------------------------------------------------------------
# loop ojn dictionary we can print key value and pair values
mydict3: dict={"Name":"Hassan","Age":18,"City":"Faisalabad"}

for key in  mydict3.keys(): # will print key only
    print(key)
for value in mydict3.values(): # will print value only
    print(value)
for key,value in mydict3.items(): # will print key,value
    print(key,value);
# ----------------------------------------------------------------
# coping a dictionary
copied_dict= mydict3 # if do somethin witH COPIED  dict it will modified the original dictionary
# so we can use ,copy fuction to copy the original dictionary
print(copied_dict)

copied_dict2=mydict3.copy()
copied_dict2["class"]=12
print(mydict3)
print(copied_dict2)


#----------------------------------------------------------------
# update the dictionary
dataSet1={"name": "john", "age":"16","class":"10"}
dataSet2={"name": "john", "age":"20","email":"john@example.com"}

dataSet1.update(dataSet2)
print(dataSet1)