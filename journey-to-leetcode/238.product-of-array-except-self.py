#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = []
        l = len(nums)
        prefix = 1

        for i in range(l):
            out.append(prefix)
            prefix *= nums[i]
        
        postFix = 1
        i = l -1
        while  i>= 0:
            # print(postFix, out[i])
            out[i] *= postFix
            postFix *= nums[i]
            i-=1 

        # print(out)
        return out
        
        
        
# @lc code=end

