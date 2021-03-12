class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def print(self):
        it = self
        while it:
            print(it.val)
            it = it.next


def createList(l: list) -> ListNode:
    if not l:
        return None

    head = ListNode(l[0])
    it = head

    for ele in l[1:]:
        it.next = ListNode(ele)
        it = it.next

    return head


def reverseList(head: ListNode) -> ListNode:
    '''
    先存下所有的 node address, 之後一起做 reverse
    '''
    if head is None:
        return None

    ptrs = []
    it = head
    while it:
        ptrs.append(it)
        it = it.next

    for i in range(len(ptrs)):
        ptrs[i].next = ptrs[i-1]
    ptrs[0].next = None

    return ptrs[-1]


if __name__ == '__main__':
    # case 1
    head = createList([1, 2, 3, 4, 5, 6])
    result = reverseList(head)
    result.print()

    # case 2
    print('=====================')
    head = createList([1])
    result = reverseList(head)
    result.print()

    # case 3
    print('=====================')
    head = createList([1, 2])
    result = reverseList(head)
    result.print()

    # case 4
    print('=====================')
    head = createList([])
    result = reverseList(head)
    assert result is None
