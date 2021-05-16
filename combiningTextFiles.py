# Python program to demonstrate merging of multiple files
import os.path
from os import path

# List of file name with own path to store multiple '.txt' files
listOfTextFileNames = []

# First loop --> check the file that is base text file
for x in range(1,102):
	# Check the file which is exist or not
	# If it is true, add to file name list
	for cnt in range(0,14):
		if (path.exists("D:\\Bitirme_2021\Splitted Texts\pandemi_Metinleri\\" + "p" + str(cnt) + "_" + str(x) + "_pandemi.txt")):
			listOfTextFileNames.append("D:\\Bitirme_2021\Splitted Texts\pandemi_Metinleri\\"+"p"+str(cnt)+"_"+str(x)+"_pandemi.txt")

	# When terminated second loop,
	# Open a new '.txt' file with appropriate name to store all splitted text files
	with open('D:\\Bitirme_2021\DATASET\\tekparca_pandemi\\' + str(x) + '_pandemi.txt', 'w') as outfile:

		# Iterate through list
		for names in listOfTextFileNames:
			# Open each file in read mode
			with open(names) as infile:
				# read the data from list
				# and write it in opened file
				outfile.write(infile.read())

			# Add white space character
			# to separate from next line
			outfile.write(" ")
	# Clear the list to start from scratch
	listOfTextFileNames.clear()



