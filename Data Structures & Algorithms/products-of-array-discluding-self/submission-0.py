import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            val = nums[:i] + nums[i+1:]
            result.append(math.prod(val))
        return result
            
