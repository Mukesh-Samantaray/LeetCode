class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Convert number to string
        x_str = str(x)
        # Check if string is same when reversed
        return x_str == x_str[::-1]

