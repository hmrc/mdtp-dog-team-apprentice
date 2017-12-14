Hangman
=======

**Technology:** Any

**Difficulty**: Intermediate

**Duration**: 1 day

**Relevant concepts**: Functions, handling user input, loops, data structures

**Prerequisites**: Codecademy Python course sections 1-9

Goal
----
Produce a game of hangman.

The game should:
* Randomly select a word, and keep it secret for the user to guess.
* Allow the user to keep track of guesses, and progressively reveal more of the word on every correct guess
* Keep track of the users' guesses and end the game if a limit is exceeded
* Notice when the word has been guessed, and congratulate the user on their win

Stretch goal
------------
* Have the game pick a word from a large word list stored in a *seperate file*.
* Allow the user to choose to make a guess at the whole word, rather than typing every character individually

Possible approach
---------------

This exercise is best accomplished with python and the terminal.

The most complicated part of this exercise is processing the user's guesses and saving the outcome so that the word is progressively revealed as the user guesses more characters.
