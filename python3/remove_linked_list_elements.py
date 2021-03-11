class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def print(self):
        it = self
        while it:
            print(it.val)
            it = it.next


def removeElements(head: ListNode, val: int) -> ListNode:
    while head and head.val == val:
        head = head.next

    it = head
    while it is not None:
        while it.next is not None and it.next.val == val:
            it.next = it.next.next
        it = it.next

    return head


def createList(l: list) -> ListNode:
    if not l:
        return None

    head = ListNode(l[0])
    it = head

    for ele in l[1:]:
        it.next = ListNode(ele)
        it = it.next

    return head


if __name__ == '__main__':
    # case 1
    head = createList([1, 2, 6, 3, 4, 5, 6])

    print('=================')
    remove_result = removeElements(head, 6)
    remove_result.print()

    # case 2
    head = createList([1, 2, 6, 6, 3, 4, 5, 6])

    print('=================')
    remove_result = removeElements(head, 6)
    remove_result.print()

    # case 3
    head = createList([6, 1, 2, 6, 6, 3, 4, 5])

    print('=================')
    remove_result = removeElements(head, 6)
    remove_result.print()

    # case 4
    head = createList([6])

    remove_result = removeElements(head, 6)
    assert remove_result == None

    # case 4
    head = createList([])

    remove_result = removeElements(head, 6)
    assert remove_result == None
