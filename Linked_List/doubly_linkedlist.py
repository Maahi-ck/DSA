class Node:
    def __init__(self, value):
        self.data = value
        self.next = None
        self.prev = None


def create_dll(nums):
    if len(nums) == 0:
        return None

    head = Node(nums[0])
    current = head

    for i in range(1, len(nums)):
        new_node = Node(nums[i])
        current.next = new_node
        new_node.prev = current
        current = new_node

    return head


def print_list(head):
    current = head
    while current:
        print(current.data, end=" <-> ")
        current = current.next
    print("None")


def print_reverse(head):
    if head is None:
        return

    current = head
    while current.next:
        current = current.next

    while current:
        print(current.data, end=" <-> ")
        current = current.prev
    print("None")


def insert_at_head(head, value):
    new_node = Node(value)

    if head is not None:
        head.prev = new_node
        new_node.next = head

    return new_node


def insert_at_tail(head, value):
    new_node = Node(value)

    if head is None:
        return new_node

    current = head
    while current.next:
        current = current.next

    current.next = new_node
    new_node.prev = current

    return head


def delete_node(head, key):
    if head is None:
        return None

    current = head

    while current:
        if current.data == key:

            if current.prev:
                current.prev.next = current.next
            else:
                head = current.next

            if current.next:
                current.next.prev = current.prev

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

