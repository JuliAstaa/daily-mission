"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true

Example 5:

Input: s = "([)]"

Output: false

 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.


link: [https://leetcode.com/problems/valid-parentheses/description/]
"""


def is_valid_parentheses(s:str) -> bool:
    pairs: dict = {")": "(", "}": "{", "]": "["}
    
    stack: list[str] = []

    for char in s:
        if char in pairs.values():
            stack.append(char)
        
        elif char in pairs:
            if not stack or stack[-1] != pairs[char]:
                return False

            stack.pop()
        
    return len(stack) == 0

print(is_valid_parentheses("()"))