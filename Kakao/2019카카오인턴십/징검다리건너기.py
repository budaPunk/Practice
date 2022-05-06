# 디딤돌에 적힌 숫자가 순서대로 담긴 배열 stones와 
# 한 번에 건너뛸 수 있는 디딤돌의 최대 칸수 k가 매개변수로 주어질 때, 
# 최대 몇 명까지 징검다리를 건널 수 있는지 return 하도록 solution 함수를 완성해주세요.
def solution(stones, k):
    LB, UB = 1, max(stones)
    ans = 0

    #print("".join(list(map(str, stones))))

    while LB <= UB:
        MID = (UB + LB) // 2
        
        unable_in_row = 0
        for stone in stones:
            if stone <= MID:
                #print(" ", end="")
                unable_in_row += 1
            else:
                #print("#", end="")
                unable_in_row = 0
            if unable_in_row >= k:
                break
        #print("       ", LB, MID, UB)

        # MID IS LOW
        if unable_in_row < k:
            LB = MID + 1
        # MID IS HIGH
        else:
            ans = MID
            UB = MID - 1
    
    return ans

def solutiona(stones, k):
    sorted_stones = sorted(list(set(stones)))
    cross = 0
    while 1:
        safe_min = sorted_stones.pop(0) - cross
        cross += safe_min
        for stone_idx in range(len(stones)):
            stones[stone_idx] -= safe_min
            if stones[stone_idx] < 0:
                stones[stone_idx] = 0
        for stone_idx in range(len(stones) - k + 1):
            if stones[stone_idx:stone_idx + k] == [0] * (k):
                return cross

print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 4))
print(solutiona([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 4))

"""
for pop_idx in range(26):
    ALPHA = ["A", "B", "C", "D", "E", "F", "G",
            "H", "I", "J", "K", "L", "M", "N",
            "O", "P", "Q", "R", "S", "T", "U",
            "V", "W", "X", "Y", "Z"]
    SEARCH = ALPHA.pop(pop_idx)
    UB = len(ALPHA) - 1
    LB = 0
    while LB <= UB:
        MID = (UB + LB) // 2
        print("".join(ALPHA))
        for idx in range(len(ALPHA)):
            if idx == UB:
                print("U", end="")
            elif idx == LB:
                print("L", end="")
            elif idx == MID:
                print("M", end="")
            else:
                print(" ", end="")
        
        print("       ", LB, MID, UB)
        # MID IS HIGH
        if SEARCH < ALPHA[MID]:
            UB = MID - 1
        elif ALPHA[MID] == SEARCH:
            print(MID)
        # MID IS LOW
        elif ALPHA[MID] < SEARCH:
            LB = MID + 1
    print("============",LB, UB, "============")
"""