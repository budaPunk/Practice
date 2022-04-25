from copy import deepcopy

# 첫 번째 줄에는 2차원 세계의 세로 길이 H와
# 2차원 세계의 가로 길이 W가 주어진다. (1 ≤ H, W ≤ 500)
H, W = map(int, input().split())

# 두 번째 줄에는 블록이 쌓인 높이를 의미하는 0이상 H이하의 정수가 
# 2차원 세계의 맨 왼쪽 위치부터 차례대로 W개 주어진다.
Before_Rain = list(map(int, input().split()))
After_Rain = deepcopy(Before_Rain)

for w_idx in range(1, W - 1):
  # left_max 랑 right_max 중 더 낮은녀석 만큼 물이 고일 수 있다.
  left_max = max(Before_Rain[:w_idx])
  right_max = max(Before_Rain[w_idx + 1:])
  # 현제 블록보다 높이 물이 고일 수 있다면 수위가 높이임.
  After_Rain[w_idx] = max(After_Rain[w_idx], min(left_max, right_max))
  #print(Before_Rain[:w_idx], After_Rain[w_idx], Before_Rain[w_idx + 1:])

# 2차원 세계에서는 한 칸의 용량은 1이다. 고이는 빗물의 총량을 출력하여라.
# 빗물이 전혀 고이지 않을 경우 0을 출력하여라.
print(sum(After_Rain) - sum(Before_Rain))