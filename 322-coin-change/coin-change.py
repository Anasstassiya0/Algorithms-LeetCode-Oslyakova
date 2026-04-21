class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # минимальное количество монет для каждой суммы
        min_coins = [amount + 1] * (amount + 1)
        min_coins[0] = 0 
        # оптимальный набор для каждой суммы от 1 до amount
        for current_amount in range(1, amount + 1):
            for coin in coins:
                if current_amount - coin >= 0:
                    # самый экономный вариант из уже посчитанных
                    min_coins[current_amount] = min(min_coins[current_amount], 1 + min_coins[current_amount - coin])
        # Если значение осталось начальным 
        return min_coins[amount] if min_coins[amount] != amount + 1 else -1
