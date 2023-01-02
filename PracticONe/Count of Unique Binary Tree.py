class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def count_trees(n):
    if n <= 1:
        return 1
    count = 0

    for i in range(1, n + 1):
        leftCount = count_trees(i - 1)
        rightCount = count_trees(n - i)
        count += leftCount * rightCount
    return count


def main():
    print("Total Trees: " + str(count_trees(2)))
    print("Total Trees: " + str(count_trees(3)))


main()
