JSON -> HTML templating
======================

**Technology:** HTML/CSS, Javascript

**Difficulty**: Intermediate

**Duration**: < 1 day

**Relevant concepts**: Data structures, templating, DOM

**Prerequisites**: Codecademy JS course sections 1-8, potentially also node.js knowledge

Goal
----
Dynamically populate a HTML template using data gained from [a JSON file](https://github.com/hmrc/mdtp-dog-team-apprentice/blob/master/tasks/data.json) (attached).

The project should:
* Check that the data is valid JSON before parsing it.
* Contain a fully styled HTML/CSS template for an online news article.
* As the user loads the page, read the JSON file and display all info contained within it in the correct parts of the template.

Stretch goal
------------
* Work out how to template the file in advance of it being loaded in a browser, and save it as a finished HTML file. Why would you want to do this?

Possible approach
---------------
This approach can be accomplished in several ways. You may choose to create a *pure JS* solution, which relies on a HTML page, plus a script whch reads the JSON file and inserts the correct parts of the JSON into the HTML.

You may instead choose to use a *templating language* like moustache or handlebars to achieve the same effect.

The template must be fully styled, using CSS to achieve a "finished" design.

The template must also work with any data file passed to it.

You can use a tool like [JSONLint](https://jsonlint.com/) to validate the data file before using it, but it would be advantageous to do this programmatically, as a step in your script, to ensure that any supplied data file will always be validated before use.

