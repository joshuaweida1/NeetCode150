"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        listToCopy = {None : None}
        cur = head
        while cur:
            copy = Node(cur.val)
            listToCopy[cur] = copy
            cur = cur.next
        cur = head
        while cur:
            copy = listToCopy[cur]
            copy.next = listToCopy[cur.next]
            copy.random = listToCopy[cur.random]
            cur = cur.next
        return listToCopy[head]
            

