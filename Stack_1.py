Max_size = 5
Stack = []
top = -1

def is_empty():
    return


def push(data):
    global top
    if top>=Max_size:
        print("overflow...")
    else:
        Stack.append(data)
        print("the book pushed to the stack: ", Stack)
        top += 1

def pop():
    global top
    if Stack is None:
        print("underflow...")
    else:
        remove_data = Stack.pop()
        print("the book removed: ", remove_data)
        top -= 1

def peek():
    global top
    if top == -1:
        print("the Stack is empty...")
    else:
        print("the book at the top is: ", Stack[top])

def display():
    if top == -1:
        print("stack is empty...")
    else:
        for i in range(top, -1, -1):
            print(f"{i+1}, {Stack[i]}")
push("abc")
push("def")
push("ghi")
pop()
peek()
display()
