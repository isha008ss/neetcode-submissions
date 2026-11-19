from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        lst = []
        for num, count in Counter(nums).most_common(k):
             lst.append(num)
        return lst
                