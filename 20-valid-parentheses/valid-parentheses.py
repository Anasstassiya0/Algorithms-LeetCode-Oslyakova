class Solution:
    def remove_last(self, stack):
        # взять последний и удалить
        if len(stack) == 0:
            return None
        
        value = stack[len(stack) - 1]
        del stack[len(stack) - 1]
        return value

    def isValid(self, s: str) -> bool:
        st = []
        
        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        
        for c in s:
            if c in pairs:  # закрывающая
                if len(st) == 0:
                    return False
                
                top = self.remove_last(st)
                
                if top != pairs[c]:  # проверяем совпадение типов
                    return False
            else:
                st.append(c)  # открывающая
        
        return len(st) == 0