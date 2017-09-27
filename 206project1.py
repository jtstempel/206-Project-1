import os
import filecmp
import datetime

def getData(file):
#Input: file name
#Ouput: return a list of dictionary objects where 
#the keys will come from the first row in the data.

#Note: The column headings will not change from the 
#test cases below, but the the data itself will 
#change (contents and size) in the different test 
#cases.

	#Your code here:
	my_file = open(file, 'r')
	my_header = my_file.readline().strip().split(',')
	big_list_data = []

	for my_data in my_file.readlines():
		my_dict_data = {}
		my_index = 0
		list_data = my_data.strip().split(',')
		for key in my_header:
			my_dict_data[key] = list_data[my_index]
			my_index += 1
		big_list_data.append(my_dict_data)
	return big_list_data


#Sort based on key/column
def mySort(data,col):
#Input: list of dictionaries
#Output: Return a string of the form firstName lastName

	#Your code here:
	my_sorted_list = sorted(data, key = lambda x: x[col])
	return my_sorted_list[0]['First'] + ' ' + my_sorted_list[0]['Last']

#Create a histogram
def classSizes(data):
# Input: list of dictionaries
# Output: Return a list of tuples ordered by
# ClassName and Class size, e.g 
# [('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)]

	#Your code here:
	list_numbers = []
	number_senior = 0
	number_junior = 0
	number_freshman = 0
	number_sophomore = 0
	for an_item in data:
		if an_item['Class'] == 'Senior':
			number_senior += 1
		elif an_item['Class'] == 'Junior':
			number_junior += 1
		elif an_item['Class'] == 'Freshman':
			number_freshman += 1
		elif an_item['Class'] == 'Sophomore':
			number_sophomore +=1

	list_numbers.append(('Senior', number_senior))
	list_numbers.append(('Junior', number_junior))
	list_numbers.append(('Freshman', number_freshman))
	list_numbers.append(('Sophomore', number_sophomore))

	return sorted(list_numbers, reverse = True, key = lambda x: x[1])



# Find the most common day of the year to be born
def findDay(a):
# Input: list of dictionaries
# Output: Return the day of month (1-31) that is the
# most often seen in the DOB

	#Your code here:
	dict_DOB_counts = {}
	for my_item in a:
		day = my_item['DOB'].split('/')[1]
		if day not in dict_DOB_counts:
			dict_DOB_counts[day] = 1
		else:
			dict_DOB_counts[day] += 1 
	list_counts = []
	for my_key in dict_DOB_counts.keys():
		new_tuple = (my_key, dict_DOB_counts[my_key])
		list_counts.append(new_tuple)
	most_common_day = sorted(list_counts, reverse = True, key = lambda x: x[1])
	return int(most_common_day[0][0])


# Find the average age (rounded) of the Students
def findAge(a):
# Input: list of dictionaries
# Output: Return the day of month (1-31) that is the
# most often seen in the DOB

	#Your code here:
	list_of_student_ages = []
	for my_student in a[1:]:
		month, day, year = my_student['DOB'].split('/')
		month_current = int(datetime.date.today().month)
		day_current = int(datetime.date.today().day)
		year_current = int(datetime.date.today().year)
		
		if (day_current >= int(day)) and (month_current >= int(month)):
			list_of_student_ages.append(year_current - int(year))
		else:
			list_of_student_ages.append(year_current - int(year) + 1)

	return round((sum(list_of_student_ages)/len(list_of_student_ages)), 0)


#Similar to mySort, but instead of returning single
#Student, all of the sorted data is saved to a csv file.
def mySortPrint(a,col,fileName):
#Input: list of dictionaries, key to sort by and output file name
#Output: None

	#Your code here:
	my_csv = open(fileName, 'w')
	my_sorted_list = sorted(a, key = lambda x: x[col])
	for thing in my_sorted_list:
		new_list = []
		for x in thing.values():
			new_list.append(x)
		my_line = ','.join(new_list[:3])
		my_csv.write(my_line + '\n')
	my_csv.close()
	return None

#Ben Crabtree, Ava Weiner and I collaborated on some of these tasks. 


################################################################
## DO NOT MODIFY ANY CODE BELOW THIS
################################################################

## We have provided simple test() function used in main() to print what each function returns vs. what it's supposed to return.
def test(got, expected, pts):
  score = 0;
  if got == expected:
    score = pts
    print(" OK ",end=" ")
  else:
    print (" XX ", end=" ")
  print("Got: ",got, "Expected: ",expected)
  return score


# Provided main() calls the above functions with interesting inputs, using test() to check if each result is correct or not.
def main():

	total = 0
	print("Read in Test data and store as a list of dictionaries")
	data = getData('P1DataA.csv')
	data2 = getData('P1DataB.csv')
	total += test(type(data),type([]),40)
	print()
	print("First student sorted by First name:")
	total += test(mySort(data,'First'),'Abbot Le',15)
	total += test(mySort(data2,'First'),'Adam Rocha',15)

	print("First student sorted by Last name:")
	total += test(mySort(data,'Last'),'Elijah Adams',15)
	total += test(mySort(data2,'Last'),'Elijah Adams',15)

	print("First student sorted by Email:")
	total += test(mySort(data,'Email'),'Hope Craft',15)
	total += test(mySort(data2,'Email'),'Orli Humphrey',15)

	print("\nEach grade ordered by size:")
	total += test(classSizes(data),[('Junior', 28), ('Senior', 27), ('Freshman', 23), ('Sophomore', 22)],10)
	total += test(classSizes(data2),[('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)],10)

	print("\nThe most common day of the year to be born is:")
	total += test(findDay(data),13,10)
	total += test(findDay(data2),26,10)
	
	print("\nThe average age is:")
	total += test(findAge(data),39,10)
	total += test(findAge(data2),41,10)

	print("\nSuccessful sort and print to file:")
	mySortPrint(data,'Last','results.csv')
	if os.path.exists('results.csv'):
		total += test(filecmp.cmp('outfile.csv', 'results.csv'),True,10)


	print("Your final score is: ",total)

#Standard boilerplate to call the main() function that tests all your code.
if __name__ == '__main__':
    main()
