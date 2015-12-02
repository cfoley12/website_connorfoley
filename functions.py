import numpy


def mean():

	for value in dict[time]:
		split(value)
		sumMins += mins
		sumSecs += secs

	# Multiply mins by 60 to get seconds
	totalSum = sumSecs + (sumMins * 60)
	mean = (totalSum / numRunners)

	return mean

def splitter(time):

	time_list = time.split(":", 2)
	mins = int(time_list[0])
	secs = float(time_list[1])
	time_in_secs = float(mins_to_secs(mins, secs))
	return time_in_secs

def mins_to_secs(mins, secs):

	temp_time = ((mins * 60) + secs)
	return temp_time

def st_dev_michigan(myList1, myList2, myList3, myList4, 
	myList5, myList6, myList7, myList8, myList9, myList10):

	mean1 = mean_of_list(myList1)
	mean2 = mean_of_list(myList2)
	mean3 = mean_of_list(myList3)
	mean4 = mean_of_list(myList4)
	mean5 = mean_of_list(myList5)
	mean6 = mean_of_list(myList6)
	mean7 = mean_of_list(myList7)
	mean8 = mean_of_list(myList8)
	mean9 = mean_of_list(myList9)
	mean10 = mean_of_list(myList10)
	mean_list = {mean1, mean2, mean3, mean4, mean5, mean6, mean7, mean8, mean9, mean10}
	
	st_dev_michigan = numpy.std(mean_list)
	return st_dev_michigan

def mean_michigan(myList1, myList2, myList3, myList4, 
	myList5, myList6, myList7, myList8, myList9, myList10):

	mean1 = mean_of_list(myList1)
	mean2 = mean_of_list(myList2)
	mean3 = mean_of_list(myList3)
	mean4 = mean_of_list(myList4)
	mean5 = mean_of_list(myList5)
	mean6 = mean_of_list(myList6)
	mean7 = mean_of_list(myList7)
	mean8 = mean_of_list(myList8)
	mean9 = mean_of_list(myList9)
	mean10 = mean_of_list(myList10)
	
	mean_michigan = mean1 + mean2 + mean3 + mean4 + mean5 + mean6 + mean7 + mean8 + mean9 + mean10

	return mean_michigan

def mean_of_list(myList):
	
	sumList = 0

	for row in myList:
		sumList += row[6]
	mean_course = (sumList / len(myList))
	return mean_course

def std_dev_course(myList):

	std_dev_course = numpy.std(zip(*myList)[6])
	return std_dev_course

def z_score_course(time_in_secs, mean_course, std_dev_course):

	z_score_course = (time_in_secs - mean_course) / (std_dev_course)

	return z_score_course

def z_score_michigan(mean_course, mean_michigan, std_dev_michigan):

	z_score_michigan = (mean_course - mean_michigan) / (std_dev_michigan)

	return z_score_michigan

def calc_speed_rating(z_score_michigan, z_score_course):

	speed_rating = 100 + (z_score_michigan * z_score_course * 12)
	return speed_rating

if __name__ == "__main__":
	
	time = "12:34"
	splitter(time)

	test_list = [
	[0, 0, 0, 0, 0, 0, 1],
	[0, 0, 0, 0, 0, 0, 2],
	[0, 0, 0, 0, 0, 0, 3],
	[0, 0, 0, 0, 0, 0, 4],
	[0, 0, 0, 0, 0, 0, 5]
	]
	
	mean = mean_of_list(test_list)

	print mean

	











