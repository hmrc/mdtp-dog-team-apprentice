Text adventure game
====================

**Technology:** Any

**Difficulty**: Intermediate

**Duration**: 1-2 days

**Relevant concepts**: Functions, handling user input, data structures, loops, conditional logic

**Prerequisites**: Codecademy Python course sections 1-9

Goal
----
A text adventure game which allows a user to explore through a virtual world, receiving feedback from the program after each action.

The program should:
* Allow a user to move in four directions (up, down, left right)
* Keep track of the user's position in a two-dimensional 'maze'
* Do not allow the user to pass through certain barriers (eg. locked doors, walls)
* Have a win condition, where the user makes their way out of the maze


Stretch goal
------------

* Have a loss condition, where the losing player is invited to restart the game
* Allow the user to open a locked door using a key picked up elsewhere in the maze


Possible approach
---------------
This is a complex exercise which could be tackled in several ways. Major questions to address are:

1. How should the world of the game - the maze - be represented in code?
2. How should the user's position be represented?
3. When and how should the program *disallow* a user's move?
4. Letting the user know when they have 'won' and escaped the maze
