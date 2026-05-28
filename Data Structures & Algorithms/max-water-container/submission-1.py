class Solution:
    def maxArea(self, heights: List[int]) -> int:
        largest = 0
        for i in range(len(heights)):
            j = i+1
            while j<len(heights):
                area = min(heights[i],heights[j])*(j-i)
                j+=1
                largest = max(largest, area)
        return largest

        