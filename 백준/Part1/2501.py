# 첫째 줄에 N과 K가 빈칸을 사이에 두고 주어진다.
N, K = map(int, input().split())

# 만일 N의 약수의 개수가 K개보다 적어서 
# K번째 약수가 존재하지 않을 경우에는 0을 출력하시오.
Res = 0

for n in range(1, N + 1):
  if N % n == 0:
    K -= 1
  if K == 0:
    res = n
    break

# 첫째 줄에 N의 약수들 중 K번째로 작은 수를 출력한다.
print(Res)