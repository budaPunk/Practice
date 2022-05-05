# PREV, CURR, NEXT
# 직선(P-C or C-N) = 100, 코너(P-C-N) = 500
from copy import deepcopy

def solution(board):
    board[0][0] = 1
    construct(len(board), [0, 0], board, [0, 0], 0)
    for line in board:
        print(line)
    print("===============================")
    return board[len(board) - 1][len(board) - 1]

# GOOD
def construct(board_size, curr_cord, board, prev_dir, price):
    #print(board_size, curr_cord, prev_dir, price)
    #for line in board:
    #    print(line)
    #print("===============================")
    #input()
    # if at end
    if curr_cord == [board_size - 1, board_size - 1]:
        pass
    else:
        # 현제 이미 더 최적화 된 방법으로 도달하는 방법이 있을 경우.
        # [[0, 0, 0, 0, 0, 0, 0, 0], 
        #  [1, 0, 1, 1, 1, 1, 1, 0], 
        #  [1, 0, 0, 1, 0, 0, 0, 0], 
        #  [1, 1, 0, 0, 0, 1, 1, 1], 
        #  [1, 1, 1, 1, 0, 0, 0, 0], 
        #  [1, 1, 1, 1, 1, 1, 1, 0], 
        #  [1, 1, 1, 1, 1, 1, 1, 0], 
        #  [1, 1, 1, 1, 1, 1, 1, 0]]
        # 500 
        if board[curr_cord[0]][curr_cord[1]] + 400 < price:
            pass
        # 내가 가장 최적화된 방법으로 해당 칸에 도착했을 경우
        else:
            # move 4 dirs
            dirs = [[1,0],[0,1],[-1,0],[0,-1]]
            for dir in dirs:
                new_cord = [curr_cord[0] + dir[0], curr_cord[1] + dir[1]]
                # in range
                if new_cord[0] in range(board_size) and new_cord[1] in range(board_size):
                    # is wall
                    if board[new_cord[0]][new_cord[1]] == 1:
                        pass
                    # not wall
                    else:
                        new_price = None
                        if prev_dir == [0, 0]:
                            new_price = price + 100
                        elif prev_dir == dir:
                            new_price = price + 100
                        else:
                            new_price = price + 100 + 500
                        # not visited
                        old_price = board[new_cord[0]][new_cord[1]]
                        if 0 == old_price:
                            board[new_cord[0]][new_cord[1]] = new_price
                            construct(board_size, new_cord, board, dir, new_price)
                        # already visited
                        else:
                            # im more efficient
                            if new_price < old_price:
                                board[new_cord[0]][new_cord[1]] = new_price
                                construct(board_size, new_cord, board, dir, new_price)
                            # im less efficient but can be more efficient next time
                            elif new_price < old_price + 400:
                                construct(board_size, new_cord, board, dir, new_price)
                            # im less efficient and no way of catching up
                            else:
                                pass

# NOTGOOD
def construct2(board_size, curr_cord, curr_board, prev_dir, price):
    #print(board_size, curr_cord, prev_dir, price)
    #for line in curr_board:
    #    print(line)
    #print("===============================")
    #input()
    # if at end
    if curr_cord == [board_size - 1, board_size - 1]:
        return price
    
    prices = [float("inf")]
    # move 4 dirs
    dirs = [[1,0],[0,1],[-1,0],[0,-1]]
    for dir in dirs:
        new_board = deepcopy(curr_board)
        new_cord = [curr_cord[0] + dir[0], curr_cord[1] + dir[1]]
        if new_cord[0] in range(board_size) and new_cord[1] in range(board_size):
            if new_board[new_cord[0]][new_cord[1]] == 0:
                new_board[new_cord[0]][new_cord[1]] = 1
                new_price = None
                if prev_dir == [0, 0]:
                    new_price = price + 100
                elif prev_dir == dir:
                    new_price = price + 100
                else:
                    new_price = price + 100 + 500
                prices.append(construct(board_size, new_cord, new_board, dir, new_price))
    #print(prices)
    return min(prices)

solution([[0,0,0],[0,0,0],[0,0,0]])
#900
solution([[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]])
#3800
solution([[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]])
#2100
solution([[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]])
#3200
solution([[0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 1, 1, 1, 1, 1, 0], [1, 0, 0, 1, 0, 0, 0, 0], [1, 1, 0, 0, 0, 1, 1, 1], [1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 0], [1, 1, 1, 1, 1, 1, 1, 0], [1, 1, 1, 1, 1, 1, 1, 0]])
#4500
#[   1, 100, 200, 300, 400, 500, 600, 700]
#[   1, 700,   1,   1,   1,   1,   1,1300]
#[   1, 800,1400,   1,2200,2100,2000,1400]
#[   1,   1,2000,2600,2700,   1,   1,   1]
#[   1,   1,   1,   1,3300,3900,4000,4100]
#[   1,   1,   1,   1,   1,   1,   1,4700]
#[   1,   1,   1,   1,   1,   1,   1,4800]
#[   1,   1,   1,   1,   1,   1,   1,4900]