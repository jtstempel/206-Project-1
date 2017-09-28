import os
import filecmp
import datetime

# Link to my Project 1 Repository on Github: https://github.com/jtstempel/206-Project-1

# Ben Crabtree, Ava Weiner and I collaborated on some of these tasks. We discussed what the 
# task was generally asking of us and how we might best go about addressing it. 

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
	my_header = my_file.readline().strip().split(',') 	# attempting to get header (only the first line) from file
	big_list_data = []									# initializing list I want to end up with
	reading_lines = my_file.readlines()
	for my_data in reading_lines:
		list_data = my_data.strip().split(',')							
		my_dict_data = {}
		match_order = 0									
		for key in my_header:							# iterating through each dictionary in the list to grab
			my_dict_data[key] = list_data[match_order]
			match_order += 1 							# making sure that keys from dictionary match up to the corresponding piece of data
		big_list_data.append(my_dict_data)  			# appending keys from dictionary to list (with data)
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
	dict_of_grades = {'Senior': 0, 'Junior': 0, 'Sophomore': 0, 'Freshman': 0}

	for an_item in data:
		if an_item['Class'] == 'Senior':
			dict_of_grades['Senior'] += 1
		elif an_item['Class'] == 'Junior':
			dict_of_grades['Junior'] += 1
		elif an_item['Class'] == 'Freshman':
			dict_of_grades['Freshman'] += 1
		elif an_item['Class'] == 'Sophomore':
			dict_of_grades['Sophomore'] +=1

	list_numbers.append(('Senior', dict_of_grades['Senior']))
	list_numbers.append(('Junior', dict_of_grades['Junior']))
	list_numbers.append(('Freshman', dict_of_grades['Freshman']))
	list_numbers.append(('Sophomore', dict_of_grades['Sophomore']))

	return sorted(list_numbers, reverse = True, key = lambda x: x[1])



# Find the most common day of the year to be born
def findDay(a):
# Input: list of dictionaries
# Output: Return the day of month (1-31) that is the
# most often seen in the DOB

	#Your code here:
	dict_DOB_counts = {}
	#list_counts = []

	for my_item in a:
		day = my_item['DOB'].split('/')[1]
		if day in dict_DOB_counts:
			dict_DOB_counts[day] += 1
		elif day not in dict_DOB_counts:
			dict_DOB_counts[day] = 1 

	return int(sorted(dict_DOB_counts, key = lambda x: dict_DOB_counts[x], reverse = True)[0])


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

