nums = [2,7,11,15,5]
target = 20
def twoSum(nums,target):
    hash_map={}
    for i,num in enumerate(nums):
        if target - num in hash_map:
            return [hash_map[target-num],i]
        print(hash_map)
        hash_map[num]=i
    return[]
print(twoSum(nums,target))   
