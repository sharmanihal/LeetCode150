
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Merge two sorted linked lists.

        Parameters:
        - list1: Head of the first sorted linked list
        - list2: Head of the second sorted linked list

        Returns:
        - Head of the merged sorted linked list
        """

        # Check if either of the lists is empty
        if not list1:
            return list2
        if not list2:
            return list1
        
        # Initialize the head of the merged list
        # Choose the smaller value as the head
        head = list1 if list1.val <= list2.val else list2

        # Initialize a current pointer for building the merged list
        curr = ListNode()

        # Loop until either of the lists is exhausted
        while list1 and list2:
            # Compare the values of the current nodes in both lists
            if list1.val <= list2.val:
                # Connect the current node to list1 and move the list1 pointer
                curr.next = list1
                list1 = list1.next
            else:
                # Connect the current node to list2 and move the list2 pointer
                curr.next = list2
                list2 = list2.next
            # Move the curr pointer to the last connected node
            curr = curr.next  

        # Connect the remaining nodes from the non-empty list
        curr.next = list1 or list2

        # Return the head of the merged list
        return head
    
"""
Explanation:

    1. Check for Empty Lists:
        The first two if statements check if either of the input lists (list1 or list2) is empty. If one of them is empty, the function returns the other list because there is nothing to merge.

    2. Initialize Head and Current Pointer:
        The code initializes the head of the merged list (head) by choosing the smaller value between the heads of list1 and list2.
        It also initializes a current pointer (curr) for building the merged list.

    3. Merge Lists Using Pointers:
        The while loop continues until either of the input lists is exhausted.
        Inside the loop, it compares the values of the current nodes in list1 and list2.
        If the value in list1 is smaller or equal, it connects the current node to the merged list through the curr pointer and moves the list1 pointer to the next node.
        If the value in list2 is smaller, it does the same with list2.
        This process continues until one of the lists is exhausted.

    4. Connect Remaining Nodes:
        After the loop, it connects the remaining nodes from the non-empty list (either list1 or list2) to the merged list.

    5. Return Merged List Head:
        Finally, it returns the head of the merged list.

This code effectively merges two sorted linked lists into a single sorted list by comparing the values of the nodes and connecting them in the correct order. The head variable keeps track of the beginning of the merged list, and the curr pointer helps in building the merged list."""
