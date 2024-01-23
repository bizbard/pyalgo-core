from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 1. 暴力法
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]

        # 2. 哈希表
        # hash_table = {}
        # for i, num in enumerate(nums):
        #     if target - num in hash_table:
        #         return [hash_table[target - num], i]
        #     hash_table[num] = i

        # 3. 一遍哈希表
        hash_table = {}
        for i, num in enumerate(nums):
            if target - num in hash_table:
                return [hash_table[target - num], i]
            hash_table[num] = i


nums = [2,7,11,15]
target = 9
sol = Solution()
print(sol.twoSum(nums, target))

