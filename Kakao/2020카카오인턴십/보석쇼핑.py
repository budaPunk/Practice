# 싹쓸이 구매를 하고 싶은데 모든 종류가 포함되게 하고 싶습니다.
def solution(gems):
    TYPE_COUNT = len(set(gems)) # 종류개수
    SHOP_LEN = len(gems)        # 진열대 길이
    answer = None
    left, right = 0, 0
    # 초기값
    cur_shop = {gems[0]: 1}
    while left in range(SHOP_LEN) and right in range(SHOP_LEN):
        # 보석이 종류별로 하나 이상씩 있지 못하면
        if len(cur_shop) < TYPE_COUNT:
            # 범위 한칸 증가시키고
            right += 1
            # 상점 범위 이탈시 끝낸다.
            if right == SHOP_LEN:
                break
            # 새로 들어온 보석을 count up 해준다.
            if gems[right] in cur_shop.keys():
                cur_shop[gems[right]] += 1
            else:
                cur_shop[gems[right]] = 1
        # 보석을 종류별로 하나 이상씩 가지고 있다면
        else:
            # [몇개사는지, [leftidx, rightidx]] 를 저장하고
            if answer == None:
                answer = [right-left, left+1, right+1]
            # 내가 더 짧을경우
            elif right-left < answer[0]:
                answer = [right-left, left+1, right+1]
            # 나랑 길이가 같을 경우
            elif right-left == answer[0]:
                # 내가 좌측 인덱스가 더 짧다면
                if left + 1 < answer[1]:
                    answer = [right-left, left+1, right+1]
            # 곧 고려하지 않게 될 보석 하나 빼고
            cur_shop[gems[left]] -= 1
            # 보석 하나도 없는거는 인덱스를 지워버리고
            if cur_shop[gems[left]] == 0:
                del cur_shop[gems[left]]
            # 한칸 줄인다.
            left += 1
    return [answer[1], answer[2]]
        


solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"])
#[3, 7]
solution(["AA", "AB", "AC", "AA", "AC"])
#[1, 3]
solution(["XYZ", "XYZ", "XYZ"])
#[1, 1]
solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"])
#[1, 5]