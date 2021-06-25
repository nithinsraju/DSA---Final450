from collections import defaultdict


def countPairs(arr):
    count = 0
    # for i in range(len(arr)):             # Brute force method which takes O(n^2) time complexity
    #     for j in range(i + 1, len(arr)):
    #         if arr[i] == arr[j]:
    #             count += 1
    # print(count)

    dict1 = defaultdict(int)

    for value in arr:                       # Another method which has a O(n) time complexity
        count += dict1[value]
        dict1[k - value] += 1
    print(count)


if __name__ == '__main__':
    nums = []
    for x in range(int(input())):           # Taking input from user
        nums.append(int(input()))
    k = int(input())
    countPairs(nums)
