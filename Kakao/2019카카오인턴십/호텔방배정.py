# 한 번에 한 명씩 신청한 순서대로 방을 배정합니다.
# 고객은 투숙하기 원하는 방 번호를 제출합니다.
# 고객이 원하는 방이 비어 있다면 즉시 배정합니다.
# 고객이 원하는 방이 이미 배정되어 있으면 
# 원하는 방보다 번호가 크면서 비어있는 방 중 가장 번호가 작은 방을 배정합니다.
def solution(k, room_number):
    EMPTY_ROOMS = {room_idx+1:True for room_idx in range(k)}
    ROOMS = {room_idx+1:[[room_idx], room_idx + 2]for room_idx in range(k)}
    ROOMS[1] = [[], 2]
    ROOMS[k] = [[k - 1], 0]

    CLI_ROOMS = []
    # 한 번에 한 명씩 신청한 순서대로 방을 배정합니다.
    # 고객은 투숙하기 원하는 방 번호를 제출합니다.
    for room_n in room_number:
        # 고객이 원하는 방이 비어 있다면 즉시 배정합니다.
        if EMPTY_ROOMS[room_n]:
            CLI_ROOMS.append(room_n)
            PREV_ROOMS, NEXT_ROOM = ROOMS[room_n]
            for PREV_ROOM in PREV_ROOMS:
                if PREV_ROOM != 0:
                    ROOMS[PREV_ROOM][1] = NEXT_ROOM
            if NEXT_ROOM != 0:
                ROOMS[NEXT_ROOM][0] += PREV_ROOMS
            EMPTY_ROOMS[room_n] = False
        # 고객이 원하는 방이 이미 배정되어 있으면 
        else:
            n_room = ROOMS[room_n][1]
            CLI_ROOMS.append(n_room)
            PREV_ROOMS, NEXT_ROOM = ROOMS[n_room]
            for PREV_ROOM in PREV_ROOMS:
                if PREV_ROOM != 0:
                    ROOMS[PREV_ROOM][1] = NEXT_ROOM
            if NEXT_ROOM != 0:
                ROOMS[NEXT_ROOM][0] += PREV_ROOMS
            EMPTY_ROOMS[n_room] = False
        for key, val in ROOMS.items():
            if EMPTY_ROOMS[key]:
                print(" ", key, val)
            else:
                print("#", key, val)

    return CLI_ROOMS



print(solution(10, [4, 5, 6, 3, 3, 4]))