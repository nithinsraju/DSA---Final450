def bruteForce(arr):                      # Brute force solution (Checks all the subArrays)
    max = 0
    curSum = 0                         # Current sum of the sub-array
    for i in range(len(arr)):
        sum = 0
        for j in range(i, len(arr)):
            sum += arr[j]
            if sum > max:
                max = sum
        sum = 0
    return max


def kadenAlgo(arr):
    curSum = 0
    max = 0
    for i in range(len(arr)):  # Solution using Kaden's algorithm
        curSum += arr[i]
        if curSum > max:
            max = curSum
        if curSum < 0:
            curSum = 0
    return max


if __name__ == "__main__":
    arr = []
    for i in range(int(input())):
        arr.append(int(input()))
    print(bruteForce(arr))
    print(kadenAlgo(arr))

