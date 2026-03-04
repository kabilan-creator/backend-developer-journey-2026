class Solution(object):
    def maxArea(self, height):
        vert = 0
        left = 0
        right = len(height)-1
        max_area = 0
        while left<right:
            vert = min(height[left],height[right]) * (right-left)
            max_area = max(max_area,vert)
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return max_area
    
slo = Solution()
print(slo.maxArea([1,8,6,2,5,4,8,3,7]))
    
