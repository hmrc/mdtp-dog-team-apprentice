Virtual drumkit
===============

**Technology:** HTML/CSS, Javascript

**Difficulty**: Easy

**Duration**: 3-4 hours

**Relevant concepts**: Functions, DOM, event listeners, browser dev tools, web audio

Goal
----
Produce a virtual drumkit in the browser.

The project should:
* Show the possible 'beats' the user can play in a simple browser interface, along with the keys used to trigger each
* Detect the user's keypresses, check which key is being pressed, and play the corresponding sound.
* The user should be able to hit more than one key simultaneously.

Stretch goal
------------

* A visual animation should accompany every sound played, to give the user feedback of what 'beat' they hit.


Possible approach
---------------
This project should be attempted in the browser.

It is sensible to start by creating the interface in HTML and CSS, and then adding the sound-playing functionality afterward with JS.

Once the interface has been designed, tackle the following problems in order:

1. Detect the user's keypress events and run a function after each one
2. Detect which key the user is pressing, and run a corresponding function based on the key pressed
3. Trigger a 'beat' sound to play using JS
4. Trigger a visual animation for the corresponding key's on-screen representation using JS
