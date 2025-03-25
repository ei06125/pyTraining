from remove_elements.remove_elements import Solution


def test_remove_element():
    s = Solution()

    # Example 1
    k = s.removeElement(nums=[3, 2, 2, 3], val=3)  # Calls implementation
    assert k == len([2, 2])

    # # Example 2
    k = s.removeElement(nums=[0, 1, 2, 2, 3, 0, 4, 2], val=2)
    expected = [0, 1, 4, 0, 3]
    assert k == len(expected)
