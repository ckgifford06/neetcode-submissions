class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for item in strs:
            encoded_string = encoded_string + item
            encoded_string = encoded_string + "é"
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_strs = s.split("é")
        return decoded_strs[:-1]