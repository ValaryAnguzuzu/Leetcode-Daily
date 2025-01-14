# Given the head of a singly linked list, reverse the list, and return the reversed list.

# Example 1:

# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]
# Example 2:


# Input: head = [1,2]
# Output: [2,1]
# Example 3:

# Input: head = []
# Output: []

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        Approach: 3 pointers - prev, cur, next
        TC: O(n)
        SC: O(1)
        """

#prev - null
# curr - curr node
# next - curr.next
# iterate while curr is not None
# create temp var for next node
# update curr.next pointer to prev; prev to be curr and curr to be next
#return prev

        prev = None
        curr = head

        while curr: 
            nextnode = curr.next #temp var
            curr.next = prev #update pointer

            prev = curr
            curr = nextnode
        return prev #at end of loop, cur points to  null and prev points to last node which is the 
                   #head of our reversed list
        
# Helper function: Convert a Python list to a linked list
def list_to_linkedlist(lst):
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for val in lst[1:]:
        current.next = ListNode(val)
        current = current.next
    return head



# Helper function: Convert a Python list to a linked list
def list_to_linkedlist(lst):
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for val in lst[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function: Convert a linked list to a Python list
def linkedlist_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

# Main function to test the solution
if __name__ == "__main__":
    solution = Solution()

    # Test cases
    test_cases = [
        [1, 2, 3, 4, 5],       # Regular case [5,4,3,2,1]
        [1, 2],                # Two elements [2,1]
        [1],                   # Single element [1]
        [],                    # Empty list []
        [7, 7, 7, 7],          # All elements the same [7,7,7,7]
       list(range(1, 1001)),  # Large list [1000, 999, ...,1]
        [-1, -2, -3, -4, -5],  # Negative numbers [-5,-4,-3,-2,-1]
        [-10, 0, 10, 20]       # Mixed positive and negative numbers [20,10,0,-10]
    ]

    # Run all test cases
    for i, test in enumerate(test_cases):
        head = list_to_linkedlist(test)            # Convert Python list to linked list
        reversed_head = solution.reverseList(head) # Reverse the linked list
        result = linkedlist_to_list(reversed_head) # Convert the reversed linked list back to Python list
        print(f"Test case {i + 1}: {result}")


 