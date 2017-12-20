Predictive Text
=======

**THIS EXERCISE RELIES ON ASSETS FROM DAY 6 OF [JAVASCRIPT30](https://javascript30.com/)**

**Technology:** Javascript

**Difficulty**: Hard

**Duration**: Half a day

**Relevant concepts**: Event listeners, data structures, DOM

**Prerequisites**: Codecademy JS course, drumkit exercise

Goal
----
Produce a text input field which offers autocomplete suggestions as the user types.

The project should:
* Offer a simple, styled text input field.
* Search for possible matches from a dictionary, stored as a JSON file.
* Present a list of suggested words and phrases under the input field, which updates on every keystroke

Stretch goal
------------
* Highlight the parts of each suggestion which have been typed so far, an update on every keystroke

Possible approach
---------------

Autocomplete suggestions are a common feature of modern user interfaces. This project is a particularly fleshed-out implementation.

Start by working out how to bring in the external dictionary JSON file into your application file as a JS object.

Then, work out how to get the user's text input stored as a JS variable.

Finally, create a function to generate and display autocomplete suggestions, and have it run every time the user changes the text input.
