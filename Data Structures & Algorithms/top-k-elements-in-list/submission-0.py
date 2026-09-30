class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_dict = {}
        for n in nums:
            nums_dict[n] = nums_dict.get(n, 0) + 1

        sorted_nums = sorted(nums_dict, key=nums_dict.get, reverse=True)
        return sorted_nums[:k]
        