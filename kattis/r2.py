from sys import stdin, stdout

class Solution:
    def solve(self):
        data = stdin.readline().split()

        r1 = int(data[0])
        s = int(data[1])

        answer = (s* 2) - r1

        print(answer)



if __name__ == "__main__":
    solution = Solution()

    solution.solve()