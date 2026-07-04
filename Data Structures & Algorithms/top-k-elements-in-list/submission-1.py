class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        check={}
        for index,item in enumerate(nums):
            if(item in check):
                check[item]+=1
            else:
                check[item]=1
        a=sorted(check.values(),reverse=True)[:k]
        result=[]
        for key in check:
            if check[key] in a:
                result.append(key)
        return result
        
        