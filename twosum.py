from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    x = {}

    for count, item in enumerate(nums):
        diff = target - item
        if diff in x:
            return [x[diff], count]

        x[item] = count


# test
num = 9
a = [2,-7,11,15]
print(twoSum(a,num))


    
