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
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    if not fast:
        slow = slow.next

    pre = None
    while slow:
        slow_next = slow.next
        slow.next = pre
        pre = slow
        slow = slow_next

    while head and head.val == pre.val:
        head = head.next
        pre = pre.next

    return not pre


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(1)
    assert isPalindrome(head) is True

    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(2)
    assert isPalindrome(head) is False
