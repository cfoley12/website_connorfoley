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
	print time_in_secs
	return time_in_secs

def mins_to_secs(mins, secs):

	temp_time = ((mins * 60) + secs)
	return temp_time

def st_dev_course_means(myList1, myList2, myList3, myList4, 
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

def mean_of_list(myList):
	
	for i in myList[i][3]:
		sumList += myList[i][3]
	mean = (sumList / len(input[3]))
	return mean

def std_dev_course(myList):

	std_dev_course = numpy.std(zip(*myList)[3])
	return std_dev_course

def calc_speed_rating(st_dev_michigan, std_dev_course):

	speed_rating = 100 + (std.dev_course * st_dev_michigan * 12)
	return speed_rating

if __name__ == "__main__":
	
	time = "12:34"
	
	splitter(time)











