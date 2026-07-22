class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            listS = list(s)
            listT = list(t)

            sortedListA = sorted(listS)
            sortedListT = sorted(listT)

            if sortedListA == sortedListT:
                return True
            else:
                return False