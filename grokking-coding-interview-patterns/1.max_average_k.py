def find_sum_regular(arr, k):
    result = []
    for i in range(len(arr) - k + 1):
        # find sum of next k elements
        sum = 0
        for j in range(i, i + k):
            sum += arr[j]
        # calculate average
        result.append(sum/k)
    return result

def find_sum_sliding_window(arr,k):
    result = []
    length = len(arr)
    i, sum=0,0
    while i < k:
        sum = sum + arr[i]
        i= i+1
    result.append(sum/k)
    
    while i < length:
        sum = sum - arr[i-k] + arr[i]
        result.append(sum/k)
        i = i+1
    return result
        

def main():
    print("Averages of subarrays of size k: " + str(find_sum_regular([1, 3, 2, 6, -1, 4, 1, 8, 2], 5)))
    print("Averages of subarrays of size k - Sliding Window: " + str(find_sum_sliding_window([1, 3, 2, 6, -1, 4, 1, 8, 2], 5)))

main()
