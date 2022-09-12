class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        score = 0
        up_idx = 0
        down_idx = len(tokens)-1
        max_score = 0
        tokens.sort()
        while up_idx <= down_idx:
            if tokens[up_idx] <= power:
                power -= tokens[up_idx]
                score += 1
                up_idx += 1
            elif score > 0:
                power += tokens[down_idx]
                score -= 1
                down_idx -= 1
            else:
                break
                
            max_score = max(max_score, score)
                
        return max_score
                