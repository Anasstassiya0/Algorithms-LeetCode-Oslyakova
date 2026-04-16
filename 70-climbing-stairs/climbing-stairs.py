class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1:
            return 1
        if n==2:
            return 2
        a=1 #1 ступенька (предыдущая)
        b=2 #2 ступеньки (текущая)
        for i in range(3, n+1):
            c=a+b #3 ступеньки
            a=b
            b=c
        return b