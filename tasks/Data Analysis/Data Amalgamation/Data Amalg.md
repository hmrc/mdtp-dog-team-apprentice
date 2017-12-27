Data Amalgamation
====================

***AVAILABLE***

**Technology:** Any

**Difficulty**: Easy

**Duration**: 12-16 hours

**Relevant concepts**: Dataframes, arrays, functions

**Prerequisites** N/A

Goal
----
To merge data from multiple csv files and calculate variables from the data.

You should:
* Look at your data
* Save each excel sheet as a csv file (e.g. NY_1939.csv, NY_1933.csv)
* Import data from all five csv files into your script
* Write a function to merge the data from all the files into one, then save this as a merged csv file
* Count the total number of banks in 1933 and 1939 (to check n against merged file)
* Compare the total number of banks against the rows in the merged file to check you haven't lost any data
* Calculate 'loans' divided by 'assets' for each bank in 1933, then put the result in a column called 'loan-asset ratio'
* Print the bottom 10 banks and corresponding loan-asset ratios
* Create a bar chart of the top 10 banks and corresponding loan-asset ratios
* Split the merged dataset into two csv files - one for 1933 and one for 1939


Stretch goals
------------

* Conduct a merge sort on the loan-asset variable to sort banks from smallest to biggest. Then plot it on a histogram.
* Conduct a bubble sort on the loan-asset variable to sort banks from smallest to biggest. Then plot it on a histogram.

Possible approach
---------------
Have a look at the data before you write the script. Make sure you understand the structure of the data and try to preempt some problems you might have, like inconsistent naming between files. You might want to look at the ‘bank id’ column to make sure you will be able to differentiate banks between different states.

(hint) functions will be your friends for this project.
