# ParsingWinter.py

import urllib.request
import xml.etree.ElementTree as xml

def comma_split(text):
	return text.split(",")


def row_iter_kml(file_obj):
	ns_map= {
	"ns0": "http://www.opengis.net/kml/2.2",
	"nsl":"http://www.google.com/kml/ext/2.2"

	}
	doc = xml.parse(file_obj)
	return (
		comma_split(coordinates.text)
		for coordinates in doc.findall("./ns0:Document/ns0:Folder/"
			"ns0:Placemark/ns0:Point/ns0:coordinates",ns_map)
		)

def pick_lat_lon(lon,lat, alt):
	return lat, lon

# will apply pick_lat_lon() function to each row
# *row is used to assign each element of the row three tuple to separate parameters

def lat_lon_kml(row_iter):
	return (pick_lat_lon(*row) for row in row_iter)   
# this line will take one list containing three entries at a time
# creating a pair of points
def pairs(iterable):
	# yields the first pair and pops the next item

	def pair_from(head, iterable_tail):
		nxt= next(iterable_tail)
		yield head, nxt
		
		yield from pair_from(nxt, iterable_tail)

	try:
		return pair_from(next(iterable), iterable)
	except StopIteration:
		return 

def legs(lat_lon_iter):
	begin= next(lat_lon_iter)
	print(begin)
	for end in lat_lon_iter:
		yield begin, end

		begin=end

def legs_filter(lat_lon_iter):
	begin= next(lat_lon_iter)
	for end in lat_lon_iter:
		if some_rule():
			continue
		yield begin,end
		begin=end


def float_from_pair(lat_lon_iter):
	return ((float(lat),float(lon)) for lat, lon in lat_lon_iter)


from math import radians,sin,cos,sqrt, asin

MI=3959 
NM=3440
KM=6371


def haversine(point1,point2, R=NM):
	lat_1, lon_1=point1
	lat_2, lon_2=point2

	D_lat=radians(lat_2-lat_1)
	D_lon=radians(lon_2 -lon_1)
	lat_1= radians(lat_1)
	lat_2= radians(lat_2)
	a= sin(D_lat/2)**2 + cos(lat_1)* cos(lat_2)* sin(D_lon/2)**2

	c=2*asin(sqrt(a))
	return R*c



with urllib.request.urlopen("file:./Winter.kml") as source:
	v0= list(row_iter_kml(source))

	for i in v0:
		print(i)
#$$$$$$$$$$$$$$$$$$$$$$$$$	
	
	# take=lat_lon_kml(v0)     # this returns a generator object
	# while(next(take)):
	# 	var=next(take)
	# 	print(var)
#$$$$$$$$$$$$$$$$$$$$$$$$$$
	trip= iter([(0,0),(1,0),(1,1),(0,1),(0,0)])
	print("Printing the tuple",tuple(pairs(trip)))

#$$$$$$$$$$$$$$$$$$$$$$$$$$

	print( list(legs(x for x in range(4))))    # this is not list comprehension-It is just producing a random list of numbers

	print( legs([1,2,3]))

	trip = [ ("1", "2"), ("2.718", "3.142") ]
	print(tuple( float_from_pair( trip ) ))

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
	print(round(haversine((36.12, -86.67), (33.94, -118.40), R=6372.8), 5))

