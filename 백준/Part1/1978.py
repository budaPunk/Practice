# 첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 
# 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.
N = int(input())
Nums = list(map(int, input().split()))
Nums.sort()
Max_num = Nums[-1]

if 1 in Nums:
  Nums.remove(1)

# 2 ~ 가장큰수 에 대해
for num in range(2, Max_num + 1):
  # 그 배수(2배수 이상) 이 존재하는지 확인한다.
  for mul in range(2, Max_num // num + 1):
    # 2배수 이상이 존재하면 그 수는 소수가 아님
    if num * mul in Nums:
      # 소수가 아니면 리스트에서 제거
      Nums.remove(num * mul)

# 주어진 수들 중 소수의 개수를 출력한다.
print(len(Nums))