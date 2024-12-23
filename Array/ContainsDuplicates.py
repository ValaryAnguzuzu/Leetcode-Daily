# 217. Contains Duplicate
# Given an integer array nums, return true if any value appears at least twice in the array, 
# and return false if every element is distinct.
# Example 1:

# Input: nums = [1,2,3,1]

# Output: true

# Explanation:

# The element 1 occurs at the indices 0 and 3.

# Example 2:

# Input: nums = [1,2,3,4]

# Output: false

# Explanation:

# All elements are distinct.

# Example 3:

# Input: nums = [1,1,1,3,3,4,3,2,4,2]

# Output: true

 

# Constraints:

# 1 <= nums.length <= 105
# -109 <= nums[i] <= 109

#Hashset
#iterate and check if val exists in hashset, if yes return true, if no add it to hashset
#return fals otherwise

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hashset = set()
        for num in nums:
            if num in hashset:
                return True
            hashset.add(num)
        return False

if __name__ == "__main__":
    solution = Solution()
    print(solution.containsDuplicate([1,2,3,1]))  # Output: true
    print(solution.containsDuplicate([1,2,3,4]))       # Output: false
    print(solution.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))       # Output: true



