from sys import stdin, stdout

text = stdin.readline()

class Solution:
    def solve(self, text):
        wordCount = text.count(" ") + 1
        stdout.write(str(wordCount) + "\n")

solution = Solution()

solution.solve(text)
