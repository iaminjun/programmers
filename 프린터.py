from collections import deque
def solution(priorities, location):
    order = deque([i for i in range(len(priorities))])
    result = []
    q = deque(priorities)

    while q:
        if q[0] == max(q):
            q.popleft()
            result.append(order.popleft())
        else:
            q.append(q.popleft())
            order.append(order.popleft())

    return result.index(location)+1
