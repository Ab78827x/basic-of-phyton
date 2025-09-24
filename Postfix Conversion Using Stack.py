class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        return len(self.items) == 0



def precedence(op):
    if op in ('+', '-'):
        return 1
    if op in ('*', '/'):
        return 2
    if op == '^': 
        return 3
    return 0


def is_right_associative(op):
    return op == '^'



def infix_to_postfix(expression):
    stack = Stack()
    output = []

    for token in expression:
        
        if token.isalnum():  
            output.append(token)

        
        elif token == '(':
            stack.push(token)

       
        elif token == ')':
            while not stack.is_empty() and stack.peek() != '(':
                output.append(stack.pop())
            stack.pop()  

        
        else:
            while (not stack.is_empty() and 
                   precedence(stack.peek()) > precedence(token) or
                   (precedence(stack.peek()) == precedence(token) and not is_right_associative(token))):
                output.append(stack.pop())
            stack.push(token)

    
    while not stack.is_empty():
        output.append(stack.pop())

    return "".join(output)



infix_expr = "A+(B*C-(D/E^F)*G)*H"
print("Infix Expression: ", infix_expr)
postfix_expr = infix_to_postfix(infix_expr)
print("Postfix Expression:", postfix_expr)
