"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters if it is non-empty.


link: [https://leetcode.com/problems/longest-common-prefix/description/]

"""

def longestCommonPrefix(strs: list[str]) -> str:
    if not strs:
        return ""

    prefix = strs[0]
    i = 0

    while i < len(prefix):
        for s in strs[1:]:
            if i >= len(s) or prefix[i] != s[i]:
                return prefix[:i]
        i += 1

    return prefix


# test
print(longestCommonPrefix(["flower","flow","flight"]))
print(longestCommonPrefix(["dog","racecar","car"]))
