class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        l1, l2 = len(str1), len(str2) #6,4

        if l1<l2:
            str1, str2 = str2, str1
            l1, l2 = l2, l1

        i = min(l1,l2) -1 # 3

        while i >= 0: # 3#2#1
            temp = i + 1 #2
            #print(i,temp, 'Temping', str1[:temp])
            if l1 % temp == 0 and l2 % temp == 0:
                s1 = str2[:temp] * (l1 // temp) # AB * 3
                s2 = str2[:temp] * (l2 //temp) # AB * 2

                if s1 == str1 and s2 == str2:
                    return str2[:temp]

            i -= 1

        return ""


solution = Solution()
print(solution.gcdOfStrings("ABCABC", "ABC"))
print(solution.gcdOfStrings("ABABAB", "ABAB"))
print(solution.gcdOfStrings("LEET", "CODE"))
