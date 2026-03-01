#Decorator
import time
def decorator(func):
    def wrapper():
        start_time = time.time()
        result = func()
        end_time = time.time()
        print(f"Execution time: {end_time - start_time}")
        return result
    return wrapper
@decorator
def example_function():
    sum = 0
    product = 1
    for i in range(1000000):
        sum += i 
        product *= i 
        if product > 1e10:  # To prevent overflow
            product = 1 
    return sum, product
    
print(example_function())

#merge two sorted arrays 
#revesered two pointer approach
class Solution(object):
    def merge(self, nums1, m, nums2, n):

        p1 = m - 1
        p2 = n - 1
        p = m + n - 1

        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1
        return nums1
print(Solution().merge([1,2,3,0,0,0],3,[2,5,6],3))
    