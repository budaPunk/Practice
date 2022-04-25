from cmath import inf

Curr_Passenger = 0
Max_Passenger = -inf

for _ in range(10):
  # 각 역에서 내린 사람 수와 탄 사람 수가 빈칸을 사이에 두고 
  # 첫째 줄부터 열 번째 줄까지 역 순서대로 한 줄에 하나씩 주어진다.
  off, on = map(int, input().split())
  Curr_Passenger -= off
  Curr_Passenger += on
  # 현제 역대급으로 많다면 최대 승객수 갱신
  if Max_Passenger < Curr_Passenger:
    Max_Passenger = Curr_Passenger
# 첫째 줄에 최대 사람 수를 출력한다.
print(Max_Passenger)