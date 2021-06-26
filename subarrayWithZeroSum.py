def zeroSum(arr, m):
    cur_sum = 0                                     # Current running sum of the sub-array
    sum_set = set()
    for i in range(m):
        cur_sum += arr[i]
        if cur_sum == 0 or cur_sum in sum_set:      # Current sum is zero or current sum already present in set
            return True                             # Then sum of sub-array is zero (return True)
        sum_set.add(cur_sum)                        # Add current sum to the set
    return False


if __name__ == '__main__':
    nums = []
    n = int(input())
    for j in range(n):
        nums.append(int(input()))
    print(zeroSum(nums, n))
