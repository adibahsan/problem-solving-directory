#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        num_len = len(nums)
        out_set = set()
        nums.sort()

        i=r=l=0

        while i < num_len - 2:
            target = 0 - nums[i]
            l = i+1
            r = num_len-1

            while l<r:
                temp = nums[l] + nums[r]

                if temp == target:
                    out_set.add(tuple([nums[i], nums[l], nums[r]]))
                    r-=1
                    l+=1
                elif temp > target:
                    r-=1
                else:
                    l+=1
            i+=1
        
        out = map(list, out_set)

        return out
        
# @lc code=end

