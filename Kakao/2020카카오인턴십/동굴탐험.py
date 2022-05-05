# 1. 모든 방을 적어도 한 번은 방문해야 합니다.
# 2. 특정 방은 방문하기 전에 반드시 먼저 방문할 방이 정해져 있습니다.
#   2-1. 이는 A번 방은 방문하기 전에 반드시 B번 방을 먼저 방문해야 한다는 의미입니다.
#   2-2. 어떤 방을 방문하기 위해 반드시 먼저 방문해야 하는 방은 없거나 또는 1개 입니다.
#   2-3. 서로 다른 두 개 이상의 방에 대해 먼저 방문해야 하는 방이 같은 경우는 없습니다.
#   2-4. 어떤 방이 먼저 방문해야 하는 방이면서 동시에 나중에 방문해야 되는 방인 경우는 없습니다.

# 방 개수 n, 
# 동굴의 각 통로들이 연결하는 두 방의 번호가 담긴 2차원 배열 path, 
# 프로도가 정한 방문 순서가 담긴 2차원 배열 order가 매개변수로 주어질 때 [선, 후]


def solution1(n, path, order):
    # {NEXT:FIRST}
    ORDER_DICT = {order[order_idx][1]:order[order_idx][0] for order_idx in range(len(order))}
    # {"VISITED-CURRPOS":MOVES, "O4XXX8X6X-0":0}
    INIT_VISITED = ""
    for room_idx in range(n):
        # start from room 0
        if room_idx == 0:
            INIT_VISITED += "O"
        elif room_idx in ORDER_DICT.keys():
            INIT_VISITED += str(ORDER_DICT[room_idx])
        else:
            INIT_VISITED += "X"
    TO_EXPLORE = {INIT_VISITED+"-0":0}
    EXPLORED = {INIT_VISITED+"-0":0}
    
    while 0 < len(TO_EXPLORE):
        # Get One Unexplored Status
        visited, currpos, currmov = None, None, None
        popkey = [K for K in TO_EXPLORE.keys()][0]
        visited, currpos = popkey.split("-")
        currpos = int(currpos)
        currmov = TO_EXPLORE.pop(popkey)
        # Explore
        for pat in path:
            # Can Move 
            if currpos == pat[0] and visited[pat[1]] in "OX":
                new_pos = pat[1]        # Move
                new_move = currmov + 1  # move++
                new_visited = ""
                for visited_idx in range(n):
                    # Mark Move
                    if new_pos == visited_idx:
                        new_visited += "O"
                    # del order
                    elif str(new_pos) == visited[visited_idx]:
                        new_visited += "X"
                    else:
                        new_visited += visited[visited_idx]
                #print(new_visited, new_pos, new_move)
                # add to TO_EXPLORE, EXPLORED
                new_key = "-".join([new_visited, str(new_pos)])
                # if EXPLORED before
                if new_key in EXPLORED.keys():
                    # curr more efficient
                    if EXPLORED[new_key] > new_move:
                        TO_EXPLORE[new_key] = new_move
                # not been explored
                else:
                    TO_EXPLORE[new_key] = new_move
            # Can Move
            elif currpos == pat[1] and visited[pat[0]] in "OX":
                new_pos = pat[0]        # Move
                new_move = currmov + 1  # move++
                new_visited = ""
                for visited_idx in range(n):
                    # Mark Move
                    if new_pos == visited_idx:
                        new_visited += "O"
                    # del order
                    elif str(new_pos) == visited[visited_idx]:
                        new_visited += "X"
                    else:
                        new_visited += visited[visited_idx]
                #print(new_visited, new_pos, new_move)
                # add to TO_EXPLORE, EXPLORED
                new_key = "-".join([new_visited, str(new_pos)])
                # if EXPLORED before
                if new_key in EXPLORED.keys():
                    # curr more efficient
                    if EXPLORED[new_key] > new_move:
                        TO_EXPLORE[new_key] = new_move
                # not been explored
                else:
                    TO_EXPLORE[new_key] = new_move
            else:
                pass
        EXPLORED[popkey] = currmov
    
    for key in EXPLORED.keys():
        if "O"*n in key:
            return True
    return False
 
def solution2(n, path, order):
    # {후:선}
    NP = {order[order_idx][1]:order[order_idx][0] for order_idx in range(len(order))}
    # {선:후}
    PN = {order[order_idx][0]:order[order_idx][1] for order_idx in range(len(order))}
    # ['O', '4', 'X', 'X', 'X', '8', 'X', '6', 'X']
    VISITED = []
    for room_idx in range(n):
        # start from room 0
        if room_idx == 0:
            VISITED.append("O")
        elif room_idx in NP.keys():
            VISITED.append(str(NP[room_idx]))
        else:
            VISITED.append("X")

    while 1:
        P_LEN = len(path) + 0
        del_pats = []
        for P0, P1 in path:
            # 하나는 방문 했고 하나는 아직 방문 안했을 경우에
            if [VISITED[P0], VISITED[P1]] == ["O", "X"]:
                # 방문한거로 기록하고
                VISITED[P1] = "O"
                # 선후방문 기록
                if P1 in PN.keys():
                    VISITED[PN[P1]] = "X"
                del_pats.append([P0, P1])
            elif [VISITED[P0], VISITED[P1]] == ["X", "O"]:
                # 방문한거로 기록하고
                VISITED[P0] = "O"
                # 선후방문 기록
                if P0 in PN.keys():
                    VISITED[PN[P0]] = "X"
                del_pats.append([P0, P1])
        for pat in del_pats:
            path.remove(pat)
        
        if len(path) == 0:
            return True
        elif len(path) == P_LEN:
            return False

def solution3(n, path, order):
    # NODE:[PARRENT, [CHILDS]]
    TREE = {0:[-1, []]}

    # BUILD TREE
    while len(path):
        DELPS = []
        # record par and child
        for P1, P2 in path:
            if P1 in TREE.keys():
                PAR, CHI= P1, P2
                TREE[CHI] = [PAR, []]
                TREE[PAR][1].append(CHI)
                DELPS.append([P1, P2])
            elif P2 in TREE.keys():
                PAR, CHI= P2, P1
                TREE[CHI] = [PAR, []]
                TREE[PAR][1].append(CHI)
                DELPS.append([P1, P2])
        # remove from path
        for DELP in DELPS:
            path.remove(DELP)

    # MAKE ORDER
    for PRE, NXT in order:
        TREE[PRE][1].append(NXT)          # PRE의 CHID 에 NXT 추가
        if NXT in TREE[TREE[NXT][0]][1]:
            TREE[TREE[NXT][0]][1].remove(NXT) # NXT는 원래 부모와 연을 끊고
        TREE[NXT][0] = PRE                # NXT는 PRE의 자식이 된다.

    # 뿌리에서 갈 수 있는 방들의 수를 카운트 해본다.
    FIND_CHILD_QUEUE = [0]
    FOUND_CHILD_COUNT = 1
    while 0 < len(FIND_CHILD_QUEUE):
        TODAYS_PARENT = FIND_CHILD_QUEUE.pop(0)
        FIND_CHILD_QUEUE += TREE[TODAYS_PARENT][1]
        FOUND_CHILD_COUNT += len(TREE[TODAYS_PARENT][1])
        print(TREE[TODAYS_PARENT][1])
    print(FOUND_CHILD_COUNT)
    print(TREE)
    if n == FOUND_CHILD_COUNT:
        return True
    else:
        return False

def solution4(n, path, order):
    #path 정보로 부터 인접 리스트를 구현한다.
    tree = [[] for _ in range(n)]
    for v1, v2 in path:
        tree[v1].append(v2)
        tree[v2].append(v1)
      
    #어떤 방 X에 가기 위해 들러야하는 방은 1개이거나 존재하지 않음
    #orders[i] : i번째 방을 방문하기 위해 이전에 방문해야하는 노드
    HAVE_TO_VISIT =[0 for i in range(n)]
    for pre, post in order:
        HAVE_TO_VISIT[post] = pre
    
    num_visit = 0
    
    HAVE_VISITED = [False for i in range(n)]
    q = [0]
    
    #방문해야하는 노드 : key에 있는 노드를 들른 후 갈 수 있는 노드
    CAN_GO ={}
    
    while q:
        here = q.pop(0)
        
        #현재 위치를 방문하기전에 들러야하는 정점이 존재하고 아직 그 정점을 방문하지 않았다면 체크해둔다.
        #orders[here] : here를 방문하기 위해 이전에 방문해야하는 정점
        if HAVE_TO_VISIT[here] and not HAVE_VISITED[HAVE_TO_VISIT[here]]:
            CAN_GO[HAVE_TO_VISIT[here]] = here
            continue
        else:
            # 갈 수 있는 곳이었다면 방문해보자!
            HAVE_VISITED[here] = True
            num_visit +=1
            
            #현재 위치와 연결되어 있는 점들을 q에 추가해준다.
            for there in tree[here]:
                if not HAVE_VISITED[there]:
                    q.append(there)
            
            #지금 방문하는 곳이 after에 포함되어 있다면 이제 현재 위치를 방문해야 갈 수 있는 정점으로 
            #이동가능하므로 이동가능 한 정점을 q에 넣어준다.
            if here in CAN_GO:
                q.append(CAN_GO[here])
                    
    return n == num_visit

                


print(solution2(9, [[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]], [[8,5],[6,7],[4,1]]))
# true
print(solution2(9, [[8,1],[0,1],[1,2],[0,7],[4,7],[0,3],[7,5],[3,6]], [[4,1],[5,2]]))
# true
print(solution2(9, [[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]], [[4,1],[8,7],[6,5]]))
# false


0
3
6
5