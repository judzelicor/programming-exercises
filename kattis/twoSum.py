from sys import stdin, stdout

class Solution:
    def solve(self):
        sum = 0

        data = stdin.readline().split()

        for datum in data:
            sum += int(datum)

        print(sum)


if __name__ == "__main__":
    solution = Solution()

    solution.solve()