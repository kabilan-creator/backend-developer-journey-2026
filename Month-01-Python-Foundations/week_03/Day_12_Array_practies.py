# Array Practices

# Find the maximum element in an array

import collections


def find_maximum(arr):
    if not arr:
        return None  # Return None for an empty array
    
    max_element = arr[0]  # Initialize max_element with the first element of the array
    
    for num in arr:
        if num > max_element:
            max_element = num  # Update max_element if a larger number is found
            
    return max_element

#find the minimum element in an array

def find_minimum(arr):
    if not arr:
        return None  # Return None for an empty array
    
    min_element = arr[0]  # Initialize min_element with the first element of the array
    
    for num in arr:
        if num < min_element:
            min_element = num  # Update min_element if a smaller number is found
            
    return min_element

# find both maximum and minimum element in an array
def find_max_and_min(arr):
    if not arr:
        return None, None  # Return None for both max and min for an empty array
    
    max_element = arr[0]  # Initialize max_element with the first element of the array
    min_element = arr[0]  # Initialize min_element with the first element of the array
    
    for num in arr:
        if num > max_element:
            max_element = num  # Update max_element if a larger number is found
        elif num < min_element:
            min_element = num  # Update min_element if a smaller number is found
            
    return max_element, min_element

maximum = find_maximum([3, 1, 4, 1, 5, 9])  # Output: 9
print("Maximum:", maximum)

minimum = find_minimum([3, 1, 4, 1, 5, 9])  # Output: 1
print("Minimum:", minimum)

# find the largest element in a rotated sorted array

def find_max(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i+1]:
            return arr[i]
    
    return arr[-1] 


array = find_max([4,5,6,7,1,2,3])
print(array)

# Find the maximum difference between two elements (j > i)
def max_difference(arr):
   min_value = arr[0] 
   max_pro = 0 
   for x in arr:
       max_pro = max(max_pro, x - min_value)
       min_value = min(min_value, x)
   return max_pro

difference = max_difference([7, 1, 5, 3, 6, 4])  
print("Maximum Difference:", difference)

# Find the minimum element in a rotated sorted array

def find_min(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i+1]:
            return arr[i+1]
    
    return arr[0]
array = find_min([4,5,6,7,1,2,3])
print(array)

# Find max element in every subarray of size K

def max_in_subarrays(arr,k):
    if not arr or k <= 0:
        return []
    
    result = []
    dq = collections.deque()

    for i in range(len(arr)):
        if dq and dq[0] <= i - k:
            dq.popleft()

        while dq and arr[dq[-1]] < arr[i]:
            dq.pop()
        dq.append(i)
        if i >= k - 1:
            result.append(arr[dq[0]])
    return result
subarray_max = max_in_subarrays([1,3,-1,-3,5,3,6,7], 3)
print(subarray_max)
