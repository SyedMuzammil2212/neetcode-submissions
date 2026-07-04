class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        check={}
        for item in strs:
            word="".join(sorted(item))
            if word in check:
                check[word].append(item)
            else:
                check[word]=[item]
        return list(check.values())
            
        