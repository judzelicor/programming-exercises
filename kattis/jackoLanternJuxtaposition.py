from sys import stdin, stdout

class Solution:
    def solve(self):
        combinations = 1

        data = stdin.readline().split()

        for datum in data:
            combinations *= int(datum)

        print(combinations)


if __name__ == "__main__":
    solution = Solution()

    solution.solve()