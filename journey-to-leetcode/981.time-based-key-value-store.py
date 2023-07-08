#
# @lc app=leetcode id=981 lang=python3
#
# [981] Time Based Key-Value Store
#

# @lc code=start
class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        curr_val =  self.store[key]
        # print(curr_val, timestamp, key)
        l,r = 0, len(curr_val) - 1
        out = ""
        while (l <=r):
            m = (l+r) //2
            ts =  curr_val[m][1]
            if ts <= timestamp:
                out = curr_val[m][0]
                l = m+1
            else:
                r = m-1
        
        return out
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
# @lc code=end

