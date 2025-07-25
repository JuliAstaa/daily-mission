"""
Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

Constraints:

-231 <= x <= 231 - 1
 

Follow up: Could you solve it without converting the integer to a string?

"""

def is_palindrome_number(x: int) -> bool:
    if x < 0 or (x % 10 == 0 and x != 0):
        return False
    
    reversed_number: int = 0
    while x > reversed_number:
        digit = x % 10
        reversed_number = reversed_number * 10 + digit
        x = x // 10
    
    return x == reversed_number or x == reversed_number // 10
