#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        c = set(nums)
        out = 0
        for i in nums:
           count = 0
           if i -1 not in c:
               while i + count in c:
                   count +=1
                   out = max(out, count)       
        return out
        
# @lc code=end

