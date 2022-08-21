class Solution:
    def rob(self, nums: List[int]) -> int:
        num_house = len(nums)
        if num_house == 1:
            return nums[0]
        elif num_house == 2:
            if nums[0] < nums[1]:
                return nums[1]
            else:
                return nums[0]
        else:
            max_rob = [-1 for _ in range(num_house)]
            max_rob[0] = nums[0]
            if nums[0] < nums[1]:
                max_rob[1] = nums[1]
            else:
                max_rob[1] = nums[0]

            for i in range(2, num_house):
                rob_this = max_rob[i-2] + nums[i]

                if max_rob[i-1] < rob_this:
                    max_rob[i] = rob_this
                else:
                    max_rob[i] = max_rob[i-1]

            return max_rob[-1]