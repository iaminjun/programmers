def solution(scores):
    answer = ''
    score = 0
    tables = list(zip(*scores))
    
    idx = 0
    for table in tables:
        if max(table) == table[idx] and table.count(table[idx]) == 1:
            score = (sum(table) - table[idx]) / (len(table)-1)
        elif min(table) == table[idx] and table.count(table[idx]) == 1:
            score = (sum(table) - table[idx]) / (len(table)-1)
        else:
            score = sum(table) / len(table)
        idx += 1
    
        if score >= 90:
             answer += 'A'
        elif 80 <= score < 90:
            answer += 'B'
        elif 70 <= score < 80:
            answer += 'C'
        elif 50 <= score < 70:
            answer += 'D'
        else:
            answer += 'F'
            
    return answer
