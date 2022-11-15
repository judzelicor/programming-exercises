class Solution:
    """
    @nums - a list of integers
    @k - an integer
    """
    def solve(self, nums, k):
        numsMap = {}
        numsFrequency = [[] for i in range(len(nums) + 1)]

        for num in nums:
            numsMap[num] = numsMap.get(num, 0) + 1

        for num, freq in numsMap.items():
            numsFrequency[freq].append(num)

        answer = []

        for i in range(len(numsFrequency) - 1, 0, -1):
            for j in numsFrequency[i]:
                if (len(answer) <= k):
                    answer.append(j)

        return answer


solution = Solution()

solution.solve([1,2,2,2,3,4,4,5], 2)