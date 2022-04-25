# a c i n t


# 첫째 줄에 단어의 개수 N과 K가 주어진다. 
# N은 50보다 작거나 같은 자연수이고, 
# K는 26보다 작거나 같은 자연수 또는 0이다.
N, K = map(int, input().split())

# 둘째 줄부터 N개의 줄에 남극 언어의 단어가 주어진다. 
# 단어는 영어 소문자로만 이루어져 있고, 
# 길이가 8보다 크거나 같고, 15보다 작거나 같다.
antartica_dict = []
for _ in range(N):
  antartica_dict.append(input().strip())
print(antartica_dict)