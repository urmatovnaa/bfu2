#Проблема размена монет: поиск количества способов внести сдачу на заданную сумму денег, используя заданный набор номиналов монет.
# Coin change problem

def make_change(S, coins):
    dp = [0] * (S + 1)
    dp[0] = 1
    coins = set(coins)
    for coin in coins:
        for i in range(coin, S + 1):
            dp[i] += dp[i - coin]

    return dp[S]

M = 8
coins = [3, 2, 5, 6]
# 3 2 3 3
# 2 2 2 2 3
# 5 6
# 5 3 3
# 6 2 3
# 2 2 2 5
print(make_change(M, coins))
