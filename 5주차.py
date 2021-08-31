def solution(word):
    answer = 0
    char = ['A', 'E', 'I', 'O', 'U']
    index = [0, 1, 2, 3, 4]
    temp = [5**i for i in reversed(range(5))]
    offset = [sum(temp), sum(temp[1:]), sum(temp[2:]), sum(temp[3:]), sum(temp[4:])]
    index_dict = dict(zip(char,index))

    idx = 0
    for w in word:
        answer += (index_dict[w] * offset[idx]) + 1
        idx += 1
        

    return answer
