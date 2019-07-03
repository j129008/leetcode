class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def tail(self):
        tail = self
        while tail.next is not None:
            tail = tail.next
        return tail

    def push_back(self, val):
        tail = self.tail()
        tail.next = ListNode(val)

    def show(self):
        node = self
        while node is not None:
            print(node.val)
            node = node.next


def mergeTwoLists(l1, l2):
    l1_head = ListNode(0)
    l1_head.next = l1
    l2_head = l2
    insert_point = l1_head
    while insert_point.next is not None and l2_head is not None:
        if insert_point.next.val > l2_head.val:
            l2_body = l2_head.next
            l2_head.next = insert_point.next
            insert_point.next = l2_head
            l2_head = l2_body
        else:
            insert_point = insert_point.next

    if l2_head is not None:
        insert_point.next = l2_head
    return l1_head.next


def mergeTwoListsFastImp(l1, l2):
    ans = ListNode(-1)
    tail = ans
    while (l1 is not None) and (l2 is not None):
        if l1.val > l2.val:
            tail.next = l2
            l2 = l2.next
        else:
            tail.next = l1
            l1 = l1.next
        tail = tail.next

    if l1 is not None:
        tail.next = l1
    else:
        tail.next = l2
    return ans.next


l1 = ListNode(1)
l1.push_back(2)
l1.push_back(4)

l2 = ListNode(3)
l2.push_back(6)
l2.push_back(7)

l3 = mergeTwoLists(l1, l2)
l3.show()
