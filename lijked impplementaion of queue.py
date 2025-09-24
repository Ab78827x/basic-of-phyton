
class Node:
    def __init__(self, car):
        self.car = car
        self.next = None


class QueueLinkedList:
    def __init__(self):
        self.front = None
        self.rear = None

   
    def enqueue(self, car):
        new_node = Node(car)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        print(f"Car '{car}' entered the parking lot.")

   
    def dequeue(self):
        if not self.is_empty():
            car = self.front.car
            self.front = self.front.next
            if self.front is None:
                self.rear = None
            print(f"Car '{car}' exited the parking lot.")
            return car
        else:
            print("Parking lot is empty. No car to exit.")
            return None

    def peek(self):
        if not self.is_empty():
            return self.front.car
        return None

    def is_empty(self):
        return self.front is None

    def display(self):
        cars = []
        current = self.front
        while current:
            cars.append(current.car)
            current = current.next
        print("Cars in parking lot:", cars)
