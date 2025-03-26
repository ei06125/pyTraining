from __builtins__ import hash

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    res = hash(integer_list)
    