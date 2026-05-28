class Solution:
    def maxArea(self, heights: List[int]) -> int:
        largest = 0
        left = 0
        right = len(heights) - 1
        while left<right:
            height = min(heights[left],heights[right])
            width = right-left
            largest = max(largest,width*height)

            if heights[left]<heights[right]:
                left+=1
            else:
                right-=1
        return largest

        