class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_Count = 0 
        current_Count = 0 
        for i in nums:
            if i == 1:
                current_Count +=1
                if current_Count > max_Count:
                    max_Count = current_Count
            else:
                    current_Count = 0 
        return max_Count
        