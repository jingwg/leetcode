class Solution:
    def numDecodings(self, s: str) -> int:
        stored_list = [0] * (len(s)+1)
        stored_list[0] = 1
        if s[0] == '0':
            stored_list[1] = 0
        else:
            stored_list[1] = 1
        for i in range(2,len(s) +1):
            if 1<= int(s[i-1]) <= 9:
                stored_list[i] += stored_list[i - 1]
            if 10 <= int(s[i-2:i]) <= 26:
                stored_list[i] += stored_list[i - 2]
        return stored_list[len(s)]
