class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        
        if(len(set1)>len(set2)):
            return [i for i in set1 if i in set2]
                    
        else:
            return[i for i in set2 if i in set1]

