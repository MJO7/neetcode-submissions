# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        # my solution
        
        firstNum = 0

        len_of_first_list = 0
        l1_head = l1
        while l1_head:
            len_of_first_list += 1
            l1_head = l1_head.next

        i = 0
        while i in range(0, len_of_first_list) and l1:
            power_of_ten = 10 ** (len_of_first_list - 1 - i)
            firstNum += (l1.val) * power_of_ten
            l1 = l1.next
            i = i + 1

        first_num_str = str(firstNum)
        first_num_str = first_num_str[::-1]
        first_num_final = int(first_num_str)

        # --
        secondNum = 0

        len_of_second_list = 0
        l2_head = l2
        while l2_head:
            len_of_second_list += 1
            l2_head = l2_head.next

        j = 0
        while j in range(0, len_of_second_list) and l2:
            power_of_ten = 10 ** (len_of_second_list - 1 - j)
            secondNum += (l2.val) * power_of_ten
            l2 = l2.next
            j = j + 1

        second_num_str = str(secondNum)
        second_num_str = second_num_str[::-1]
        second_num_final = int(second_num_str)

        resultNum = first_num_final+ second_num_final
        resultNum_str = str(resultNum)
        resultNum_str = resultNum_str[::-1]
        
        dummy = ListNode()
        curr = dummy

        for k in resultNum_str:
            next_node = ListNode(int(k), None)
            curr.next = next_node
            curr = curr.next

        return dummy.next
