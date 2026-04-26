def coin_change_with_ways(coins, amount):
    # Min coins DP
    min_dp = [float('inf')] * (amount + 1)
    min_dp[0] = 0

    # Ways DP
    ways_dp = [0] * (amount + 1)
    ways_dp[0] = 1

    # Calculate number of ways
    for coin in coins:
        for i in range(coin, amount + 1):
            ways_dp[i] += ways_dp[i - coin]

    # Calculate minimum coins
    for i in range(1, amount + 1):
        for coin in coins:
            if i - coin >= 0:
                min_dp[i] = min(min_dp[i], min_dp[i - coin] + 1)

    min_coins = min_dp[amount] if min_dp[amount] != float('inf') else -1
    total_ways = ways_dp[amount]

    return min_coins, total_ways


# Example
coins = [1, 2, 5]
amount = 5

min_coins, ways = coin_change_with_ways(coins, amount)

print("Minimum coins required:", min_coins)
print("Number of ways:", ways)