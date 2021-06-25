def reverse(nums, m):                   # Reversing an array using an additional array
    nums1 = []
    for i in range(m-1, -1, -1):        # Traversing the array nums from last
        nums1.append(nums[i])
    return nums1


def reverseList(nums2, x):              # Reversing an array without using an extra array
    start = 0
    while start < (x - 1):                    # x is the length of the array
        nums2[start], nums2[x - 1] = nums2[x - 1], nums2[start]
        start += 1
        x -= 1
    return nums2


if __name__ == '__main__':              # Taking input from user
    arr = []
    n = int(input())
    for j in range(n):
        arr.append(int(input()))
    print(reverse(arr, n))
    print(reverseList(arr, n))
