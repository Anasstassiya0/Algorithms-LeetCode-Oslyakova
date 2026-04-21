class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        # если общая сумма нечетная
        if total_sum % 2 != 0:
            return False
            
        target = total_sum // 2
        # все возможные суммы, которые можно собрать
        possible_sums = {0}
        
        for x in nums:
            # новые суммы, добавляя текущее число к уже найденным
            new_sums = {s + x for s in possible_sums if s + x <= target}
            possible_sums.update(new_sums)
            
            # Если цель найдена, досрочно возвращаем результат
            if target in possible_sums:
                return True
         
        return False
