def solution(n):
    answer = 1
    

    x = n // 2
    start = x
    if n > 1 and (n % 2 != 0):
        answer += 1

        
    while True:
        nn = n
        for i in range(start, 0, -1):
            nn -= i
            if nn == 0:
                answer += 1
                break
            elif nn < 0: break
        start -= 1
        if start < 0: break
            
    return answer
