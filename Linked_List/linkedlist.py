class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def create_linked_list(nums):
    n=len(nums)
    if n==0:
        return None
    
    head = Node(nums[0])
    current = head
    
    for i in range(1,n):
        current.next = Node(nums[i])
        current = current.next
        
    return head

def print_list(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

def insert_at_head(head, value):
    new_node = Node(value)
    new_node.next = head
    return new_node

def delete_node(head, key):
    if head is None:
        return None
    
    if head.data == key:
        return head.next
    
    current = head
    
    while current.next:
        if current.next.data == key:
            current.next = current.next.next
            return head
        current = current.next
    
    return head

def length(head):
    count = 0
    current = head
    
    while current:
        count += 1
        current = current.next
        
    return count

def search(head, key):
    current = head
    
    while current:
        if current.data == key:
            return True
        current = current.next
        
    return False
