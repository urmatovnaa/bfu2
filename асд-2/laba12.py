#Решить дискретную задачу о рюкзаке.

def knapsack(weights, costs, W):
    n = len(weights)
    dp = [0] * (W + 1)
    selected = [[] for i in range(W + 1)]

    for i in range(n):
        for w in range(W, weights[i] - 1, -1):
            if dp[w - weights[i]] + costs[i] > dp[w]:
                dp[w] = dp[w - weights[i]] + costs[i]
                selected[w] = selected[w - weights[i]] + [i]
    return dp[W], selected[W]

weights = [4, 2, 5]
costs = [8, 6, 12]
W = 10
result = knapsack(weights, costs, W)
print("Максимальная стоимость:", result[0])
print("Выбранные предметы:", result[1])
