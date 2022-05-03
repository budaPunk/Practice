# BFS? A* search?
def solution1(n, start, end, roads, traps):
    # CURR_TIME:[start, roads]
    STATE_QUEUE = {0:[[start, roads]]}
    MIN_TIME = float("inf")
    while 0 < len(STATE_QUEUE):
        # 가장 걸리는 시간이 작은 case부터 계산해본다.
        CURR_TIME = min(STATE_QUEUE.keys())
        CURR_STATE = STATE_QUEUE[CURR_TIME].pop(0)
        if len(STATE_QUEUE[CURR_TIME]) == 0:
            del STATE_QUEUE[CURR_TIME]
        # 갈 수 있는길 전부 중에서
        for START, END, TIME in CURR_STATE[1]:
            if START == CURR_STATE[0]:
                # 해당 위치까지 도달하는데 걸리는 시간이 MIN_TIME 보다 작을경우
                if CURR_TIME + TIME < MIN_TIME:
                    # 목적지에 도달하는 경우
                    if END == end:
                        # 도달하는데 걸리는 시간이 더 짧으면 MIN_TIME update
                        MIN_TIME = min(CURR_TIME + TIME, MIN_TIME)
                    # 함정에 도달하는 경우
                    elif END in traps:
                        if CURR_TIME + TIME in STATE_QUEUE.keys():
                            STATE_QUEUE[CURR_TIME + TIME].append([END, [[R[1], R[0], R[2]] if END in [R[0], R[1]] else R for R in CURR_STATE[1]]])
                        else:
                            STATE_QUEUE[CURR_TIME + TIME] = [[END, [[R[1], R[0], R[2]] if END in [R[0], R[1]] else R for R in CURR_STATE[1]]]]
                    # 아무것도 아닌 지점에 도달하는 경우
                    else:
                        if CURR_TIME + TIME in STATE_QUEUE.keys():
                            STATE_QUEUE[CURR_TIME + TIME].append([END, CURR_STATE[1][:]])
                        else:
                            STATE_QUEUE[CURR_TIME + TIME] = [[END, CURR_STATE[1][:]]]
        # 기존에 등록되어있던 녀석들도 시간 더 걸리는 녀석들 빼버린다.
        dels = []
        for time in STATE_QUEUE.keys():
            if MIN_TIME <= time:
                dels.append(time)
        for time in dels:
            del STATE_QUEUE[time]

    return MIN_TIME

# 다익스트라
def solution2(n, start, end, roads, traps):
    # list는 key로 사용할 수 없다.
    # STATE : TIME
    DONE = {(start, roads):0}
    # STATE, TIME
    TODO = [[start, roads, 0]]
    MIN_TIME = float("inf")
    while 0 < len(TODO):
        CURR_STATE = TODO.pop(0)
        for START, END, TIME in CURR_STATE[1]:
            if START == CURR_STATE[0]:
                if END == end:
                    MIN_TIME = min(MIN_TIME, CURR_STATE[2] + TIME)
                # 함정에 도달하는 경우
                if END in traps:
                    NEW_STATE = (END, [[R[1], R[0], R[2]] if END in [R[0], R[1]] else R for R in CURR_STATE[1]])
                # 아닐경우
                else:
                    NEW_STATE = (END, CURR_STATE[1][:])
                # 이미 방문한 상태일 경우
                if NEW_STATE in DONE.keys():
                    # 더 짧은 시간에 방문한 기록이 있으면
                    if DONE[NEW_STATE] < CURR_STATE[2] + TIME:
                        pass
                    # 지금 기록이 더 짧으면
                    else:
                        DONE[NEW_STATE] = CURR_STATE[2] + TIME
                        TODO.append(NEW_STATE.append(CURR_STATE[2] + TIME))
                # 방문한적 없는 상태일 경우
                else:
                    DONE[NEW_STATE] = CURR_STATE[2] + TIME
                    TODO.append(NEW_STATE.append(CURR_STATE[2] + TIME))
    return MIN_TIME


print(solution1(3, 1, 3, [[1, 2, 2], [3, 2, 3]], [2]))
print(solution1(4, 1, 4, [[1, 2, 1], [3, 2, 1], [2, 4, 1]], [2, 3]))

print(solution2(3, 1, 3, [[1, 2, 2], [3, 2, 3]], [2]))
print(solution2(4, 1, 4, [[1, 2, 1], [3, 2, 1], [2, 4, 1]], [2, 3]))