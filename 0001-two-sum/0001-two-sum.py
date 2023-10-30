class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            i_val = nums[i]
            for j in range(i+1,len(nums)):
                j_val = nums[j]
                if i_val + j_val == target:
                    out_put = [i, j]
                    return out_put
        