class Solution(object):
    def sortList(self, head):
        if not head:
            return None

        values = []
        current = head
        while current:
            values.append(current.val)
            current = current.next
        
        values.sort()
        
        current = head
        for val in values:
            current.val = val
            current = current.next
        
        return head

