class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min = float('inf')
        profit = 0
        for i in prices:
            if i < min:
                min = i
            temp = i - min
            if temp > profit:
                profit = temp
        return profit