import unittest


def unique_character1(s):
    """This function uses built-in function to find the index of 
    character which is unique.

    Args:
        s (str): string

    Returns:
        int: index of first unique character or -1
    """

    for char in s:
        if s.count(char) == 1:
            return s.index(char)
    return -1


def unique_character2(s):
    """This function also find the first index of unique character from given 
    string by using hash map apporach

    Args:
        s (str): string

    Returns:
        int: index of unique character or -1
    """
    chars = {}  # hashmap

    # or chars = Counter(s)
    # both below loop and counter works same
    for char in s:
        if char not in chars:
            chars[char] = 1

        else:
            chars[char] += 1

    # searching for character
    for i, char in enumerate(s):
        if chars[char] == 1:
            return i

    return -1


# Testcases
class TestUniqueCharacter(unittest.TestCase):
    def testcase1(self):
        s = "leetcode"
        output = 0
        self.assertEqual(unique_character1(s), output, "Testcase 1 Passed!")
        self.assertEqual(unique_character2(s), output, "Testcase 1 Passed!")

    def testcase2(self):
        s = "loveleetcode"
        output = 2
        self.assertEqual(unique_character1(s), output, "Testcase 2 Passed!")
        self.assertEqual(unique_character2(s), output, "Testcase 2 Passed!")

    def testcase3(self):
        s = "aabb"
        output = -1
        self.assertEqual(unique_character1(s), output, "Testcase 3 Passed!")
        self.assertEqual(unique_character2(s), output, "Testcase 3 Passed!")
    print("All TestCase Passed!!")


if __name__ == "__main__":
    unittest.main()
