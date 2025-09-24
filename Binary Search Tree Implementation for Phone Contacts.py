
class ContactNode:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
        self.left = None
        self.right = None


class ContactBST:
    def __init__(self):
        self.root = None

   
    def insert(self, root, name, phone):
        if root is None:
            return ContactNode(name, phone)

        if name.lower() < root.name.lower():
            root.left = self.insert(root.left, name, phone)
        elif name.lower() > root.name.lower():
            root.right = self.insert(root.right, name, phone)
        else:
            print(f"Contact '{name}' already exists. Updating phone number.")
            root.phone = phone
        return root

  
    def search(self, root, name):
        if root is None:
            return None
        if name.lower() == root.name.lower():
            return root
        elif name.lower() < root.name.lower():
            return self.search(root.left, name)
        else:
            return self.search(root.right, name)


    def min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

   
    def delete(self, root, name):
        if root is None:
            return root

        if name.lower() < root.name.lower():
            root.left = self.delete(root.left, name)
        elif name.lower() > root.name.lower():
            root.right = self.delete(root.right, name)
        else:
           
            if root.left is None and root.right is None:
                return None
            
            elif root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            
            temp = self.min_value_node(root.right)
            root.name, root.phone = temp.name, temp.phone
            root.right = self.delete(root.right, temp.name)
        return root

    
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(f"Name: {root.name}, Phone: {root.phone}")
            self.inorder(root.right)


    def count_contacts(self, root):
        if root is None:
            return 0
        return 1 + self.count_contacts(root.left) + self.count_contacts(root.right)
