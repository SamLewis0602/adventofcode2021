from day1 import read_file

moves = read_file('input/day2.txt')


def part1():
    depth = 0
    position = 0
    for move in moves:
        direction, distance = move.split(' ')
        distance = int(distance)
        if direction == 'down':
            depth += distance
        elif direction == 'up':
            depth -= distance
        else:
            position += distance
    return position * depth


def part2():
    depth = 0
    position = 0
    aim = 0
    for move in moves:
        direction, distance = move.split(' ')
        distance = int(distance)
        if direction == 'down':
            aim += distance
        elif direction == 'up':
            aim -= distance
        else:
            position += distance
            depth += distance * aim
    return depth * position


print(part1())
print(part2())
