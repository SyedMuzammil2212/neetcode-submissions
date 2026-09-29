class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h=dict()
        for index,val in enumerate(nums):
            k=target-val
            if k in h.keys():
                return [h[k],index]
                break
            else:
                h[val]=index
            


        