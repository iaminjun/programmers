def solution(s):
    answer = []
    s = s.replace('{{','').replace('}}','').split('},{')
    s = sorted(s, key=len)

    for t in s:
        temps = t.split(',')
        for temp in temps:
            if int(temp) not in answer:
                answer.append(int(temp))
    return answer
