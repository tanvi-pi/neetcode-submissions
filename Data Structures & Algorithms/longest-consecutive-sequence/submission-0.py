class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set(nums)
        longest = 0

        for val in numbers:
            if val - 1 not in numbers:
                length = 1
                curr = val
                while curr + 1 in numbers:
                    length = length + 1
                    curr +=1
                
                longest = max(longest, length)
        return longest