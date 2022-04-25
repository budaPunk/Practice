# 연산 bad
#           5
#      4          3
#   3     2    2     1
#  2 1   1 0  1 0  
# 1 0
# fibo(5)를 구하는데만 해도 fibo(1)이 5번, fibo(0)이 3번
# 연산되어야 하는 소요가 있습니다.
def fibo_notGood(n):
  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    return fibo_notGood(n-1) + fibo_notGood(n-2)

# 연산 good 메모리 bad
# 이미 구했던 연산을 반복하지 않아도 되지만 O(n) 메모리가 필요합니다.
def fibo_Good(n):
  fibo_list = []
  for idx in range(n + 1):
    if idx == 0:
      fibo_list.append(0)
    elif idx == 1:
      fibo_list.append(1)
    else:
      fibo_list.append(fibo_list[-2] + fibo_list[-1])
  return fibo_list[-1]

# 연산 good 메모리 good
# 이미 구했던 연산을 반복하지 않으며, 메모리도 효율적입니다.
def fibo_Best(n):
  curr, next = 0, 1
  for idx in range(n):
    curr, next = next, curr + next
  return curr

# 첫째 줄에 n이 주어진다. n은 20보다 작거나 같은 자연수 또는 0이다.
n = int(input())
# 첫째 줄에 n번째 피보나치 수를 출력한다.
print(fibo_notGood(n))
print(fibo_Good(n))
print(fibo_Best(n))