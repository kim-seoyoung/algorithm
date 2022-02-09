class Solution:
    cnt = 0
    def recurr(self, s, N, st, dp):
        if st >= N:
            return 1
        
        for n in range(0,min(N-st,2)):
            # print(st)
            now = s[:n+1]
            # print('now', now)
            if now[0] == "0" or int(now) < 1 or int(now) > 26:
                continue
            if not dp[st][1]:
                next_ = s[n+1:]
                # print('next', next_)
                ret = self.recurr(next_, N, st+n+1, dp)
                dp[st][0] += ret
                
        if not dp[st][1]:
            dp[st][1] = True
            
        # print('return', dp[st][0])
        return dp[st][0]
            
        
    
    def numDecodings(self, s: str) -> int:
        len_ = len(s)
        
        dp = [[0, False] for _ in range(len_+1)]
        
        self.recurr(s + ' ', len_, 0, dp)
        # print(dp)
        
        return dp[0][0]