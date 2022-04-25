from cmath import inf

# 첫째 줄에 테스트 케이스의 개수 T(1 ≤ T ≤ 1,000)가 주어진다. 
T = int(input())

answers = []
for t in range(T):
  # 각 테스트 케이스는 한 줄로 이루어져 있고, 
  # 배열 A의 원소 10개가 공백으로 구분되어 주어진다. 
  # 이 원소는 1보다 크거나 같고, 1,000보다 작거나 같은 자연수이다.
  A = list(map(int, input().split()))

  first = -inf
  second = -inf
  third = -inf
  
  for a in A:
    if first < a:
      first, second, third = a, first, second
    elif second < a:
      second, third = a, second
    elif third < a:
      third = a
    else:
      pass
  answers.append(third)

for answer in answers:
  print(answer)