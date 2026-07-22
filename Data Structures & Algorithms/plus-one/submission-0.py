class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digitsStr = ""
        for item in digits:
            digitsStr = digitsStr + str(item)
        
        digitsInt = int(digitsStr)
        digitsInt = digitsInt + 1

        digitsStr2 = str(digitsInt)

        output = []
        for char in digitsStr2:
            output.append(char)
        return output