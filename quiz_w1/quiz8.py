import math

def poly(n, s):
	return ((0.25 * n * s**2) / math.tan((math.pi/n)))
	#return polygon

print poly(7, 3)