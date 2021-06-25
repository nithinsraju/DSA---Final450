def buyStocks(prices):
    maxprofit = 0
    min1 = max(prices) + 1
    # for i in range(len(prices)):                  # Brute force approach O(n^2)
    #     for j in range(i + 1, len(prices)):
    #         if (prices[j] - prices[i]) > max1:
    #             max1 = prices[j] - prices[i]
    # print(max1)
    for i in range(len(prices)):
        if prices[i] < min1:
            min1 = prices[i]
        elif (prices[i] - min1) > maxprofit:
            maxprofit = prices[i] - min1
    print(maxprofit)


if __name__ == '__main__':                  # 7,6,4,3,1
    arr = []
    for j in range(int(input())):
        arr.append(int(input()))
    buyStocks(arr)
