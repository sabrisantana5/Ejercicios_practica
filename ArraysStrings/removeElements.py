class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        counter = 0
        j = 0
        for x in range(len(nums)):
            print(nums)
            if(nums[j]==val):
                counter += 1
                print(nums[j])
                for i in range(j,len(nums)-1):
                    temp = ""
                    temp = nums[i]
                    nums[i]=nums[i+1]
                    nums[i+1] = temp
                    i += 1
            else:
                j += 1
        return len(nums) - counter
    
        
'''class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        for x in nums:
            if(val == x):
                count+=1
        for x in range(count):
            nums.remove(val)
        return len(nums)
'''