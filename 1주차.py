def solution(price, money, count):
    answer = -1

    answer = max(0,price * (count * (count +1))/2 - money)    
    return answer
