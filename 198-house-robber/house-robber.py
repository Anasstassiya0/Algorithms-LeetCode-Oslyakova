class Solution:
    def rob(self, nums: List[int]) -> int:
        a = 0  # сумма через один дом назад
        b = 0 # сумма в предыдущем доме
        
        for x in nums:
            # взять деньги сейчас (a + x) или не рисковать (b)
            c = max(b, a + x)
            a = b
            b = c # текущий max
        
        return b