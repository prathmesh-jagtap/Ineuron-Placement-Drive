import unittest


def move_zero(nums):
    """This helps to modify given array by moving zero at the last index whiout creating any new list or hash set.

    Args:
        nums (int): array of intergers

    Returns:
        int: modefied array which has all zeros at last index
    """
    # creat two pointer one for iteration and other is for non-zero elemnt
    left = right = 0

    while right < len(nums):

        if nums[right] != 0:
            nums[right], nums[left] = nums[left], nums[right]
            left += 1

        right += 1
    return nums

## TestCases 
class Testmove_zero(unittest.TestCase):
    def testcase1(self):
        nums = [0, 1, 0, 3, 12]
        output = [1, 3, 12, 0, 0]
        self.assertEqual(move_zero(nums), output, "Testcase 1 Passed!")

    def testcase2(self):
        nums = [0]
        output = [0]
        self.assertEqual(move_zero(nums), output, "Testcase 2 Passed!")
    print("All TestCase Passed!!")


if __name__ == "__main__":
    unittest.main()
