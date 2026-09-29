class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h=dict()
        for val in strs:
            k="".join(sorted(val))
            if k in h.keys():
                h[k].append(val)
            else:
                h[k]=[val]
        return list(h.values())
            
        


        