class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        if self.head is None:
            return
        elif position == 1:
            return self.head

        index = 1
        current = self.head

        while current.next:
            index += 1
            current = current.next
            if index == position:
                return current

    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        if position == 1:
            if self.head:
                new_element.next = self.head
            self.head = new_element
            return

        index = 1
        prev_elem = self.head
        cur_elem = prev_elem.next

        while cur_elem:
            index += 1
            if index == position:
                new_element.next = cur_elem
                prev_elem.next = new_element
                return
            prev_elem = cur_elem
            cur_elem = cur_elem.next

    def delete(self, value):
        """Delete the first node with a given value."""
        if self.head and self.head.value == value:
            self.head = self.head.next
            return

        prev_elem = self.head
        cur_elem = prev_elem.next

        while cur_elem:
            if cur_elem.value == value:
                prev_elem.next = cur_elem.next
                return
            prev_elem = cur_elem
            cur_elem = cur_elem.next
