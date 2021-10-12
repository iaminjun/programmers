def num_of_greater(input_list, x):
    num = 0
    for a in input_list:
        if a > x:
            num+=1
    return num

def list_minus(input_list, x):
    for i in range(len(input_list)):
        input_list[i] -= x
    return input_list

def solution(citations):
    h_index = 0
    while True:
        if num_of_greater(citations, 0) <= h_index:
            break
        h_index += 1
        list_minus(citations,1)

    return h_index
