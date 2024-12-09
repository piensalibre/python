import unittest
from mergeTwoLists import MergeTwoLists, ListNode  

def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for value in arr[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

class TestMergeTwoLists(unittest.TestCase):

    def setUp(self):
        self.solution = MergeTwoLists()
        
    def test_both_empty(self):
        result = self.solution.mergeTwoLists(None, None)
        self.assertIsNone(result)

    def test_one_empty(self):
        list1 = create_linked_list([1, 3, 5])
        list2 = None
        expected = create_linked_list([1, 3, 5])
        result = self.solution.mergeTwoLists(list1, list2)
        self.assertEqual(result, expected)
    
    def test_two_single_element_lists(self):
        list1 = create_linked_list([1])
        list2 = create_linked_list([2])
        expected = create_linked_list([1, 2])
        result = self.solution.mergeTwoLists(list1, list2)
        self.assertEqual(result, expected)
        
    def test_multiple_elements(self):
        list1 = create_linked_list([1, 2, 4])
        list2 = create_linked_list([1, 3, 4])
        expected = create_linked_list([1, 1, 2, 3, 4, 4])
        result = self.solution.mergeTwoLists(list1, list2)
        self.assertEqual(result, expected)
    
    def test_different_lengths(self):
        list1 = create_linked_list([1, 3, 5, 7])
        list2 = create_linked_list([2, 4])
        expected = create_linked_list([1, 2, 3, 4, 5, 7])
        result = self.solution.mergeTwoLists(list1, list2)
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
