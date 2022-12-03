from collections import Counter
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        dist1 = [0 for _ in range(26)]
        dist2 = [0 for _ in range(26)]

        for w in word1:
            dist1[ord(w)-97] += 1
        for w in word2:
            dist2[ord(w)-97] += 1

        for i in range(26):
            if (dist1[i] > 0 and dist2[i] == 0) or (dist1[i] == 0 and dist2[i] > 0):
                return False
        
        cnt1 = Counter(dist1)
        cnt2 = Counter(dist2)
        
        if cnt1 == cnt2:
            return True
        else:
            return False
