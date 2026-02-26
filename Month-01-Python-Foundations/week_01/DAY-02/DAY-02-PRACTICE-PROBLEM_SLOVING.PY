# ARRAY
# two sum problem
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.


def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    seen = {}
    for i,num in enumerate(nums):
        remain = target - num
        if remain in seen:
            return (seen[remain],i)
        seen[num]=i

print(twoSum([2,7,11,15],9))   


# Encapsulation of helper functions

def process_data(data):
    def clean_data():
        return [item.strip() for item in data] 
    return clean_data()
print(process_data(["  Python  ", "  Inner Function  "]))

# Remove Duplicates from Sorted Array


# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.
# Consider the number of unique elements in nums to be k​​​​​​​​​​​​​​. After removing duplicates, return the number of unique elements k.
# The first k elements of nums should contain the unique numbers in sorted order. The remaining elements beyond index k - 1 can be ignored.


# Input: nums = [1,1,2]
# Output: 2, nums = [1,2,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.


def removeDuplicates(nums):
    k=1
    for i in range(1,len(nums)):
        if nums[i]!=nums[i-1]:
            nums[k] = nums[i]
            k+=1
    return k,nums

print(removeDuplicates([1,1,2]))