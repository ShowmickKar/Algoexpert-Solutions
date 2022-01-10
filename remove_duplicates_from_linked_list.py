# Problem Link: https://www.algoexpert.io/questions/Remove%20Duplicates%20From%20Linked%20List
# Time Complexity = O(N)
# Space Complexity = O(1)

# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(head):
    cur = head
    while cur != None:
        next_node = cur.next
        if next_node != None and next_node.value == cur.value:
            cur.next = cur.next.next if cur.next.next != None else None
        else:
            cur = cur.next
    return head
