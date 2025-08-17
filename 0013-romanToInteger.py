class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        for i in range(len(s)):
            if i+1 < len(s):
                if s[i] == "I" and (s[i+1] == "V" or s[i+1] == "X"):
                    count -= 1
                    continue
                elif s[i] == "X" and (s[i+1] == "L" or s[i+1] == "C"):
                    count -= 10
                    continue
                elif s[i] == "C" and (s[i+1] == "D" or s[i+1] == "M"):
                    count -= 100
                    continue
                    
            if s[i] == "I":
                count += 1
            elif s[i] == "V":
                count += 5
            elif s[i] == "X":
                count += 10
            elif s[i] == "L":
                count += 50
            elif s[i] == "C":
                count += 100
            elif s[i] == "D":
                count += 500
            elif s[i] == "M":
                count += 1000
        
        return count
