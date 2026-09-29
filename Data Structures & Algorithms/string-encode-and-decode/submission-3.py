class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs)==0:
            return "none"
        else:
            return "|*|*".join(strs)

    def decode(self, s: str) -> List[str]:
        if s=="none":
            return []
        else:
            return s.split("|*|*")
