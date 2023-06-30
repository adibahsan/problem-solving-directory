#
# @lc app=leetcode id=438 lang=python3
#
# [438] Find All Anagrams in a String
#

# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        r=l=i=0
        counter=tracker=0
        s_len = len(s)
        p_len = len(p)
        out = []
        s_tracker, p_tracker = {}, {}

        if s_len < p_len:
            return out

        while i < p_len:
            c = p[i]
            p_tracker[c] = p_tracker.get(c, 0) + 1
            i +=1
        
        counter = len(p_tracker)

        while r<p_len:
            c = s[r]
            s_tracker[c] = s_tracker.get(c,0) + 1
            if c in p_tracker and s_tracker[c] == p_tracker[c]:
                tracker+=1
            if counter == tracker:
                out.append(r-p_len+1) 
            r+=1
    
        while r < s_len: 

            # print(counter, tracker, "r&l", r, l)
            d = s[r-p_len]
            s_tracker[d] -=1

            if d in p_tracker and s_tracker[d] < p_tracker[d]:
                tracker -=1

            c = s[r]
            s_tracker[c] = s_tracker.get(c,0) +1 
            if c in p_tracker and s_tracker[c] == p_tracker[c]:
                tracker+=1
            # print(counter, tracker)

            if counter == tracker:
                out.append(r-p_len+1)
            
            r+=1

        return out 


solve = Solution()

out = solve.findAnagrams("aasaa","aa")

print("Output ", out)
        
# @lc code=end

