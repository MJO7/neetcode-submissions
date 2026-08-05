class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None
        self.prev = None

class MyLinkedList:

    def __init__(self):
        self.left = ListNode(0)
        self.right = ListNode(0)  
        self.left.next = self.right
        self.right.prev = self.left

    def get(self, index: int) -> int:
        cur = self.left.next
        while cur and index>0:
            cur = cur.next
            index -=1
    #    3 cases possible here
    #    1. The index is much greater, so cur becomes None and we get out of while loop --- so directly invalid
    #    2. The index is exactly equal to right (the right sentinel) so it's invalid
    #    3. We consume all the steps of the array and are at the correct value
        if cur and index==0 and cur!=self.right:
            return cur.val
        return -1


    def addAtHead(self, val: int) -> None:
        node, next, prev = ListNode(val), self.left.next, self.left
        prev.next = node
        next.prev = node
        node.next = next
        node.prev = prev

    def addAtTail(self, val: int) -> None:
        node, next, prev = ListNode(val), self.right, self.right.prev
        prev.next = node
        next.prev = node
        node.next = next
        node.prev = prev

    def addAtIndex(self, index: int, val: int) -> None:
        cur = self.left.next
        while cur and index>0:
            cur = cur.next
            index -=1

        if cur and index==0:
            node, next, prev = ListNode(val), cur, cur.prev
            prev.next = node
            next.prev = node
            node.next = next
            node.prev = prev    
        return -1

    def deleteAtIndex(self, index: int) -> None:
        cur = self.left.next
        while cur and index > 0:
            cur = cur.next
            index -=1
        if index == 0 and cur and cur!=self.right:
            next, prev = cur.next, cur.prev
            next.prev = prev
            prev.next = next

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)