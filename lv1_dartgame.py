def solution(dartResult):
    num1 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    score =[] 
    num = 0

    for a in range(len(dartResult)):
        if dartResult[a] in num1:
            dr = dartResult[a]
            if dartResult[a] == '1':
                if dartResult[a+1] == '0':
                    dr = '10'
            elif dartResult[a] == '0':
                if a -1 > =0 and dartResult[a-1] == '1':
                    continue
            num += 1
            score.append(int(dr))
        elif dartResult[a] == 'D':
            score[num-1] = score[num-1] ** 2
        elif dartResult[a] == 'T':
            score[num-1] = score[num-1] ** 3
        elif dartResult[a] == '#':
            score[num-1] = score[num-1] * (-1)
        elif dartResult[a] == '*':
            score[num-1] = score[num-1] * 2
            if num - 2 >= 0:
                score[num-2] = score[num-2] * 2

    answer = sum(score)
    return answer
