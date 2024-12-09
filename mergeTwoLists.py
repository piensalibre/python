from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __eq__(self, other):
        current_self = self
        current_other = other
        while current_self and current_other:
            if current_self.val != current_other.val:
                return False
            current_self = current_self.next
            current_other = current_other.next
        return current_self is None and current_other is None

    def to_list(self):
        result = []
        current = self
        while current:
            result.append(current.val)
            current = current.next
        return result
    
class MergeTwoLists:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        nodoInicial = ListNode()
        puntero = nodoInicial

        while list1 and list2:
            if list1.val < list2.val:
                puntero.next = list1
                list1 = list1.next
            else:
                puntero.next = list2
                list2 = list2.next
            puntero = puntero.next

        puntero.next = list1 if list1 else list2

        return nodoInicial.next