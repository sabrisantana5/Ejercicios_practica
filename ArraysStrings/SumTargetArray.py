#return indices of array which values add up to a specific
#number with dictionaries
def twoSum(nums, target):
        dict = {}
        valor = None
        
        for  i in range(len(nums)):
            dict[nums[i]] = i
            
        for  i in range(len(nums)):  
            temp = target - nums[i]
            if temp in dict and dict.get(temp) != i:
                return [i,dict.get(temp)]
nums = [2, 7, 11, 15]
target = 9
res = []
res = twoSum(nums,target)
for i in res:
    print(res[i])

"""     Brute Force
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if(nums[i] + nums[j] == target):
                    return i,j
 """