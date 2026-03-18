class MinStack:

    def __init__(self):
        self.stack = []  # основной стек
        self.min_stack = []  # стек минимумов

    def push(self, val: int) -> None:
        self.stack.append(val)
        
        # если пустой - просто добавляем
        if len(self.min_stack) == 0:
            self.min_stack.append(val)
        else:
            # сохраняем текущий минимум
            current_min = self.min_stack[-1]
            if val < current_min:
                self.min_stack.append(val)
            else:
                self.min_stack.append(current_min)

    def pop(self) -> None:
        if len(self.stack) != 0:
            self.stack.pop()
            self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack() 
# obj.push(val)
# obj.pop() 
# param_3 = obj.top() 
# param_4 = obj.getMin()