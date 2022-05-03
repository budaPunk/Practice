# 1. 하나의 노드는 하나의 시험장을 나타냅니다.
# 2. 검은 바탕의 흰 숫자는 해당 시험장의 고유 번호(ID)를 나타냅니다.
#   2-1. 시험장이 n개 있다면, 시험장의 고유 번호는 0부터 n-1까지 부여됩니다.
# 3. 노드 안의 빨간 숫자는, 해당 시험장의 응시자 수를 나타냅니다.
#   3-1. 위의 그림에서, 9번 시험장에는 10명, 4번 시험장에는 8명, 6번 시험장에는 20명의 응시자가 시험을 볼 예정입니다.
# 4. 노드 사이의 간선은 해당 시험장이 연결되어 있음을 의미합니다.
#   4-1. 위의 그림에서, 9번 시험장은 7번 시험장과, 7번 시험장은 6번 시험장과 연결되어 있습니다.

# 나눌 그룹의 수를 나타내는 정수 k, 
# 각 시험장의 응시자 수를 나타내는 1차원 정수 배열 num, 
# 시험장의 연결 상태를 나타내는 2차원 정수 배열 links가 매개변수로 주어집니다. 
# 인원이 가장 많은 그룹의 인원이 최소화되도록 k개의 그룹으로 나누었을 때, 
# 최소화된 최대 그룹의 인원을 return 하도록 solution 함수를 완성해주세요.
from copy import deepcopy

def solution1(k, num, links):
    SUMMED, ROOT = Summer(num, links)
    PARTIAL_SUM = SUMMED[ROOT][0] // k
    while 1:
        #print(SUMMED)
        if Search2(SUMMED, PARTIAL_SUM + 1, k + 1, 0):
            break
        PARTIAL_SUM += 1
        #input()
    print(PARTIAL_SUM)

# ROOM_NUMBER:[NUM_SUM, LEFT_ROOM, RIGHT_ROOM, PAR_NUMBER]
def Summer(num, links):
    ROOT = -1
    RESULT = {}
    BUFFER = {idx:[num[idx], links[idx][0], links[idx][1]]for idx in range(len(num))}
    while len(BUFFER):
        # find leaf nodes
        LEAFS = []
        for ROOM_NUM in BUFFER.keys():
            BN, BLC, BRC = BUFFER[ROOM_NUM]
            if BLC not in BUFFER.keys() and BRC not in BUFFER.keys():
                LEAFS.append(ROOM_NUM)
        # move leaf to result
        for ROOM_NUM in LEAFS:
            BN, BLC, BRC = BUFFER.pop(ROOM_NUM)
            if BLC in RESULT.keys():
                BN += RESULT[BLC][0]
                RESULT[BLC][3] = ROOM_NUM
            if BRC in RESULT.keys():
                BN += RESULT[BRC][0]
                RESULT[BRC][3] = ROOM_NUM
            RESULT[ROOM_NUM] = [BN, BLC, BRC, -1]
        # root node
        if len(BUFFER) == 1:
            ROOT = [k for k in BUFFER.keys()][0]
    return RESULT, ROOT

def Search1(summed, PARTIAL_SUM, depth_limit, depth):
    SUMMED = deepcopy(summed)
    # 아직 기회가 더 남아있다면
    if depth < depth_limit:
        # 리스트를 비우는것에 성공했다면.
        if len(SUMMED) == 0:
            #print("TRUE", SUMMED, PARTIAL_SUM, depth_limit, depth)
            return True
        DEL_ROOT = {}
        # Find Biggest
        for ROOM_NUM in SUMMED.keys():
            if PARTIAL_SUM > SUMMED[ROOM_NUM][0]:
                if PARTIAL_SUM - SUMMED[ROOM_NUM][0] in DEL_ROOT.keys():
                    DEL_ROOT[PARTIAL_SUM - SUMMED[ROOM_NUM][0]].append(ROOM_NUM)
                else:
                    DEL_ROOT[PARTIAL_SUM - SUMMED[ROOM_NUM][0]] = [ROOM_NUM]
        # Del childs
        DEL_ROOT_KEYS = [k for k in DEL_ROOT.keys()]
        DEL_ROOT_KEYS.sort()

        for DRK in DEL_ROOT_KEYS:
            while 0 < len(DEL_ROOT[DRK]):
                DR = DEL_ROOT[DRK].pop(0)

                SUMMED_DC = deepcopy(SUMMED)
                DN, DLC, DRC, DP = SUMMED_DC.pop(DR)
                # Del from parrent
                if DP == -1:
                    pass
                else:
                    cdp = DP
                    while 1:
                        SUMMED_DC[cdp][0] -= DN
                        cdp = SUMMED_DC[cdp][3]
                        if cdp == -1:
                            break
                    if SUMMED_DC[DP][1] == DR:
                        SUMMED_DC[DP][1] = -1
                    if SUMMED_DC[DP][2] == DR:
                        SUMMED_DC[DP][2] = -1
                # Del childs
                CHILDS = [DLC, DRC]
                while 0 < len(CHILDS):
                    CHILD_NUM = CHILDS.pop(0)
                    if CHILD_NUM == -1:
                        pass
                    else:
                        NS, LC, RC, P = SUMMED_DC.pop(CHILD_NUM)
                        CHILDS += [LC, RC]
                #print(DR)
                #print(SUMMED_DC, PARTIAL_SUM, depth_limit, depth)
                if Search1(SUMMED_DC, PARTIAL_SUM, depth_limit, depth+1):
                    #print("TRUE", SUMMED, PARTIAL_SUM, depth_limit, depth)
                    return True
    # 기회가 더이상 없다면
    else:
        #print("FALSE", SUMMED, PARTIAL_SUM, depth_limit, depth)
        return False

def Search2(summed, PARTIAL_SUM, depth_limit, depth):
    SUMMED = deepcopy(summed)
    # 아직 기회가 더 남아있다면
    if depth < depth_limit:
        # 리스트를 비우는것에 성공했다면.
        if len(SUMMED) == 0:
            return True
        DEL_ROOT = []
        HOW_FAR = float("inf")
        # Find Biggest
        for ROOM_NUM in SUMMED.keys():
            if PARTIAL_SUM > SUMMED[ROOM_NUM][0]:
                if HOW_FAR > PARTIAL_SUM - SUMMED[ROOM_NUM][0]:
                    HOW_FAR = PARTIAL_SUM - SUMMED[ROOM_NUM][0]
                    DEL_ROOT = [ROOM_NUM]
                elif HOW_FAR == PARTIAL_SUM - SUMMED[ROOM_NUM][0]:
                    HOW_FAR = PARTIAL_SUM - SUMMED[ROOM_NUM][0]
                    DEL_ROOT.append(ROOM_NUM)
        # Del childs
        for DR in DEL_ROOT:
            SUMMED_DC = deepcopy(SUMMED)
            DN, DLC, DRC, DP = SUMMED_DC.pop(DR)
            # Del from parrent
            if DP == -1:
                pass
            else:
                cdp = DP
                while 1:
                    SUMMED_DC[cdp][0] -= DN
                    cdp = SUMMED_DC[cdp][3]
                    if cdp == -1:
                        break
                if SUMMED_DC[DP][1] == DR:
                    SUMMED_DC[DP][1] = -1
                if SUMMED_DC[DP][2] == DR:
                    SUMMED_DC[DP][2] = -1
            # Del childs
            CHILDS = [DLC, DRC]
            while 0 < len(CHILDS):
                CHILD_NUM = CHILDS.pop(0)
                if CHILD_NUM == -1:
                    pass
                else:
                    NS, LC, RC, P = SUMMED_DC.pop(CHILD_NUM)
                    CHILDS += [LC, RC]
            if Search2(SUMMED_DC, PARTIAL_SUM, depth_limit, depth+1):
                return True
    # 기회가 더이상 없다면
    else:
        return False

"""
di = {1:"a", 3:"b", 9:"c", 5:"d", 7:"e"}
print(di.keys())
a = [k for k in di.keys()]
print(a)
a.sort(reverse=True)
print(a)
"""
import sys
sys.setrecursionlimit(10 ** 6)
def solution2(k, num, links):
    # if have parent => False
    root_candidate = [True for i in range(len(num))]
    for a, b in links:
        for i in (a,b):
            if i>=0:
                root_candidate[i] = False
    # root_candidate[idx] == True => root = idx
    root = None
    for i in range(len(root_candidate)):
        if root_candidate[i]:
            root = i
            break

    max_sum = sum(num)
    # left = 조각의 최소값, right = 조각의 최대값
    left, right = max(num), max_sum
    while left < right:
        print(left, right)
        # dp[i][0] = i번 노드를 루트 노드로 하는 서브트리를 최대 그룹 인원이 L 이하가 되도록 하기 위한 최소 그룹의 수
        # dp[i][1] = i번 노드를 루트 노드로 하는 서브트리를 최대 그룹 인원이 L 이하가 되도록 dp[i][0]개로 나누었을 때, 
        #            i번 노드가 포함되는 서브트리의 가중치 합의 최솟값
        dp = [None for _ in range(len(num))] # 이 친구가 
        mid = (left + right) // 2
        result = travelsal(root, mid, num, links, dp, max_sum)
        if result[1] <= k:
            right = mid
        else:
            left = mid + 1
        input()
    print(left)
    return left

def travelsal(root, lower_bound, num, links, dp, max_sum):
    left, right = links[root]
    if dp[root] != None:
        return dp[root]
    # 우선 전부 쪼개고
    dp_left, dp_right = [
        travelsal(i, lower_bound, num, links, dp, max_sum) if i != -1 else [max_sum, 0] for i in [left, right]
    ]
    # 합치면서 계산하는편
    all_sum = num[root] + dp_left[0] + dp_right[0]
    two_sum = num[root] + min(dp_left[0], dp_right[0])
    if all_sum <= lower_bound:
        dp[root] = all_sum, dp_left[1] + dp_right[1] - 1
    elif two_sum <= lower_bound:
        dp[root] = two_sum, dp_left[1] + dp_right[1]
    else:
        dp[root] = num[root], dp_left[1] + dp_right[1] + 1
    print(dp)
    return dp[root]

#solution2(3, [12, 30, 1, 8, 8, 6, 20, 7, 5, 10, 4, 1], [[-1, -1], [-1, -1], [-1, -1], [-1, -1], [8, 5], [2, 10], [3, 0], [6, 1], [11, -1], [7, 4], [-1, -1], [-1, -1]])
solution2(1, [6, 9, 7, 5], [[-1, -1], [-1, -1], [-1, 0], [2, 1]])
solution2(2, [6, 9, 7, 5], [[-1, -1], [-1, -1], [-1, 0], [2, 1]])
solution2(4, [6, 9, 7, 5], [[-1, -1], [-1, -1], [-1, 0], [2, 1]])