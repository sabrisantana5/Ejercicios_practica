'''Find the disappeared numbers within the sequence
in the array of integers (starts in 1, finishes in 'n'),
numbers can be repeated '''
def findNumbers(nums):
        dict = {}
        answer = []
        maxim = 0
        for c in nums:
            if c not in dict:
                dict[c] = 0
                if(c>maxim):
                    maxim = c
        for c in range(1,maxim):
            if c not in dict:
                answer.append(c)
        return answer
        
nums = [4,6,2,6,7,2,1]
print(findNumbers(nums))
#[3,5]