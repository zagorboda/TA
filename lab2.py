from numpy import nan
from math import inf
import math
import numpy as np
n = 4
a,b,c,d = range(n)
values = [a,b,c,d]
start_top = 1
# N = [
# 	{b:3}, 			# a
# 	{a:3,c:1,d:7},  # b
# 	{b:1,d:2}, 		# c
# 	{b:7,c:2} 		# d
# ]
C = [[nan,	3,		2,	12],
	 [3,	nan,	1,		7],
	 [2,	1,		nan,	2],
	 [12, 	7, 		2, 		nan]]

passed = []

D = [0] * (n)
for k in range(0, n):
	D[k] = C[start_top][k]
path = {start_top:0}
current_top = start_top
previous_top = 0
for i in range(n):
	for k in range(0, n):
		D[k] = C[current_top][k]
	# print(D)
	for j in range(n):
			if(not math.isnan(D[j]) and D[j] != inf):
				if j not in path and j not in passed:
					path[j] = D[j] + path[current_top]
				elif j in path and j not in passed:
					print("D[j] = ", D[j])
					print("path[j] = ", path[j])
					print("path[current_top] = ", path[current_top])
					if D[j] + path[current_top] < path[j] and j != current_top:
						path[j] = D[j] + path[current_top]
	passed.append(current_top)
	print("Passed = ", passed)
	print(path)
	minimum = inf
	next = 0
	previous_top = current_top
	for k in range(n):
		print(k)
		try:
			if (path[k] < minimum) and (k not in passed):
				minimum = path[k]
				next = k
		except KeyError:
			pass
	print(next)
	current_top = next
	print("Next top = ", current_top)
print(D)
print(path)
print(passed)

# current_top  = start_top
# next_tops = [current_top]
# passed_tops = []
# path = {}
# print("D = ", D)
# for i in range(n):
# 	for k in range(0, n):
# 		D[k] = C[current_top][k]
# 	next_tops.clear()
# 	passed_tops.append(current_top)
# 	print("Pass = ", passed_tops)
# 	for j in range(n):
# 		if(not math.isnan(D[j]) and D[j] != inf):
# 			path[j] = D[j] # min(D[j], D[w] + C[w][j])
# 			if values[j] not in passed_tops:
# 				next_tops.append(values[j])
# 			print(next_tops)
# 	current_top = min(next_tops)
# 	# current_top = print(list(path.keys())[list(path.values()).index(min(path.values()))])
# 	print("Next top = ", current_top)
# 	print(path)

# for i in range(0, n):
# 	minimum = D[0]
# 	for j in range(4):
# 		if D[j] < minimum:
# 			minimum = j
# 	w = minimum
# 	print(w)
# 	for v in V:
# 		D[v] = min(D[v], D[w] + C[w][v])
# 		curent_D.append(min(D[v], D[w] + C[w][v]))
# 		print("Current D = ", curent_D)
# 	if (len(V) > 0):
# 		V.remove(w)
# 		print("V = ", V)
# 	curent_D.clear()
# print(D)
