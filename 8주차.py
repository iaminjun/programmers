def solution(sizes):
    rows = []
    cols = []
    temp1 = 10000
    temp2 = 0
    for row, col in sizes:
        temp1 = min(row,col)
        temp2 = max(temp2 ,temp1)
        rows.append(row)
        cols.append(col)

    answer = max(rows+cols) * temp2
    return answer
