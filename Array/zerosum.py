
     ##THE IDEA IS BASICALLY ON PREFIX SUM
     ##Compute the prefix sum then the trick is use a hashmap to track count of the psum...your 
     ##total sum would increase by however many times your psum occurs

# Problem Statement: Count Zero-Sum Subarrays
# Given an array of integers, find the number of subarrays (continuous subarrays) whose sum equals zero.
# Input:
# An array of integers nums of length n (1 ≤ n ≤ 10^5).
# The elements of nums can be negative, zero, or positive.
# Output:
# Return an integer representing the count of subarrays that sum to zero.
# Example 1:
# Input:
#  nums = [1, -1, 2, -2, 3, -3]
# Output:
#  3
# Explanation:
#  The zero-sum subarrays are:
# [1, -1]
# [2, -2]
# [3, -3]
# Example 2:
# Input:
#  nums = [0, 0, 0]
# Output:
#  6
# [4, 5, 2, -1, -3, -3, 4, 6, -7]  --> 
#[4,9,11,4, 7, 4, 0, 6, -1]
#[4,0,-4]
# Explanation:
#  The possible zero-sum subarrays are:
# [0] (each 0 individually)
# [0, 0] (each adjacent pair)
# [0, 0, 0] (the entire array)
# Constraints:
# The function should run efficiently in O(n) time complexity.

from collections import defaultdict
def ZeroSumSubarray(nums):



    #populate prefix subarray
    prefix_sum = [0] * len(nums)
    prefix_sum[0] = nums[0]

    for i in range(1,len(nums)):
        prefix_sum[i] = nums[i] + prefix_sum[i-1]

    zero_sums = 0
    sum_dict = defaultdict(int)

    for psum in prefix_sum:
        if psum == 0:
            zero_sums += 1
# [4, 5, 2, -1, -3, -3, 4, 6, -7]  --> 
#[4, 9 ,11, 10, 7,  4,  0, 6, -1]
        
        zero_sums += sum_dict[psum]
        sum_dict[psum] += 1

    return zero_sums

        



