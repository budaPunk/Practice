def solution(user_id, banned_id):
    reslist = []
    DP(user_id, banned_id, [], reslist)
    return len(set(reslist))

def DP(user_id, banned_id, chosen_id, reslist):
    if len(banned_id) == 0:
        reslist.append("/".join(sorted(chosen_id)))
    else:
        banned = banned_id[0]
        for user in user_id:
            if len(banned) == len(user):
                for idx in range(len(banned)):
                    if banned[idx] == user[idx] or banned[idx] == "*":
                        if len(banned) - 1 == idx:
                            new_user_id = user_id[:]
                            new_banned_id = banned_id[:]
                            new_chosen_id = chosen_id[:]
                            new_user_id.remove(user)
                            new_banned_id.remove(banned)
                            new_chosen_id.append(user)
                            DP(new_user_id, new_banned_id, new_chosen_id, reslist)
                        else:
                            pass
                    else:
                        break

#a = [["1", "2", "3"], ["3", "2", "1"], ["1", "2", "4"]]
#print(a)
#print()

solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"])
# 2
solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"])
# 2
solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"])
# 3
