class Solution:
    def hasCycle(self, head):
        node_ids = set()
        while head is not None:
            node_ids.add(id(head))
            next_node = head.next
            if id(next_node) in node_ids:
                return True
            head = next_node
        return False
