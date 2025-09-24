
class Node:
    def __init__(self, book_title):
        self.book_title = book_title
        self.next = None


class StackLinkedList:
    def __init__(self):
        self.top = None

    
    def push(self, book_title):
        new_node = Node(book_title)
        new_node.next = self.top
        self.top = new_node
        print(f"Book '{book_title}' added to stack.")

   
    def pop(self):
        if not self.is_empty():
            book = self.top.book_title
            self.top = self.top.next
            print(f"Book '{book}' retrieved from stack.")
            return book
        else:
            print("Stack is empty. No book to retrieve.")
            return None

    def peek(self):
        if not self.is_empty():
            return self.top.book_title
        return None

    def is_empty(self):
        return self.top is None

    def display(self):
        books = []
        current = self.top
        while current:
            books.append(current.book_title)
            current = current.next
        print("Current Stack:", books)
