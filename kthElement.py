def kmin(nums1, k1):
    nums1.sort()
    print(nums1[k1 - 1])


def kmax(nums2, k2):
    nums2.sort(reverse=True)
    print(nums2[k2 - 1])


if __name__ == '__main__':
    k = int(input())
    nums = []
    for i in range(int(input())):
        nums.append(int(input()))
    kmin(nums, k)
    kmax(nums, k)
