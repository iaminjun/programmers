def solution(s):
    answer = ''
    aa = s.split(' ')

    for i in range(len(aa)):
        if aa[i] != '':
            aa[i] = aa[i][0].upper() + aa[i][1:].lower()

    answer = ' '.join(aa)
    return answer
