'''
for every iteration we calculate the number2 and if this number2 already exists in the dictionary(hashMap) then we return values of indices using return [hashMap[number2], i]
If it does not exist in the dictionary then we store that value and its index in the our hashMap with (value, index) as key, value
So the next time if we find a number2 that exists in the hashMap we can easily find it.

***Time Complexity = O(n) and Space Complexity = O(n) ***
'''


def twoSum(nums, target):
    hashMap = {}
    for i in range(len(nums)):
        number2 = target - nums[i]
        if number2 in hashMap:
            return [hashMap[number2], i]
        else:
            hashMap[nums[i]] = i


'''
brute force approach
O(n^2) complexity
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in nums:
            for j in range(len(nums)):
                if i + nums[j] == target and nums.index(i) != j:
                    return [nums.index(i),j]
                    
            

# Or

def twoSums(nums,target):
    for i in range(len(nums)): #1
        for j in range(i+1,len(nums)):  #2
            if nums[i] + nums[j] == target:  #3
                return [i,j]  #4

            
