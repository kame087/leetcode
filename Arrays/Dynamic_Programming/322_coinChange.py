class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        """
            * HIGH LEVEL:
            * This is a great exercise for dynamic programming approach. 
            * The method I used is a bottom-up approach because it’s the one that made more sense to me.
            
            * Here’s the breakdown of the approach.
            * Build an min_coins array of length amount +  1, where the min amount of coins to make 0 is 0, where each index value represents the amount, and the value in the array[index] represents the min coins to  make “index” essentially.
            * For example: if amount = 11, then min_coins = [0, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12]
            * for each index of min_coins array:
                * for each coin value “j” in coins array:
                    * calculate the value if you were to use coin[i] and subtract it from i: change = (i - coins[j])
                    * if change >= 0: (this means you can make change)
                        * min_coins[i] = min(min_coins[i], min_coins[change] + 1) # it’s “ + 1” because you’re taking + 1 from coin[j]
            * By the end you should have the minimum to make amount on min_coins[amount]
            * if min_coins[amount] == amount + 1:
                * that means you couldn’t make that amount with the coins given
                * return -1
            * return min_coins[amount]

            * Time Complexity = O(A * c), A= amount, c = len(coins) array. Space Complexity = O(A), A = amount
        
        
        """
        
        default_min_coins = amount + 1
        min_coins = [default_min_coins] * default_min_coins
        
        min_coins[0] = 0
        
        for i in range(1, len(min_coins)):
            for j in range(len(coins)):
                change = i - coins[j]
                if change >= 0:
                    min_coins[i] = min(min_coins[i], min_coins[i - coins[j]]+1)
        
        
        if min_coins[-1] == default_min_coins:
            return -1
        
        return min_coins[-1]
        