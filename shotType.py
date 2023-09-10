import csv
# area = {}
sections = {}
# for x in range(-250, 250):
# 	for y in range(-50, 400):
# 		if(x not in area):
# 			area[x] = {}
# 		if(y < 100 and x <= 250 and x > 225):
# 			area[x][y] = "Left Corner"
# 		elif(y < 100 and x < 225 and x >= -250):
# 			area[x][y] = "Right Corner"
# 		elif(y > 100 and x < -75):
# 			area[x][y] = "Left Wing"
# 		elif(y > 100 and x > -75 and x < 75):
# 			area[x][y] = "Top of the key"
# 		elif(y > 100 and x > 75):
# 			area[x][y] = "Right Wing"
# 		else:
# 			area[x][y] = "Random"
# 		sections[area[x][y]] = [0,0]
# print(area)
with open("Data/originalShotData.csv") as csv_file:
	csv_reader = csv.reader(csv_file)
	i=0
	typeToIndex, indexToType = {}, {}
	for line in csv_reader:
		for dataType in line:
			typeToIndex[dataType] = i
			indexToType[i] = dataType
			i+=1
		break
	i=0
	points = {}
	for line in csv_reader:
		x = int(line[typeToIndex['X Location']])
		y = int(line[typeToIndex['X Location']])
		if line[typeToIndex['Action Type']] not in points:
			points[line[typeToIndex['Action Type']]] = [0,0]
		if line[typeToIndex['Shot Zone Basic']] not in points:
			points[line[typeToIndex['Shot Zone Basic']]] = [0,0]
		if(line[typeToIndex['Shot Made Flag']] == "1"):
			if line[typeToIndex['Shot Type']] == "2PT Field Goal":
				points[line[typeToIndex['Action Type']]][0]+=2
				points[line[typeToIndex['Shot Zone Basic']]][0]+=2
				if(x in area and y in area[x]):
					sections[area[x][y]][0] += 2
			else:
				points[line[typeToIndex['Action Type']]][0]+=3
				points[line[typeToIndex['Shot Zone Basic']]][0]+=3
				if(x in area and y in area[x]):
					sections[area[x][y]][0] += 3
		points[line[typeToIndex['Action Type']]][1] += 1
		points[line[typeToIndex['Shot Zone Basic']]][1] += 1
		if(x in area and y in area[x]):
			sections[area[x][y]][1] += 1
	for i in sections.keys():
		print(sections)
		print(i, sections[i][0] / sections[i][1])


		