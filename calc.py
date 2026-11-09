def average(nums):
    total = 0
    for n in nums:
        total += n
    return total / len(nums)


def read_config(path):
    f = open(path)
    return f.read()
