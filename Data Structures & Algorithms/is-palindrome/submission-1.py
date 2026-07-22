class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphabet = "abcdefghijklmnopqrstuvwxyz0123456789"
        
        s = s.lower()
        for char in s:
            if char not in alphabet:
                s = s.replace(char, "")
        print(s)

        lenOfS = len(s)

        for i in range(0, lenOfS):
            if s[i] == s[lenOfS - i - 1]:
                continue
            else:
                return False
        return True