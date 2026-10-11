class Solution:
    def encode(self, strs: List[str]) -> str:
            encoded_str = ""
            for word in strs:
                encoded_str+=str(len(word))+"#"+word
            return encoded_str

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < (len(s)):
            separator_index = s.index("#",i)
            length_in_question = s[i:separator_index]
            length_in_question =int(length_in_question)
            res.append(s[separator_index+1 : separator_index+length_in_question+1])
            i = length_in_question+separator_index+1
        return res