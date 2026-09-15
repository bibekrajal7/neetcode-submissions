class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxCount = 0 
        currentCount = 0
        
        for i in nums:
            if i == 1:
                currentCount += 1
                if currentCount > maxCount:
                    maxCount = currentCount
            else:
                currentCount = 0
        return maxCount