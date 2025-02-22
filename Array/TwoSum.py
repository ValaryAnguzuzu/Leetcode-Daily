# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

 

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]

#Brute Force: check every combination and see if it sums up to our target; complexity - O(n^2)
#Optimal sol:
   # Hashmap
   #for each num, the val we are looking for is diff = target - num
   #map each val to its index and check if diff exixts in hashmap
   #return the indices of diff and num


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        Approach: Hash Map  
        Optimal Complexity: O(n) time, O(n) space  

        """
        HashMap = {}
        for i, val in enumerate(nums):
            diff = target - val
            if diff in HashMap:
                return [HashMap[diff], i]
            HashMap[val] = i
        return

if __name__ == "__main__":
    solution = Solution()
    print(solution.twoSum([2, 7, 11, 15], 9))  # Output: [0, 1]
    print(solution.twoSum([3, 2, 4], 6))       # Output: [1, 2]
    print(solution.twoSum([3, 3], 6))          # Output: [0, 1]
