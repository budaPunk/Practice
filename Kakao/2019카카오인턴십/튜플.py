def solution(s):
    wordlists = {}
    temp = []
    for c in s[1:-1].split(","):
        temp.append(c)
        if "{" in ",".join(temp) and "}" in ",".join(temp):
            temp_list = list(map(int, ",".join(temp)[1:-1].split(",")))
            wordlists[len(temp_list)] = temp_list
            temp = []
    res = []
    for i in range(len(wordlists)):
        if i == 0:
            res.append(wordlists[i+1][0])
        else:
            for j in wordlists[i+1]:
                if j in wordlists[i]:
                    pass
                else:
                    res.append(j)
                    break
    return res


solution("{{2},{2,1},{2,1,3},{2,1,3,4}}")
# [2, 1, 3, 4]
solution("{{1,2,3},{2,1},{1,2,4,3},{2}}")
# [2, 1, 3, 4]
solution("{{20,111},{111}}")
# [111, 20]
solution("{{123}}")
# [123]
solution("{{4,2,3},{3},{2,3,4,1},{2,3}}")
# [3, 2, 4, 1]