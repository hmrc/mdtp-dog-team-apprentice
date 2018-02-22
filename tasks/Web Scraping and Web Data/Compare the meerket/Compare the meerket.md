Bargain Hunter (Compare the Meerket)
====================

***AVAILABLE FOR INDIVIDUALS***

**Technology:** Any

**Difficulty**: Medium

**Duration**: 8-16 hours

**Relevant concepts**: hmtl parsing/xpaths, schedules, saving data

**Prerequisites** Web Scraper project

Goal
----
Produce a script or program that searches common online marketplaces for a product of your choice and compares prices in real time. Find the cheapest.

The script should:
* Pull price data on a predefined product from multiple online marketplaces
* Have a function to compare prices for the product (don’t forget shipping)
* Display a recommended retailer to the user and a link

Stretch goals
------------

* Implement a schedule to track the price of an item on different online marketplaces over time. Is there a day of the week or time of year when prices change often?
* Instead of hardcoding in a product, try a product class and allow users to pick from a selection of products to compare. Alternatively, allow the user to include or exclude different online marketplaces.

Possible approach
---------------
This program can be implemented fully using the terminal and python. Lxml, requests, numpy and pandas are all useful packages for this project. Despite this, javascript may give you a friendlier interface for your user.

Gotchas
-------
* Don't run the script too many times for the same websites, you may get blocked! Instead, try to only pull data from websites when necessary and after a few times try to space it out before retrying
* If an error occurs when pulling the data, try opening the webpage and check that it works in the browser, then try running the script again
* Sometimes when getting an xpath for a website it'll give you back an empty array, this may need a little messing around to get the data you want to be returned to you (making the xpath more general, for example)
* If your data is returned in an array don't forget to call the correct index of the array to get the data you want
* Data may need cleaning up. The strip() function may be helpful to use for this
* The join() function can also be used for tidying the data
