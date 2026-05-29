class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        heights.append(0)
        for h in range(len(heights)):
            while stack and heights[stack[-1]] > heights[h]:
                height = heights[stack.pop()]
                width = h if not stack else h - stack[-1] -1
                max_area = max(max_area, height*width)
            stack.append(h)
        return max_area