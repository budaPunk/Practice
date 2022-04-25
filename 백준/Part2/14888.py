from cmath import inf

# 첫째 줄에 수의 개수 N(2 ≤ N ≤ 11)가 주어진다.
N = int(input())
# 둘째 줄에는 A1, A2, ..., AN이 주어진다. (1 ≤ Ai ≤ 100) 
Nums = list(map(int, input().split()))
# 셋째 줄에는 합이 N-1인 4개의 정수가 주어지는데, 
# 차례대로 덧셈(+)의 개수, 뺄셈(-)의 개수, 곱셈(×)의 개수, 나눗셈(÷)의 개수이다.
add, sub, mul, div = map(int, input().split())

Max_Result = -inf
Min_Result = inf

def calc(Result, Nums, add, sub, mul, div, idx):
  global Max_Result, Min_Result
  if idx == N:
    if Max_Result < Result:
      Max_Result = Result
    if Result < Min_Result:
      Min_Result = Result
  if 0 < add:
    calc(Result + Nums[idx], Nums, add - 1, sub, mul, div, idx + 1)
  if 0 < sub:
    calc(Result - Nums[idx], Nums, add, sub - 1, mul, div, idx + 1)
  if 0 < mul:
    calc(Result * Nums[idx], Nums, add, sub, mul - 1, div, idx + 1)
  if 0 < div:
    calc(int(Result / Nums[idx]), Nums, add, sub, mul, div - 1, idx + 1)

calc(Nums[0], Nums, add, sub, mul, div, 1)
print(Max_Result)
print(Min_Result)