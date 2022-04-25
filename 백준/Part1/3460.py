from math import log2

# 첫째 줄에 테스트 케이스의 개수 T가 주어진다. 
T = int(input())

# 각 테스트 케이스는 한 줄로 이루어져 있고, n이 주어진다. 
# (1 ≤ T ≤ 10, 1 ≤ n ≤ 106)
for T_idx in range(T):
  n10 = int(input())
  n2 = {0 : [], 1 : []}
  while True:
    # 나머지가 0일 경우 log연산 불필요&불가
    if n10 == 0:
      break
    # 나머지가 1 이상일 경우
    else:
      # log2를 취해서 소수가 아닌 부분에 대해
      log2_n10 = int(log2(n10))
      # index를 기록하고
      n2[1].append(log2_n10)
      # 기록한 수는 원래 수에서 제한다.
      n10 -= 2 ** log2_n10

  # 위치가 낮은 것부터 출력한다.
  n2[1].reverse()
  for n2_1s in n2[1]:
    # 1의 위치를 공백으로 구분해서 줄 하나에 출력한다.
    print(n2_1s, end=" ")