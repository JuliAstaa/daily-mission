"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
 

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums contains distinct values sorted in ascending order.
-104 <= target <= 104
"""

def search_insert(nums: list[int], target: int) -> int:
    low: int = 0
    high: int = len(nums) - 1

    while low <= high:
        mid: int = (low + high) // 2

        if nums[mid] == target:
            return mid
        elif target < nums[mid]:
            high = mid -1
        elif target > nums[mid]:
            low = mid + 1
    
    return low


nums = [1,3,5,6]
target = 7
print(search_insert(nums=nums, target=target))

