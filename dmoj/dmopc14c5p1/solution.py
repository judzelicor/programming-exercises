from sys import stdin, stdout
from math import pi

class Solution:
    def solve(self, radius, height):
        V = (pi * (radius ** 2) * height) / 3
        stdout.write("{:.2f}".format(V).format() + '\n')

r = int(stdin.readline().strip())

h = int(stdin.readline().strip())

solution = Solution()

solution.solve(r, h)