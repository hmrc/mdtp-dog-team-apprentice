Virtual clock
===============

**THIS EXERCISE RELIES ON ASSETS FROM [JAVASCRIPT30](https://javascript30.com/)**

**Technology:** HTML/CSS, Javascript

**Difficulty**: Easy

**Duration**: 3-4 hours

**Relevant concepts**: Functions, DOM, event listeners, CSS animations

**Prerequisites**: Codecademy JS course sections 1-4

Goal
----
Produce a virtual analogue clock in the browser.

The project should:
* Show a clock with a hour, minute and second hand
* All three hands should move *continuously* and *smoothly* (i.e., the hour hand should not just jump from one hour to the next)

Stretch goal
------------

* Allow the user to set their timezone and have the clock adjust accordingly.

Possible approach
---------------
This project should be attempted in the browser.

It is sensible to start by creating the clock in HTML and CSS, and then use some Javascript to adjust the style of each hand based on the current time.

Once the interface has been designed, tackle the following problems in order:

1. Access the current time
2. Work out how to translate the current time into the positions of the three hands
3. Update the positions of the hands every second
