#6x6 가로모형 테트리스(?)	
# implementation	
# Silver IV

def solution(param0):
    # 가로 좌표: 2차원 위치
    # 세로 좌표: 1차원 위치
    # 즉, 맵[x][y]=맵[세로][가로]
    BLOCK_WIDTH = 6
    BLOCK_HEIGHT = 6

    # init board
    maps = []
    for _ in range(BLOCK_HEIGHT):
        maps.append([0, 0, 0, 0, 0, 0]) # BLOCK_WIDTH

    index = 0
    while index < len(param0):
        cols = param0[index]
        rows = param0[index+1]
        length = param0[index+2]
        index += 3

        # if block already filled
        if sum(maps[rows][cols:cols+length]) > 0:
            return []

        # if block went out of the map
        if cols + length - 1 >= BLOCK_WIDTH:
            return []

        # set blocks
        for value in range(length):
            maps[rows][cols+value] = value+1

        # if sum of column equals 10
        for col_index in range(BLOCK_WIDTH):
            sum_of_column = sum([maps[x][col_index] for x in range(BLOCK_HEIGHT)])
            # remove column blocks
            if sum_of_column == 10:
                for x in range(BLOCK_HEIGHT):
                    maps[x][col_index] = 0

    answer = []
    for m in maps:
        row = "".join([str(x) for x in m]).replace("0", " ")
        answer.append(row)

    return answer
#2차원 배열 평면의 셀들을 다루는 문제였는데 테스트 케이스를 작성하기도 까다로워서 
#주어진 것에 구현하기 쉬운 테스트 케이스만 몇 개 추가해서 돌려보고 넘어갔던 것 같다.