class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h=dict()
        for val in nums:
            if val in h:
                h[val]+=1
            else:
                h[val]=1
        result = heapq.nlargest(
            k,
            h,
            key=h.get
        )
        return result


        
        
        