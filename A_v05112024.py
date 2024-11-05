def long_sub(arr):
    n = len(arr)
    if n == 0:
        return []

    dp = [1] * n
    prev_index = [-1] * n
    
    for i in range(1, n):
        for j in range(i):
            if ((arr[j] < arr[i] and (j == 0 or arr[j-1] > arr[j]))
                or (arr[j] > arr[i] and (j == 0 or arr[j-1] < arr[j]))) and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                prev_index[i] = j

    max_index = 0
    for i in range(1, n):
        if dp[i] > dp[max_index]:
            max_index = i

    result = []
    while max_index != -1:
        result.append(arr[max_index])
        max_index = prev_index[max_index]

    result.reverse()
    return result

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split()))
    result = long_sub(arr)
    print(' '.join(map(str, result)))