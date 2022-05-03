# P = 응시자
# 0 = 빈 테이블
# X = 파티션
# 응시자들끼리는 맨해튼 거리가 2 이하로 앉지 말아야 한다.
#   => 1인 경우는 바로 붙어앉는 경우
#   => 2인 경우는 대각선 or 한자리 띄어 앉는 경우 이다.
# 단 응시자가 앉아있는 자리 사이가 파티션으로 막혀있을 경우에는 허용한다.
#   => 파티션으로 막히는 경우는 대각선 or 한자리 띄어 앉는 경우만 허용
def solution(places):
    answer = []
    for place in places:
        answer.append(isgood([[i for i in row] for row in place]))
    return answer

# Good = 1, Bad = 0
def isgood(room):
    for row_idx in range(5):
        for col_idx in range(5):
            if room[row_idx][col_idx] == "P":
                if in2range(room, row_idx, col_idx) == True:
                    return 0
    return 1

# Good = False, Bad = True
def in2range(room, row_idx, col_idx):
    floods = [[row_idx, col_idx]]
    for depth in range(2):
        print(depth)
        floods_buff = []
        # 모든칸 사방에 대해 확장
        for flood in floods:
            dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
            for dir in dirs:
                new_axis = [flood[0]+dir[0], flood[1]+dir[1]]
                # 새로운 칸이 range 안에 들어오고
                if new_axis[0] in range(5) and new_axis[1] in range(5):
                    # 탐사되지 않았던 지역임
                    if new_axis not in floods:
                        if room[new_axis[0]][new_axis[1]] == "P":
                            return True
                        elif room[new_axis[0]][new_axis[1]] == "O":
                            floods_buff.append(new_axis)
                        elif room[new_axis[0]][new_axis[1]] == "X":
                            pass
        floods += floods_buff
    return False

places =   [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], 
            ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], 
            ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], 
            ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], 
            ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]

print(solution(places))