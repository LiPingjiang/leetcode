class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        后面的一个数减前面一个数的max值
        """
        if not prices :
            return 0
        max=0
        min_price=prices[0]
        for i in range(1,len(prices)):
            profit=prices[i]-min_price
            if prices[i] < min_price:
                min_price = prices[i]
            if profit > max:
                max = profit
        return max
    def maxProfit2(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        后面的一个数减前面一个数的max值
        使用 min,max   竟然更慢。。。。
        """
        if not prices :
            return 0
        max_profit=0
        min_price=prices[0]
        for i in range(1,len(prices)):
            profit=prices[i]-min_price
            min_price= min(prices[i],min_price)
            max_profit= max(profit > max_profit)
        return max_profit
    def maxProfit3(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        后面的一个数减前面一个数的max值
        使用 for p in ps 竟然更慢。。。。
        """
        if not prices :
            return 0
        max=0
        min_price=prices[0]
        for p in prices:
            profit=p-min_price
            if p < min_price:
                min_price = p
            if profit > max:
                max = profit
        return max

if __name__ == '__main__':
    import time
    start = time.clock()
    s=Solution()
    # print(s.maxProfit([7,1,5,3,6,4]))
    print(s.maxProfit([7,1,5,3,6,4]))
    print("Time Used: " + str(time.clock() - start))