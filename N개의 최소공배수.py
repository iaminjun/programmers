from collections import deque
def gcd(a,b):
    if a < b:
        a, b = b, a

    while b>0:
        temp = a%b
        a = b
        b = temp
    return a

def lcm(a,b):
    return int((a * b) / gcd(a,b))

def solution(arr):
    q = deque(arr)
    while len(q) > 1:
        temp = lcm(q.popleft(),q.popleft())
        q.append(temp)

    return q[0]
