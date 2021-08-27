def solution(table, languages, preference):
    table_score = [0, 5, 4, 3, 2, 1]
    lan_pre = dict(zip(languages,preference))
    result = {}
    #print(lan_pre)
    
    for lans in table:
        score = 0
        lans = list(map(str,lans.split(' ')))
        #print(lans)
        for i in range(1,6):
            if lans[i] in lan_pre:
                score += lan_pre[lans[i]] * table_score[i]
        result[lans[0]] = score
    
    result = sorted(result.items(), key = lambda x:(-x[1],x[0]))
            

    answer = result[0][0]
    return answer
