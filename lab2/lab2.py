from tabulate import tabulate
from math import inf
import math
import numpy as np
import datetime

def Dijkstra(data):
	passed = []
	n = data[0]
	C = data[1]
	start_top = data[2]
	end_top = data[3]
	values = []
	for i in range(n):
		values.append(i)
	start_time = datetime.datetime.now()
	D = [0] * (n)
	for k in range(0, n):
		D[k] = C[start_top][k]
	path = {start_top:0}
	current_top = start_top
	previous_top = 0
	for i in range(n):
		for k in range(0, n):
			D[k] = C[current_top][k]
		for j in range(n):
				if(not math.isnan(D[j]) and D[j] != inf):
					if j not in path and j not in passed:
						path[j] = D[j] + path[current_top]
					elif j in path and j not in passed:
						if D[j] + path[current_top] < path[j] and j != current_top:
							path[j] = D[j] + path[current_top]
		passed.append(current_top)
		minimum = inf
		next = 0
		previous_top = current_top
		for k in range(n):
			try:
				if (path[k] < minimum) and (k not in passed):
					minimum = path[k]
					next = k
			except KeyError:
				pass
		current_top = next

	print()
	print("-----| Length of shortest path from start top ", start_top, " to end top ", end_top, " is : ", path[end_top], "|-----")
	print("Algorithm takes %s microseconds to execute" % (datetime.datetime.now() - start_time).microseconds)

	print("-| To exit programm enter 0 |-")
	print("-| To restart programm enter 1 |-")
	print("-| To save graph and choose another method and start-end tops enter 2 |-")

	exit = ''
	while exit != '0' and exit != '1' and exit != '2':
		exit = input()
	if exit == '0':
		return 0
	elif exit == '1':
		print(end="\n\n")
		start([])
	elif exit == '2':
		print("--- Your graph ---")
		print(tabulate(C))
		start([C])

def Floyd_Warshall(data):
	n = data[0]
	C = data[1]
	graph = data[1]
	start_top = data[2]
	end_top = data[3]
	start_time = datetime.datetime.now()
	for k in range(n):
		for i in range(n):
			for j in range(n):
				C[i][j] = min(C[i][j], C[i][k] + C[k][j])

	print("-----| Length of shortest path from start top ", start_top, " to end top ", end_top, " is : ", C[start_top][end_top], "|-----")
	print("Algorithm takes %s microseconds to execute" % (datetime.datetime.now() - start_time).microseconds)

	print("-| To exit programm enter 0 |-")
	print("-| To restart programm enter 1 |-")
	print("-| To save graph and choose another method and start-end tops enter 2 |-")
	exit = ''
	while exit != '0' and exit != '1' and exit != '2':
		exit = input()
	if exit == '0':
		return 0
	elif exit == '1':
		print(end="\n\n")
		start([])
	elif exit == '2':
		print("--- Your graph ---")
		print(tabulate(graph))
		start([graph])

def start(data):
	print("Program to find shortest path between 2 tops in graph")
	method = 0
	while method != 1 and method != 2:
		print("Choose method (enter 1 to chose Dijkstra, enter 2 to choose Floyd-Warshall) : ", end="")
		method = input()
		try:
			method = int(method)
			if method > 0:
				pass
		except ValueError:
			continue
	if len(data) == 0:
		while True:
			print("Enter number of tops in graph:", end="")
			n = input()
			try:
				n = int(n)
				if n > 0:
					break
			except ValueError:
				continue

		C = []
		row = []
		print()
		print("Enter matrix of weights that represent your graph")
		print("Matrix must be symmetric, if tops is not connected enter inf")
		stop = True
		while stop is True:
			C = []
			for i in range(n):
				for j in range(n):
					print("Enter [",i+1,"][",j+1,"] element : ", end="")
					while True:
						k = input()
						try:
						    int(k)
						    is_dig = True
						except ValueError:
						    is_dig = False
						if is_dig:
							if i == j:
								row.append(0)
							else:
								row.append(int(k))	
							break
						elif k == 'inf':
							if i == j:
								row.append(0)
							else:
								row.append(inf)
							break
						else:
							print("Incorrect input. Input must contain only numbers or inf.")
				C.append(row)
				row = []
			print("--- Your graph ---")
			print(tabulate(C))

			for i in range(n):
				for j in range(n):
					if C[i][j] != C[j][i]:
						print("Input matrix is not symmetric. Try another one : ")
						break
				else:
					stop = False
				break
	else:
		C = data[0]
		n = len(C)

	print("Enter number of start top: ", end="")
	while True:
		start_top = input()
		try:
			start_top = int(start_top) - 1
			if start_top > n:
				print("Number is too big. It must be less than numbers of tops in graph.")
				continue
			if start_top >= 0:
				break
			if start_top < 0:
				print("Input must be positive integer")
				continue
		except ValueError:
			print("Input must be positive integer")
			continue

	print("Enter number of end top: ", end="")
	while True:
		end_top = input()
		try:
			end_top = int(end_top) - 1
			if end_top > n:
				print("Number is too big. It must be less than numbers of tops in graph.")
				continue
			if end_top >= 0:
				break
			if end_top < 0:
				print("Input must be positive integer")
		except ValueError:
			print("Input must positive integer")
			continue

	check([method, n, C, start_top, end_top])

def check(res):
	method = res[0]
	res.remove(res[0])

	if method == 1:
		Dijkstra(res)
	if method == 2:
		Floyd_Warshall(res)

start([])
