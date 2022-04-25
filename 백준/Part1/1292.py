# 1 2 2 3 3 3 4 4 4 4
#     3 4 5 6 7
Lo, Hi = map(int, input().split())

# 수열 전체를 만들어 주고
Num_list = [j for j in range(46) for i in range(j)]
# split 한 다음 더하는 방식으로 해결
print(sum(Num_list[Lo - 1 : Hi]))