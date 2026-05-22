class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        # iterate through the array
        for idx, val in enumerate(nums):
            # check if difference exists in the hash map
            diff = target - nums[idx]
            if diff in hashMap:
                return [hashMap[diff], idx]
            # else store the current element in the hashmap with its index
            hashMap[val] = idx 