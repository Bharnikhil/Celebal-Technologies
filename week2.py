class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, data):
        new_node = Node(data)
        if (self.head==None):
            self.head = new_node
            return
        # Traverse to the last node if list is not empty and then join the new Node
        current = self.head
        while (current.next!=None):
            current = current.next
        current.next = new_node

    def print_list(self):
        if self.head==None:
            print("List is empty.")
            return
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def delete_nth_node(self, n):
        if self.head==None:
            raise Exception("Cannot delete from an empty list.")
        if n <= 0:
            raise IndexError("Index must be a positive integer.")
        if n == 1:
            self.head = self.head.next
            return

        # Traverse to the (n-1)th node
        current = self.head
        count = 1
        while current!=None  and count < n - 1:
            current = current.next
            count += 1

        if current is None:
            raise IndexError("List is too short.")

        if current.next is None:
            raise IndexError("No node to delete at that position.")

        current.next = current.next.next

ll = LinkedList()

# Add nodes
ll.add_node(10)
ll.add_node(20)
ll.add_node(30)
ll.add_node(40)

# Print initial list
print("Initial Linked List:")
ll.print_list()

# Delete the 2nd node
print("\nDeleting 2nd node...")
ll.delete_nth_node(2)
ll.print_list()

# Try deleting an out-of-range node
print("\nTrying to delete 10th node...")
try:
    ll.delete_nth_node(10)
except Exception as e:
    print("Error:", e)

# Try deleting from an empty list
print("\nEmpty list delete test...")
empty_ll = LinkedList()
try:
    empty_ll.delete_nth_node(1)
except Exception as e:
    print("Error:", e)

