def solution(s):
    answer = ''
    temp =[]
    for ss in s:
        temp.append(ss)
    temp.sort(reverse = True)
    
    for t in temp:
        answer += t

    return answer
