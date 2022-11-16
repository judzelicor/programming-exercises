from sys import stdin, stdout

class Solution:
    def solve(self):
        words = []

        wordsCount = int(stdin.readline())

        for i in range(wordsCount):
            words.append(input())

        for i in range(wordsCount):
            if ((i + 1) % 2 == 1):
                print(words[i])



if __name__ == "__main__":
    solution = Solution()

    solution.solve()