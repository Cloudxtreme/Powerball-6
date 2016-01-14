import csv
import math
from collections import Counter
import operator

#Common ball numbers and pairs/triplets for Powerball Lottery

#takes in a csv file of winning numbers
def import_data(title = 'lotto.csv'):
	lst = []
	reader = csv.reader(open(title, 'rU'), dialect=csv.excel_tab)
	for arr in reader:
		row = arr[0].split(',')
		nums = row[1].split(' ')
		lst.append(nums)
	red = []
	white = []
	for arr in lst:
		red.append(arr[5])
		white.append(arr[0])
		white.append(arr[1])
		white.append(arr[2])
		white.append(arr[3])
		white.append(arr[4])
	whitecount = Counter(white)
	print("Most common white balls:")
	print(whitecount)
	redcount = Counter(red)
	print("Most common red balls:")
	print(redcount)
	dicti2 = {}
	for arr in lst:
		for y in arr:
			for x in arr:
				if x!=y:
					dicti2[(x,y)]=check_count(lst,(x,y))
	sorted_d2 = sorted(dicti2.items(), key=operator.itemgetter(1))
	sorted_d2.reverse()
	for x in sorted_d2:
		for y in sorted_d2:
			if x[0][0]==y[0][1] and x[0][1]==y[0][0]:
				sorted_d2.remove(x)
	print("Most common pairs:")
	print(sorted_d2[0:30])
	dicti = {}
	for arr in lst:
		for y in arr:
			for x in arr:
				for z in arr:
					if x!=y and y!=z and x!=z:
						dicti[(x,y,z)]=check_count2(lst,(x,y,z))
	sorted_d = sorted(dicti.items(), key=operator.itemgetter(1))
	sorted_d.reverse()
	print("Most common triplets:")
	print(sorted_d[0:30])
	print("Total data points: "+str(len(lst)))

def check_count(lst,pair):
	count = 0
	x,y = pair
	for arr in lst:
		if x in arr and y in arr:
			count+=1
	return count

def check_count2(lst,triplet):
	count = 0
	x,y,z = triplet
	for arr in lst:
		if x in arr and y in arr and z in arr:
			count+=1
	return count
