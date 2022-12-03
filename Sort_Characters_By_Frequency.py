from heapq import heappush, heappop
class Solution:
    def frequencySort(self, s: str) -> str:
        ascii_a = 97
        small_list = [0 for _ in range(26)]
        big_list = [0 for _ in range(26)]
        num_list = [0 for _ in range(10)]

        for al in s:
            ord_al = ord(al)
            if 65<=ord_al<=90:
                big_list[ord_al-65] += 1
            elif 48<=ord_al<=57:
                num_list[ord_al-48] += 1
            else:
                small_list[ord_al-ascii_a] += 1

        hq = []
        for i, cnt in enumerate(big_list):
            if cnt > 0:
                heappush(hq, (-cnt, chr(i+65)))

        for i, cnt in enumerate(small_list):
            if cnt > 0:
                heappush(hq, (-cnt, chr(i+ascii_a)))

        for i, cnt in enumerate(num_list):
            if cnt > 0:
                heappush(hq, (-cnt, chr(i+48)))


        ans = ''
        while hq:
            cnt, letter = heappop(hq)
            ans += (letter * (-cnt))

        return ans
