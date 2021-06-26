from collections import defaultdict     # Importing default dict from collections package


def countOccurrences(arr, n, k):
    # dict1 = {}
    dict1 = defaultdict(int)            # dict1 using default dictionary
    for key in arr:
        # if key not in dict1:          # Adding the element into dictionary if default dictionary is not used
        #     dict1[key] = 1
        # else:
        #     dict1[key] += 1           # Incrementing the value part of dict1
        dict1[key] += 1
    count = 0
    for value in dict1:
        if dict1[value] > n//k:
            count += 1
    return count


if __name__ == '__main__':
    le = int(input())
    nums = []
    for i in range(le):
        nums.append(int(input()))
    x = int(input())
    print(countOccurrences(nums, le, x))
