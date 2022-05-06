from itertools import combinations

l = [1,2,3]
for i in combinations(l,2):
	print(i)

from itertools import combinations_with_replacement

l = ['A', 'B', 'C']
for i in combinations_with_replacement(l,3):
	print(i)