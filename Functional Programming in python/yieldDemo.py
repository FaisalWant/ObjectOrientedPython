# yieldDemo.py

def legs(lat_lon_iter):
	begin= next(lat_lon_iter)   # store  0 first
	print(begin)
	for end in lat_lon_iter:
		yield begin, end
		begin=end
print(list(legs(x for x in range(4))))