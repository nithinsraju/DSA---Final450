def minMax(arr, n):
    if n == 1:                          # Array containing only one element
        mini = arr[0]
        maxi = arr[0]
    elif arr[0] < arr[1]:               # Finding minimum and maximum element in the first two elements
        mini = arr[0]
        maxi = arr[1]
    else:
        mini = arr[1]
        maxi = arr[0]

    for j in range(2, n):               # Traversing through the array from the second element
        if arr[j] > maxi:
            maxi = arr[j]
        elif arr[j] < mini:
            mini = arr[j]
    print(mini)
    print(maxi)


if __name__ == '__main__':
    nums = []
    m = int(input())                        # Taking input from the user
    for i in range(m):
        nums.append(int(input()))
    minMax(nums, m)
