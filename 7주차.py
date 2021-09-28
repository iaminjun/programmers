from collections import deque
def solution(enter, leave):
    answer = [0] * (len(enter) + 1)
    meet = [0] * (len(enter) + 1) # 인덱스에 편하게 접근하기 위해 +1 해줌
    # 최악으로 못만날때를 가정해서 푼다
    # -> 나갈 수 있는 사람이 있으면 다 나간다

    enter = deque(enter)
    leave = deque(leave)
    # enter : meet idx 1로
    while enter:
        # enter시 sum(meet) 이 1 이상이면 다음에 누가들어오면 만남을 가짐
        if sum(meet) >= 1:
            for i in range(1,len(meet)):
                if meet[i]:
                    answer[i] += 1
            answer[enter[0]] += sum(meet)
        meet[enter[0]] = 1
        enter.popleft()

        # leave
        # leave할 수 있는 사람이 있으면 다 나가기
        while leave:
            if meet[leave[0]] == 1:
                meet[leave[0]] = 0
                leave.popleft()
            else:
                break

    answer = answer[1:]
    return answer
