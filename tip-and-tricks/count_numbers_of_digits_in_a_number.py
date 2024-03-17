# Log based Python program to count number of
# digits in a number

# function to import ceil and log
import math


def countDigit(n):
    return math.floor(math.log10(n)+1)


# Driver Code
n = int(input("Enter a number: "))
print("Number of digits : % d" % (countDigit(n)))

# This code is contributed by Shreyanshi Arun
