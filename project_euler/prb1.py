#!/usr/bin/python


def sum_multiple(d,x):
    return d * (x/d) * (1 + x/d)/2

def solve_problem1(boundry):
    sum = sum_multiple(3,boundry) + sum_multiple(5,boundry) - sum_multiple(15,boundry)
    return sum

def main():
    print solve_problem1(999)
    
if __name__ == '__main__':
    main()
