# read a file line by line
def read_file(filename):
    lines = []
    with open(filename) as f:
        for line in f:
            lines.append(line.strip())
    return lines


nums = read_file('./input/day1.txt')
nums = [int(num) for num in nums]


def get_increases(nums):
    increases = 0
    prev = nums[0]
    for num in nums[1:]:
        if num > prev:
            increases += 1
        prev = num
    return increases


def sliding_window(nums):
    increases = 0
    prev = nums[0] + nums[1] + nums[2]
    for i in range(1, len(nums) - 2):
        sum = nums[i] + nums[i+1] + nums[i+2]
        if sum > prev:
            increases += 1
        prev = sum
    return increases


if __name__ == '__main__':
    print(get_increases(nums))
    print(sliding_window(nums))
