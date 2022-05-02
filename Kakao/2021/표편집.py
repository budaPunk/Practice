# "U X": 현재 선택된 행에서 X칸 위에 있는 행을 선택합니다.
# "D X": 현재 선택된 행에서 X칸 아래에 있는 행을 선택합니다.
# "C" : 현재 선택된 행을 삭제한 후, 바로 아래 행을 선택합니다. 단, 삭제된 행이 가장 마지막 행인 경우 바로 윗 행을 선택합니다.
# "Z" : 가장 최근에 삭제된 행을 원래대로 복구합니다. 단, 현재 선택된 행은 바뀌지 않습니다.

# 처음 표의 행 개수를 나타내는 정수 n, 
# 처음에 선택된 행의 위치를 나타내는 정수 k, 
# 수행한 명령어들이 담긴 문자열 배열 cmd가 매개변수로 주어질 때, 
# 모든 명령어를 수행한 후 표의 상태와 처음 주어진 표의 상태를 비교하여 삭제되지 않은 행은 O, 
# 삭제된 행은 X로 표시하여 문자열 형태로 return 하도록 solution 함수를 완성해주세요.

from cgitb import reset
from tkinter import NE


def solution1(n, k, cmd):
    CURR_K = k
    DEL_LOG = []
    CURR_STATE = ["O" for idx in range(n)]
    
    for command in cmd:
        # Save Curr State
        if "U" in command:
            C, X = command.split()
            CURR_K = UD(C, CURR_STATE, CURR_K, int(X))
        elif "D" in command:
            C, X = command.split()
            CURR_K = UD(C, CURR_STATE, CURR_K, int(X))
        elif "C" in command:
            # 현재 선택된 행을 삭제한 후
            CURR_STATE[CURR_K] = "X"
            DEL_LOG.append(CURR_K)
            # 바로 아래 행을 선택합니다.
            if "O" in CURR_STATE[CURR_K:]:
                CURR_K = UD("D", CURR_STATE, CURR_K, 1)
            # 삭제된 행이 가장 마지막 행인 경우 바로 윗 행을 선택합니다.
            else:
                CURR_K = UD("U", CURR_STATE, CURR_K, 1)
        elif "Z" in command:
            CURR_STATE[DEL_LOG.pop()] = "O"

    return "".join(CURR_STATE)

def UD(UorD, CURR_STATE, CURR_K, HowMuch):
    HM = HowMuch
    NEW_K = CURR_K
    while HM:
        if UorD == "U":
            NEW_K -= 1
        elif UorD == "D":
            NEW_K += 1
        else:
            print("ERROR")
        if CURR_STATE[NEW_K] == "O":
            HM -= 1
    return NEW_K

def solution2(n, k, cmd):
    IDX_K = k
    IDX_DEL_LOG = []
    IDX_LIST = [idx for idx in range(n)]

    for command in cmd:
        # Save Curr State
        if "U" in command:
            C, X = command.split()
            IDX_K -= int(X)
        elif "D" in command:
            C, X = command.split()
            IDX_K += int(X)
        elif "C" in command:
            # LOG 남기고 현재 선택된 행을 삭제한 후
            IDX_DEL_LOG.append([IDX_K, IDX_LIST.pop(IDX_K)])
            # 삭제된 행이 가장 마지막 행인 경우 바로 윗 행을 선택합니다.
            if IDX_K == len(IDX_LIST):
                IDX_K -= 1
            # 바로 아래 행을 선택합니다.
            else:
                pass
        elif "Z" in command:
            LOG = IDX_DEL_LOG.pop()
            IDX_LIST.insert(LOG[0], LOG[1])
            if IDX_K < LOG[0]:
                pass
            else:
                IDX_K += 1

    return "".join(["O" if idx in IDX_LIST else "X" for idx in range(n)])

def solution3(n, k, cmd):
    IDX_K = k
    IDX_DEL_LOG = []
    IDX_LIST = [idx for idx in range(n)]

    for command in cmd:
        # Save Curr State
        if "U" in command:
            C, X = command.split()
            IDX_K -= int(X)
        elif "D" in command:
            C, X = command.split()
            IDX_K += int(X)
        elif "C" in command:
            # LOG 남기고
            IDX_DEL_LOG.append([IDX_LIST[:], IDX_K])
            # 현재 선택된 행을 삭제한 후
            IDX_LIST.pop(IDX_K)
            # 삭제된 행이 가장 마지막 행인 경우 바로 윗 행을 선택합니다.
            if IDX_K == len(IDX_LIST):
                IDX_K -= 1
            # 바로 아래 행을 선택합니다.
            else:
                pass
        elif "Z" in command:
            LOG = IDX_DEL_LOG.pop()
            IDX_LIST, INS_K = LOG[0], LOG[1]
            if IDX_K < INS_K:
                pass
            else:
                IDX_K += 1

    return "".join(["O" if idx in IDX_LIST else "X" for idx in range(n)])

def solution4(n, k, cmd):
    IDX_K = k
    IDX_DEL_LOG = []
    IDX_LIST = [idx for idx in range(n)]

    for command in cmd:
        # Save Curr State
        if "U" in command:
            C, X = command.split()
            IDX_K -= int(X)
        elif "D" in command:
            C, X = command.split()
            IDX_K += int(X)
        elif "C" in command:
            # LOG 남기고 현재 선택된 행을 삭제한 후
            IDX_DEL_LOG.append([IDX_K, IDX_LIST.pop(IDX_K)])
            # 삭제된 행이 가장 마지막 행인 경우 바로 윗 행을 선택합니다.
            if IDX_K == len(IDX_LIST):
                IDX_K -= 1
            # 바로 아래 행을 선택합니다.
            else:
                pass
        elif "Z" in command:
            LOG = IDX_DEL_LOG.pop()
            IDX_LIST.append(LOG[1])
            IDX_LIST.sort()
            if IDX_K < LOG[0]:
                pass
            else:
                IDX_K += 1

    return "".join(["O" if idx in IDX_LIST else "X" for idx in range(n)])

# 풀이 https://kjhoon0330.tistory.com/entry/프로그래머스-표-편집-Python
# 파이썬 자료구조 시간복잡도 https://wayhome25.github.io/python/2017/06/14/time-complexity/
# dict 자료형을 통해서 링크드 리스트 비슷한거를 쉽게 만들 수 있다.
# dict가 hasy table 구조라고 하니까 무조건 dict쓰는게 옳을듯
def solution5(n, k, cmd):
    IDX_K = k
    IDX_DELL_LOG = []
    IDX_DICT = { idx:[idx-1, idx+1] for idx in range(n) }
    IDX_DICT[0], IDX_DICT[n - 1] = [None, 1], [n-2, None]
    for command in cmd:
        if "U" in command:
            # <= X ==
            C, X = command.split()
            for _ in range(int(X)):
                IDX_K = IDX_DICT[IDX_K][0]
        elif "D" in command:
            # == X =>
            C, X = command.split()
            for _ in range(int(X)):
                IDX_K = IDX_DICT[IDX_K][1]
        elif "C" in command:
            PREV, NEXT = IDX_DICT.pop(IDX_K) # pop 이지랄 하는데 시간 너무 많이 쓰는것 같기도 함.
            IDX_DELL_LOG.append([PREV, IDX_K, NEXT])
            # 삭제된 행이 가장 마지막 행인 경우 바로 윗 행을 선택합니다.
            if NEXT == None:
                IDX_K = PREV
                IDX_DICT[IDX_K][1] = None
            # 삭제된 행이 가장 앞쪽의 행인 경우 다음행 선택
            elif PREV == None:
                IDX_K = NEXT
                IDX_DICT[IDX_K][0] = None
            # 삭제된 행이 가운데 행일 경우 양쪽 연결
            else:
                IDX_K = NEXT
                IDX_DICT[PREV][1] = NEXT
                IDX_DICT[NEXT][0] = PREV
        elif "Z" in command:
            PREV, NOW, NEXT = IDX_DELL_LOG.pop()
            # 복구된 행이 가장 마지막 행인 경우 바로 윗 행을 선택합니다.
            if NEXT == None:
                IDX_DICT[NOW] = [PREV, NEXT]
                IDX_DICT[PREV][1] = NOW
            # 복구된 행이 가장 앞쪽의 행인 경우 다음행 선택
            elif PREV == None:
                IDX_DICT[NOW] = [PREV, NEXT]
                IDX_DICT[NEXT][0] = NOW
            # 복구된 행이 가운데 행일 경우 양쪽 연결
            else:
                IDX_DICT[NOW] = [PREV, NEXT]
                IDX_DICT[PREV][1] = NOW
                IDX_DICT[NEXT][0] = NOW
    
    return "".join(["O" if idx in IDX_DICT.keys() else "X" for idx in range(n)])

#return answer
cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]
print(solution1(8, 2, cmd))
print(solution5(8, 2, cmd))