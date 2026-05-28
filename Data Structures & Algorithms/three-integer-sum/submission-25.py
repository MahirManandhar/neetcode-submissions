class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result= []
        sorted_nums = sorted(nums)
        for i in range(len(sorted_nums)):
            if i>0 and sorted_nums[i] == sorted_nums[i-1]:
                continue
            j = i+1
            k = len(sorted_nums)-1
            while j<k:
                total = sorted_nums[j] + sorted_nums[k] + sorted_nums[i]
                if total == 0:
                    result.append([sorted_nums[i],sorted_nums[j],sorted_nums[k]])
                    j+=1
                    k-=1
                    while j<k and sorted_nums[j]==sorted_nums[j-1]:
                        j+=1
                    while j<k and sorted_nums[k]==sorted_nums[k+1]:
                        k-=1
                elif total < 0:
                    j+=1
                else:
                    k-=1
        return result