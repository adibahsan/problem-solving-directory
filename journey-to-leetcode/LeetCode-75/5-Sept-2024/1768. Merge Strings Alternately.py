class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len1 = len(word1)
        len2 = len(word2)
        out = ""


        i, j, k = 0, 0, 0

        min_len = min(len1, len2)

        for i in range(min_len):
            out += word1[j]
            out += word2[k]
            j+=1
            k+=1

        if len1 > len2:
            out += word1[j:]
        else:
            out += word2[k:]
        return out


# Create an instance of the Solution class
solution = Solution()

# Call the mergeAlternately function on the instance
# result = solution.mergeAlternately("abc", "def")
result = solution.mergeAlternately("a1111", "d")

# Print the result
print(result)
