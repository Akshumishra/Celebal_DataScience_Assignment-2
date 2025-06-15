# Celebal ( Data Science ) ----- Assignment 2 ( Implement a Linked List in Python Using OOP and Delete the Nth Node )

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            print(f"Added head node with value: {data}")
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            print(f"Added node with value: {data}")

    def print_list(self):
        current = self.head
        if not current:
            print("List is empty.")
            return
        print("Linked List:", end=" ")
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def delete_nth_node(self, n):
        try:
            if not self.head:
                raise Exception("Cannot delete from an empty list.")

            if n < 1:
                raise ValueError("Index must be a positive integer.")

            if n == 1:
                print(f"Deleting node at position {n} with value: {self.head.data}")
                self.head = self.head.next
                return

            current = self.head
            count = 1
            while current and count < n - 1:
                current = current.next
                count += 1

            if not current or not current.next:
                raise IndexError("Index out of range.")

            print(f"Deleting node at position {n} with value: {current.next.data}")
            current.next = current.next.next

        except Exception as e:
            print(f"Error: {e}")


# === Testing the Implementation ===
if __name__ == "__main__":
    ll = LinkedList()

    while True:
        print("\nChoose an operation:")
        print("1. Add a node")
        print("2. Print the list")
        print("3. Delete the nth node")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            value = input("Enter the value to add: ")
            ll.add_node(value)
        elif choice == '2':
            ll.print_list()
        elif choice == '3':
            try:
                index = int(input("Enter the position (1-based index) to delete: "))
                ll.delete_nth_node(index)
            except ValueError:
                print("Please enter a valid integer.")
        elif choice == '4':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select from 1 to 4.")


