
def generate_ints(n):
	for i in range(n):
		yield i



g= generate_ints(4)

print(type(g))

print(next(g))
print(next(g))

print(next(g))
print(next(g))

print(next(g))
