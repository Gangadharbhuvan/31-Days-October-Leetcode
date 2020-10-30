'''
    Given an integer array nums, return the number of longest increasing subsequences.

 

Example 1:

Input: nums = [1,3,5,4,7]
Output: 2
Explanation: The two longest increasing subsequences are [1, 3, 4, 7] and [1, 3, 5, 7].
Example 2:

Input: nums = [2,2,2,2,2]
Output: 5
Explanation: The length of longest continuous increasing subsequence is 1, and there are 5 subsequences' length is 1, so output 5.

 

Constraints:

0 <= nums.length <= 2000
-106 <= nums[i] <= 106


'''

class Solution:
    def findNumberOfLIS(self, nums):
        dp = collections.defaultdict(collections.Counter)
        dp[-1][-1e9] = 1
        table = []
        for i in nums:
            index = bisect.bisect_left(table, i)
            if index == len(table):
                table.append(i)
            else:
                table[index] = i 
            dp[index][i] += sum(dp[index-1][j] for j in dp[index-1] if j < i)
        return sum(dp[max(0, len(table)-1)].values()) 