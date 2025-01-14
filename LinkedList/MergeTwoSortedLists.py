# <!-- 21. Merge Two Sorted Lists

# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.

 

# Example 1:


# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
# Example 2:

# Input: list1 = [], list2 = []
# Output: []
# Example 3:

# Input: list1 = [], list2 = [0]
# Output: [0]
 

# Constraints:

# The number of nodes in both lists is in the range [0, 50].
# -100 <= Node.val <= 100
# Both list1 and list2 are sorted in non-decreasing order. -->


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):

        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        Approach: 
        TC:O(n)
        SC:O(1)
        """
#create a dummy node with next pointer pointing to current list
#while the two lists are non empty, compare the values at each step and append the smallest to the dummy.next as you update the node to the next node
#if one list is empty, if l1...append all of list2 nodes to dummy, if list2, append all of list1 nodes to dummy, update tail.next to next node
#if both lists are empty? return empyty list

        dummyNode = ListNode()
        tail = dummyNode

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1 #point to the smaller node
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next #always update the tail pointer

        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
        
        return dummyNode.next #head of sorted list


# Convert a Python list to a linked list
def list_to_linkedlist(lst):
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for val in lst[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Convert a linked list to a Python list
def linkedlist_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([1, 2, 4], [1, 3, 4]),       # Test case 1 [1, 1, 2, 3, 4, 4]
        ([], [0]),                    # Test case 2 [0]
        ([], []),                     # Test case 3 []
        ([2], [1]),                   # Test case 4 [1,2]
        ([1, 1, 2], [1, 3, 4])        # Test case 5 [1,1,1,2,3,4]
    ]

    for i, (list1, list2) in enumerate(test_cases):
        l1 = list_to_linkedlist(list1)
        l2 = list_to_linkedlist(list2)
        merged_head = solution.mergeTwoLists(l1, l2)
        result = linkedlist_to_list(merged_head)
        print(f"Test case {i + 1}: {result}")
