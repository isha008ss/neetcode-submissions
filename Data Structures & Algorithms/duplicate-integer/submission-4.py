class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        copy= set()
        for num in nums:
            if num in copy:
                return True
            copy.add(num)
        return False
    
