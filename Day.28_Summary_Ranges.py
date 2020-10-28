class Solution(object):
    def summaryRanges(self, nums):
        if not nums: return []
        
        def create_interval(curr_start, curr_end):
            if curr_start == curr_end:
                return str(curr_start)
            else:
                return str(curr_start) + "->" + str(curr_end)
        
        curr_start = nums[0]
        curr_end = nums[0]
        
        res = []
        for i in range(1, len(nums)):
            if (curr_end == nums[i] - 1):
                curr_end += 1
            else:
                res.append(create_interval(curr_start, curr_end))
                # start a new session
                curr_start = nums[i]
                curr_end = nums[i]
                
        res.append(create_interval(curr_start, curr_end))
        return res
