class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummy = ListNode(0)
        current = dummy
        
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
            
        current.next = list1 if list1 else list2
        
        return dummy.next

# Example usage:
# Creating the linked lists for the first example
list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4)))

solution = Solution()
merged_list = solution.mergeTwoLists(list1, list2)

# Function to print the linked list
def print_linked_list(head: ListNode):
    current = head
    while current:
        print(current.val, end=' ')
        current = current.next
    print()

print_linked_list(merged_list)  # Output: 1 1 2 3 4 4 
