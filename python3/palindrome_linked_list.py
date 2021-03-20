class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def print(self):
        cur_node = self
        while cur_node:
            print(cur_node.val)
            cur_node = cur_node.next


def isPalindrome(head: ListNode) -> bool:
    fast, slow = head, head
    while fast.next and fast.next.next:
        fast = fast.next.next
        slow = slow.next

    middle = slow.next
    if middle is None:
        return True

    pre = middle
    cur = middle.next
    pre.next = None
    while cur:
        next_node = cur.next
        cur.next = pre
        pre = cur
        cur = next_node

    while pre:
        if pre.val != head.val:
            return False
        pre = pre.next
        head = head.next

    return True


if __name__ == '__main__':
    head = ListNode(1)

    print(isPalindrome(head))
