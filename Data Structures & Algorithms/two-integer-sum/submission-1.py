class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {} # val -> index

        for idx, value in enumerate(nums):
            complement = target - nums[idx]
            if complement in hashMap and hashMap[complement] != idx:
                return [hashMap[complement], idx]
            hashMap[value] = idx
        return
