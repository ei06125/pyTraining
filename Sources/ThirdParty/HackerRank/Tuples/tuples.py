from builtins import hash

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    t = tuple(integer_list)
    res = hash(t)
    print(res)
    