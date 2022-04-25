# 입력의 첫째 줄에 M이, 둘째 줄에 N이 주어진다.
# M과 N은 10,000이하의 자연수이며, M은 N보다 작거나 같다.
M = int(input())
N = int(input())
Nums = [n for n in range(M, N + 1)]

# 1은 소수가 아니다.
if 1 in Nums:
  Nums.remove(1)

# 2 ~ 가장큰수 에 대해
for num in range(2, N + 1):
  # 그 배수(2배수 이상) 이 존재하는지 확인한다.
  for mul in range(2, N // num + 1):
    # 2배수 이상이 존재하면 그 수는 소수가 아님
    if num * mul in Nums:
      # 소수가 아니면 리스트에서 제거
      Nums.remove(num * mul)

# M이상 N이하의 자연수 중 소수인 것을 모두 찾아 
# 첫째 줄에 그 합을, 둘째 줄에 그 중 최솟값을 출력한다. 
if 0 < len(Nums):
  print(sum(Nums))
  print(min(Nums))
# 단, M이상 N이하의 자연수 중 소수가 없을 경우는 첫째 줄에 -1을 출력한다.
else:
  print(-1)