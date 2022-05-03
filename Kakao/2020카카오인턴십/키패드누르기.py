# 맨 처음 왼손 엄지손가락은 * 키패드에 오른손 엄지손가락은 # 키패드 위치에서 시작하며, 
# 엄지손가락을 사용하는 규칙은 다음과 같습니다.
# 1. 엄지손가락은 상하좌우 4가지 방향으로만 이동할 수 있으며 키패드 이동 한 칸은 거리로 1에 해당합니다.
# 2. 왼쪽 열의 3개의 숫자 1, 4, 7을 입력할 때는 왼손 엄지손가락을 사용합니다.
# 3. 오른쪽 열의 3개의 숫자 3, 6, 9를 입력할 때는 오른손 엄지손가락을 사용합니다.
# 4. 가운데 열의 4개의 숫자 2, 5, 8, 0을 입력할 때는 두 엄지손가락의 현재 키패드의 위치에서 더 가까운 엄지손가락을 사용합니다.
#   4-1. 만약 두 엄지손가락의 거리가 같다면, 오른손잡이는 오른손 엄지손가락, 왼손잡이는 왼손 엄지손가락을 사용합니다.
def solution(numbers, hand):
    #
    BUTTON_CORD = {"1":[0,0], "2":[0,1], "3":[0,2], "4":[1,0], "5":[1,1], "6":[1,2],
                   "7":[2,0], "8":[2,1], "9":[2,2], "*":[3,0], "0":[3,1], "#":[3,2]}
    # [LHAND, RHAND]
    CURR_STATUS = [BUTTON_CORD["*"], BUTTON_CORD["#"]]
    
    answer = ""
    for number in numbers:
        str_number = str(number)
        if str_number in "147":
            answer += "L"
            CURR_STATUS[0] = BUTTON_CORD[str_number]
        elif str_number in "369":
            answer += "R"
            CURR_STATUS[1] = BUTTON_CORD[str_number]
        else:
            ldist = getdist(CURR_STATUS[0], BUTTON_CORD[str_number])
            rdist = getdist(CURR_STATUS[1], BUTTON_CORD[str_number])
            if ldist == rdist:
                if hand == "left":
                    answer += "L"
                    CURR_STATUS[0] = BUTTON_CORD[str_number]
                elif hand == "right":
                    answer += "R"
                    CURR_STATUS[1] = BUTTON_CORD[str_number]
            elif ldist < rdist:
                answer += "L"
                CURR_STATUS[0] = BUTTON_CORD[str_number]
            elif ldist > rdist:
                answer += "R"
                CURR_STATUS[1] = BUTTON_CORD[str_number]
    print(answer)
    return answer

def getdist(finger, dest):
    return abs(finger[0] - dest[0]) + abs(finger[1] - dest[1])

solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right")    # "LRLLLRLLRRL"
solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left")	    # "LRLLRRLLLRR"
solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right")       # "LLRLLRLLRL"

"""
  012
0 123
1 456
2 789
3 *0#
"""