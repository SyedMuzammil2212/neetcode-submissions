class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return "empty"
        a=""
        j=len(strs)
        for i in range(0,j):
            if i==j-1:
                a=a+strs[i]
            else:
                a=a+strs[i]+"."
        return a

    def decode(self, s: str) -> List[str]:
        if(s == "empty"):
            return []
        return s.split(".")

