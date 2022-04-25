def who_is_real(dwarfs:list):
  # 얼마나 더 큰지 계산
  taller = sum(dwarfs) - 100
  for no1 in range(len(dwarfs)):
    for no2 in range(no1):
      # 더 큰만큼에 딱 맞는 두명을 찾아내면
      if dwarfs[no1] + dwarfs[no2] == taller:
        # 난쟁이 리스트에서 제거
        # 인덱스가 변하지 않도록 순서가 중요함.
        # pop back => pop front
        dwarfs.pop(no1)
        dwarfs.pop(no2)
        return dwarfs

# 아홉 개의 줄에 걸쳐 난쟁이들의 키가 주어진다. 
# 주어지는 키는 100을 넘지 않는 자연수이며, 아홉 난쟁이의 키는 모두 다르다
dwarfs = []
for _ in range(9):
  dwarfs.append(int(input()))
dwarfs = who_is_real(dwarfs)
# 일곱 난쟁이의 키를 오름차순으로 출력한다. 
# 일곱 난쟁이를 찾을 수 없는 경우는 없다.
dwarfs.sort()
for dwarf in dwarfs:
  print(dwarf)