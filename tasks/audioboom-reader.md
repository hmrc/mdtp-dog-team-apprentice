Audioboom API Reader
===================

Hangman
=======

**Technology:** Any

**Difficulty**: Intermediate

**Duration**: 1 day

**Relevant concepts**: HTTP, data structures & JSON, APIs, scheduled tasks

**Prerequisites**: Codecademy Python course sections 1-9 **OR** Codecademy Javascript course sections 1-8, background API knowledge

Goal
----
Produce a program which displays the most recent episodes of a podcast on the Audioboom podcast network.

The program should:
* Use the Audioboom API to retrieve information about the most recent ten episodes of a given podcast.
* Parse through the retrieved data and display only the *title*, *publication date* and *hyperlink* to the user.

Stretch goals
-------------
* Store the most recent podcast locally on disk, overwriting it with a new file whenever a new episode is released.
* Schedule the script to run daily at a given time, without any user input
* Email the user when a new episode is released

Possible approach
---------------

This exercise is best accomplished with python and the terminal.

A library to handle network requests is required, and some way to convert the JSON returned by the Audioboom API into a python dictionary is necessary.

A browser extension like **JSONView** will make parsing through the retrieved data easier.

The Audioboom API documentation is [here](https://github.com/audioBoom/api).

The unix utility cron can be used to schedule tasks.
