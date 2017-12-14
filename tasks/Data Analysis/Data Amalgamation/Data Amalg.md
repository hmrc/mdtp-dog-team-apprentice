Data Amalgamation
====================

**Technology:** Any

**Difficulty**: Easy

**Duration**: 4-6 hours

**Relevant concepts**: Dataframes, arrays, functions

**Prerequisites** N/A

Goal
----
To merge data from multiple csv files and calculate variables from the data.

You should:
* Look at your data
* Import data from all five csv files into your script
* Write a function to merge the data from all the files into one
* Check you haven’t lost any data
* Create a bank-level variable for the difference in bank lending between 1939 and 1933
* Create a fips-level variable for the difference in bank lending between 1939 and 1933
* Display the top and bottom 10 banks and fips codes for positive and negative changes in bank lending 

Stretch goals
------------

* Conduct a merge sort on the bank-level loan_change variable to sort banks from smallest to biggest change. Then plot it on a histogram.
* Conduct a bubble sort on the fips-level loan_change variable to sort banks from smallest to biggest change. Then plot it on a histogram.

Possible approach
---------------
Have a look at the data before you write the script. Make sure you understand the structure of the data and try to preempt some problems you might have, like inconsistent naming between files. You might want to look at the ‘bank id’ column to make sure you will be able to differentiate banks between different states.

(hint) functions will be your friends for this project.
