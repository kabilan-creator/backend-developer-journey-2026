
# Closure With Modification
from unicodedata import digit


def counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment
counter1 = counter()
print(counter1())  # Output: 1
print(counter1())  # Output: 2
counter2 = counter()
print(counter2())  # Output: 1
print(counter1())  # Output: 3    


#Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

# Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

# Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
# Return k.

k = 0

def removeElement(nums, val):
    global k
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    return k, nums

result = removeElement([3, 2, 2, 3], 3)
print(result)  # Output: (2, [2, 2, 2, 3])

# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
# insert search
def insertsearch(nums,target):
    for i in range(len(nums)):
        if nums[i]>=target:
            return i
    return len(nums)

print(insertsearch([1,3,5,6],5))  # Output: 2


class solution:
    
    def oneplus(self,digit):
        for i in range(len(digit)-1,-1,-1):
            if digit[i]<9:
                digit[i]+=1
                return digit
            digit[i]=0
        return [1]+digit
sol = solution()
print(sol.oneplus([1,2,3])) # Output: [1, 2, 4]