Virtual drumkit
===============

**THIS EXERCISE RELIES ON ASSETS FROM [JAVASCRIPT30](https://javascript30.com/)**

**Technology:** HTML/CSS, Javascript

**Difficulty**: Easy

**Duration**: 3-4 hours

**Relevant concepts**: Functions, DOM, event listeners, browser dev tools, web audio

**Prerequisites**: Codecademy JS course sections 1-4

Goal
----
Produce a virtual drumkit in the browser.

The project should:
* Show the possible 'beats' the user can play in a simple browser interface, along with the key used to trigger each.
* Detect the user's keypresses, check exactly which key is being pressed, and play the corresponding sound.
* The user should be able to hit more than one key simultaneously.
* Include all of the following 'beats' and their corresponding trigger keys:
  * Clap (A)
  * Hihat (S)
  * Kick (D)
  * Openhat (F)
  * Boom (G)
  * Ride (H)
  * Snare (J)
  * Tom (K)
  * Tink (L)

Stretch goal
------------

* A visual animation should accompany every sound played, to give the user feedback of what 'beat' they hit.

Possible approach
---------------
This project should be attempted in the browser.

It is sensible to start by creating a simple interface in HTML and CSS, and then adding the sound-playing functionality afterward with JS.

Once the interface has been designed, tackle the following problems in order:

1. Detect the user's keypress events and run a function after each one
2. Detect exactly which key the user is pressing, and run the corresponding function for that key
3. Trigger a different 'beat' sound to play for each keypress using JS
4. Trigger a visual animation for the corresponding key's on-screen representation using JS
