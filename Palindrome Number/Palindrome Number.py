class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        a = str(x)
        reverse = a[::-1]
        m = int(reverse)
        if m == x:
            return True
        else:
            return False
