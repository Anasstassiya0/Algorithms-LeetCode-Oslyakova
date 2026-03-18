class Solution:
    def evalRPN(self, tokens):
        stack = []
        
        for token in tokens:
            # если оператор
            if token in ["+", "-", "*", "/"]:
                b = stack.pop()
                a = stack.pop()
                
                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                else:
                    # деление с усечением к нулю
                    stack.append(int(a / b))
            else:
                # если число
                stack.append(int(token))
        
        return stack[0]