# 첫째 줄에는 두 개의 자연수가 주어진다. 
# 이 둘은 10,000이하의 자연수이며 사이에 한 칸의 공백이 주어진다.
Nums = list(map(int, input().split()))
Nums.sort()

# 최대공약수는 더 작은수의 약수중에 찾는게 좋다고 생각됨.
GCD = 0
for n in range(Nums[0], 0, -1):
  if Nums[0] % n == 0 and Nums[1] % n == 0:
    GCD = n
    break

# 최소공배수는 더 큰 수의 배수중에 찾는게 좋다고 생각된다.
LCM = 0
multiple = 1
while True:
  if (Nums[1] * multiple) % Nums[0] == 0:
    LCM = Nums[1] * multiple
    break
  else:
    multiple += 1

# 첫째 줄에는 입력으로 주어진 두 수의 최대공약수를, 
# 둘째 줄에는 입력으로 주어진 두 수의 최소 공배수를 출력한다.
print(GCD)
print(LCM)