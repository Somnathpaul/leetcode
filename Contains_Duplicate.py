from typing import List

def containsDuplicate(nums: List[int]) -> bool:
        a = set()
        for i in range(0,len(nums)):
            if nums[i] in a:
                return True

            a.add(nums[i])
            print("------")
            print(a)
                
        return False



print(containsDuplicate([1,2,4,3,10]))