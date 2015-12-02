def mean():

	for value in dict[time]:
		split(value)
		sumMins += mins
		sumSecs += secs

	# Multiply mins by 60 to get seconds
	totalSum = sumSecs + (sumMins * 60)
	mean = (totalSum / numRunners)

	return mean

def splitter():

	time = "12:34"
	
	time_list = time.split(":", 2)
	
	mins = int(time_list[0])
	secs = float(time_list[1])

	time_in_secs = float(mins_to_secs(mins, secs))
	print time_in_secs

def mins_to_secs(mins, secs):

	temp_time = ((mins * 60) + secs)
	return temp_time

#def list_time_conversion():

	#temp_dict = {}
	#for value in my_dict():
		#temp_dict[][time]
		#for t in temp_dict[t][time]



if __name__ == "__main__":
	splitter()











