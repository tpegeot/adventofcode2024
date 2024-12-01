#!/usr/bin/env python

""" Advent of code 2024 - part1 """

import pandas as pd

def read_input():
    _data = pd.read_csv('input/day1',
                       header=None,
                       sep=r'\s+',
                       names=['list1', 'list2'],
                       usecols=[0,1])
    return _data


def part1(_data):
    """
    Part 1
    """
    print("# Day 1 - part 1")
    list1 = sorted(list(_data['list1']))
    list2 = sorted(list(_data['list2']))
    distances = [ value_list2-value_list1 if value_list2>=value_list1 else value_list1-value_list2 for (value_list1, value_list2) in zip(list1, list2) ]
    return sum(distances)


def part2(_data):
    """
    Part 2
    """
    left = list(_data['list1'])
    right = list(_data['list2'])
    similarity_score = sum([ number * right.count(number) for number in left])
    return similarity_score
def main():
    """
    Main function
    """
    data = read_input()
    print(part1(data))
    print(part2(data))


if __name__ == "__main__":
    main()
