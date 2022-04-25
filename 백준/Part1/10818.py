from cmath import inf

# 첫째 줄에 정수의 개수 N (1 ≤ N ≤ 1,000,000)이 주어진다. 
N = int(input())
# 둘째 줄에는 N개의 정수를 공백으로 구분해서 주어진다. 
# 모든 정수는 -1,000,000보다 크거나 같고, 1,000,000보다 작거나 같은 정수이다.
Nums = list(map(int, input().split()))
min_max = [inf, -inf]
for Num in Nums:
  # if Num smaller then min
  if Num < min_max[0]:
    # Num is new min
    min_max[0] = Num
  # if Num Bigger then max
  if min_max[1] < Num:
    # Num is new max
    min_max[1] = Num

print(min_max[0], min_max[1])