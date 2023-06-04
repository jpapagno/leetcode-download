import Arrays
import bisect
import collections
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i, cur in enumerate(nums):
            if target-cur in map:
                return [map[target-cur], i]
            map[cur] = i