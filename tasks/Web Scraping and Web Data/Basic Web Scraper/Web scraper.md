Web Scraper
====================

***ONGOING IN PAIRS***

**Technology:** Any

**Difficulty**: Easy

**Duration**: 4-6 hours

**Relevant concepts**: hmtl parsing/xpaths, schedules, saving data, plotting data

**Prerequisites** Web Scraper Workshop

Goal
----
Produce a script or program which extracts weather data from a site like bbc weather or the met office on a regular basis and displays it.

The script should:
* Pull weather data on multiple cities from a webpage
* Store the data locally
* Set up a schedule to extract data regularly and store it
* Create a display for the weather data over time

Stretch goals
------------

* Define criteria or set a threshold for
* Compare weather data against the monthly average for each city.
* Compare weather data forecasts against actual temperature recordings. As a further extension, identify an uncertainty threshold around the forecast data based on days from the current date.

Possible approach
---------------
This program can be implemented fully using the terminal and python. Lxml, requests, numpy and pandas are all useful packages for this project.

Gotchas
-------
Taking BBC Weather as an example:
BBC Weather gives you the weather for today and the upcoming four days (5 days in total). For each day there is a minimum and maximum temperature. This is fine, except that when a city is at night there is no maximum temperature, only a minimum. This means you will have missing data any time a city you want the weather for is currently at night.
This causes a few problems...

* Firstly, when you get weather data and put it in a dataframe you will need to account for when the length of your maximum data is four (instead of five). You will need to use conditional logic to handle when you have a list of length four rather than five in your dataframe
* Secondly, when you try to make a graph of this data you will face the same issue
* If you had two cities, e.g. London and Sydney, it is likely one will be day time and one will be night time. You will need to have a way for your graph function to handle two different maximum lengths
* You will also need to consider how you will put missing data into a graph. Using numpy you may already have either np.zeros or np.empty
* Using np.empty will give you None in replacement of missing data, this cannot be put into a graph. Using np.zeros will give you a 0 in replacement of missing data, this is also an issue as it can be mistaken for actual data
* By doing something like -999*np.ones this will leave any missing data as -999, preventing any mixing up with actual dataframe

Another issue you may come across is how to deal with the y axis when making your graph. You will need to use a matplotlib function called set_ylim (set the y axis limit). You can use this to set your minimum or 0 as the y axis minimum and your maximum as the maximum. Take a look at the example to see how this works.

Also think about how you would handle data below 0 on your graph.

https://github.com/trumpetgrace/Web_Scraper/blob/master/scriptrequest.py
