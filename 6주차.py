def solution(weights, head2head):
    answer = []
    win_rate = []
    win_heavy = []
    table ={}
    
    len_match = len(head2head[0]) - 1
    len_player = len(weights)
    player = [i for i in range(1,len_player+1)]
    # 승률 구하기 + 자기자신보다 무거운 사람 이긴 횟수
    for i in range(len_player):
        win = 0
        w = head2head[i].count("W")
        l = head2head[i].count("L")
        if w+l > 0:
            win_rate.append(w / (w + l))
        else:
            win_rate.append(0)
        for j in range(len_match +1):
            if head2head[i][j] == 'W' and weights[j] > weights[i]:
                win += 1
        win_heavy.append(win)
        
    table = list(zip(win_rate, win_heavy, weights, player))
    table.sort(key= lambda x : (-x[0],-x[1],-x[2],x[3]))
    
    for a, b, c, d in table:
        answer.append(d)
    


    return answer
