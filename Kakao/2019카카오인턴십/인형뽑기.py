# 게임 화면의 격자의 상태가 담긴 2차원 배열 board와 
# 인형을 집기 위해 크레인을 작동시킨 위치가 담긴 배열 moves가 매개변수로 주어질 때, 
# 크레인을 모두 작동시킨 후 터트려져 사라진 인형의 개수를 return 하도록 solution 함수를 완성해주세요.
def solution(board, moves):
    # board
    # [[0,0,0,0,0]
    # ,[0,0,1,0,3]
    # ,[0,2,5,0,1]
    # ,[4,2,4,4,2]
    # ,[3,5,1,3,1]]
    # use QUEUE_BOARD[COL_IDX].pop(0) to pull out
    # QUEUE_BOARD
    # {0:[4, 3]
    # ,1:[2, 2, 5]
    # ,2:[1, 5, 4, 1]
    # ,3:[4, 3]
    # ,4:[3, 1, 2, 1]}
    
    # INIT QUEUE_BOARD
    QUEUE_BOARD = {}
    for COL_IDX in range(len(board)):
        QUEUE_BOARD[COL_IDX] = []
        for ROW_IDX in range(len(board)):
            if board[ROW_IDX][COL_IDX] == 0:
                pass
            else:
                QUEUE_BOARD[COL_IDX].append(board[ROW_IDX][COL_IDX])
    # PULL OUT
    POP_DOLL_COUNT = 0
    BASKET = []
    for move in moves:
        COL_IDX = move - 1
        # CAN GET NEW_DOLL
        if 0 < len(QUEUE_BOARD[COL_IDX]):
            NEW_DOLL = QUEUE_BOARD[COL_IDX].pop(0)
            # BASKET EMPTY
            if len(BASKET) == 0:
                BASKET.append(NEW_DOLL)
            # BASKET NOT EMPTY
            else:
                # PREV == NEW
                if BASKET[-1] == NEW_DOLL:
                    BASKET.pop()
                    POP_DOLL_COUNT += 2
                # PREV != NEW
                else:
                    BASKET.append(NEW_DOLL)
        # CAN NOT GET NEW_DOLL
        else:
            pass
    return POP_DOLL_COUNT






print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))
# 4