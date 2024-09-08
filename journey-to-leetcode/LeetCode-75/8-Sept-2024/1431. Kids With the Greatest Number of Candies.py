from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_kid = max(candies)
        out = []
        for i in candies:
            if i + extraCandies >= max_kid :
                out.append(True)
            else:
                out.append(False)

        return out

solution =  Solution()

print(solution.kidsWithCandies([2,3,5,1,3], 3))
