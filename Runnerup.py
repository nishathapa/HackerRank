# n = int(input())
# arr = list(map(int, input().split()))
# list.sort(arr)
# print(arr[2])

if __name__ == '__main__':
    n = int(input())
    a = map(int, input().split())
    b = set(a)
    d = list(b)
    d.sort()
    print(d[-2])
