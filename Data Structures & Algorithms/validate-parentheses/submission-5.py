class Solution:
    def isValid(self, s: str) -> bool:
        s = list(s)
        stack = []
        p_dict = {
            "}": "{",
            "]": "[",
            ")": "("
        }

        if len(s) == 1 or len(s) % 2 == 1:
            return False

        for i in range(0, len(s)):
            if s[i] == "{" or s[i] == "[" or s[i] == "(":
                stack.append(s[i])
            elif s[i] == "}" or s[i] == "]" or s[i] == ")": 
                if not stack or p_dict[s[i]] != stack[-1]:
                    return False
                stack.pop()
        if not stack:
            return True
        else:
            return False
