import numpy as np

'''
this function bellow return a float value
return 0  -> two points only or many points colinears
return -1 -> the array of points has one or many points that has only x position or y position, instead of (x,y) tuple
'''

def poly_area(P):

	N = len(P)-2

	if N < 1:
		return 0

	for p in P:
		if len(p) != 2:
			return -1

	T = np.zeros([N,3,2])

	for i in range(0,N):
		T[i] = [P[0],P[i+1],P[i+2]]

	A = np.zeros(N)

	for i in range(0,N):

		M = np.zeros([3,3])

		for j in range(0,3):
			M[j] = [T[i][j][0],T[i][j][1],1]

		A[i] = np.absolute(np.linalg.det(M)/2)

	A = np.sum(A)

	return A
