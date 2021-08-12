def solution(s):
    answer = ''
    temps = s.split(' ')
    
    for temp in temps:
        for i in range(len(temp)):
            if i % 2 == 0:
                answer += temp[i].upper()
            else:
                answer += temp[i].lower()
        answer += ' '
    answer = answer[:-1]
    return answer
