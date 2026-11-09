def average(nums):
    if not nums:
        raise ValueError("empty")
    return sum(nums) / len(nums)


def read_config(path):
    with open(path, encoding="utf-8") as f:
        return f.read()
