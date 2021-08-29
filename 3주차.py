from collections import deque

BOARD = 0
TABLE = 1
VISITED = 2

"""
Block이 있는 board/table의 좌표 찾기
"""
def find_block(array, kind):
    nbs = []
    N = len(array)
    for x in range(N):
        for y in range(N):
            if array[x][y] == kind:
                block_xy = bfs(array, x, y, kind)
                nbs.append(normalize_block(block_xy))
    return nbs


def bfs(array, x, y, kind):
    N = len(array)
    block_xy = []
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    q= deque()
    q.append((x,y))
    array[x][y] = VISITED
    block_xy.append((x,y))
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx<0 or nx>=N or ny<0 or ny>=N or array[nx][ny] != kind:
                continue
            else:
                q.append((nx,ny))
                array[nx][ny] = VISITED
                block_xy.append((nx, ny))
    return block_xy


"""
Block을 포함하는 최소의 직사각 배열을 만들고
좌표를 0,0부터 시작하도록 변환
"""
def normalize_block(block):
    block.sort(key=lambda x:x[1])
    min_c = block[0][1]
    nb_len_c= block[-1][1] - block[0][1] + 1
    block.sort()
    min_r = block[0][0]
    nb_len_r = block[-1][0] - block[0][0] + 1
    nb = [[0] * nb_len_c for _ in range(nb_len_r)]
    for r,c in block:
        nb[r-min_r][c-min_c] = 1
    return nb


"""
2차원 직사각 배열 90도 회전
"""
def block_rotate(array):    # 직사각 행렬에 의해서 돌려야함
    N = len(array)          # row 의 개수 -> 변환 행렬의 col개수
    M = len(array[0])       # col의 개수 -> 변환 행렬의 row 개수
    ret = [[0] * N for _ in range(M)]
    ret_c_s = N-1           #ret column start

    for arrs in array: 
        i = 0
        for arr in arrs:
            ret[i][ret_c_s] = arr
            i += 1
        ret_c_s -= 1
        
    return ret


"""
2차원 직사각 배열을 0도 90도 180도 270도 회전한 결과 출력
"""
def block_rotate_alldegree(array):   
    N = len(array)
    M = len(array[0])
    result = []

    array_90 = [[0] * N for _ in range(M)]
    array_180 = [[0] * M for _ in range(N)]
    array_270 = [[0] * N for _ in range(M)]
    
    array_90 = block_rotate(array)
    array_180 = block_rotate(array_90)
    array_270 = block_rotate(array_180)
    
    result.append(array)
    result.append(array_90)
    result.append(array_180)
    result.append(array_270)
    
    return result
    
"""
2차원 배열 합구하기 : Block의 칸수 구하기 위해 사용
"""    
def sum_array(array):
    res = 0
    for a in array:
        res += sum(a)
    return res
    
        

def solution(game_board, table):
    answer = 0
    board_array = find_block(game_board, BOARD)
    table_array = find_block(table, TABLE)
    
    
    for board_block in board_array:
        for table_block in table_array:
            if board_block in block_rotate_alldegree(table_block):
                answer += sum_array(board_block)
                table_array.remove(table_block)
                break
                
    return answer
