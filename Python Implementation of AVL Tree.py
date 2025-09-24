
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    
    def get_height(self, root):
        if not root:
            return 0
        return root.height

   
    def get_balance(self, root):
        if not root:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)

    
    def right_rotate(self, y):
        x = y.left
        T2 = x.right

        
        x.right = y
        y.left = T2

       
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))

        return x

    
    def left_rotate(self, x):
        y = x.right
        T2 = y.left

       
        y.left = x
        x.right = T2

        
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    
    def insert(self, root, key):
       
        if not root:
            return Node(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        elif key > root.key:
            root.right = self.insert(root.right, key)
        else:  
            return root

      
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

       
        balance = self.get_balance(root)

      
        if balance > 1 and key < root.left.key:
            return self.right_rotate(root)

        
        if balance < -1 and key > root.right.key:
            return self.left_rotate(root)

       
        if balance > 1 and key > root.left.key:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

    
        if balance < -1 and key < root.right.key:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root


    def min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

  
    def delete(self, root, key):
        if not root:
            return root

        
        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            temp = self.min_value_node(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)

        if not root:
            return root

        
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        
        balance = self.get_balance(root)

       
      
        if balance > 1 and self.get_balance(root.left) >= 0:
            return self.right_rotate(root)

     
        if balance > 1 and self.get_balance(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

       
        if balance < -1 and self.get_balance(root.right) <= 0:
            return self.left_rotate(root)

      
        if balance < -1 and self.get_balance(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

  
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.key, end=" ")
            self.inorder(root.right)

    
    def preorder(self, root):
        if root:
            print(root.key, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)
