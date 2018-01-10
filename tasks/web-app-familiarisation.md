Web application framework familiarisation
=======

**Technology:** Javascript or Python

**Difficulty**: Intermediate

**Duration**: Half a day

**Relevant concepts**: Web application frameworks, MVC, HTTP

**Prerequisites**: Basic knowledge of a web application framework

Goal
----
Produce a really simple web application, which can be run locally with no errors.

The project should:
* Serve at least three different views to the user, each at its own URL (or route).
* At least one route should render some dynamic data from the server, using a templating language.
* Also serve static assets (eg. images and other files) from a folder specified in the application's configuration.

Stretch goal
-----------
The app should also catch all 'unknown' URLs and redirect them to its own custom '404 not found' page.

Possible approach
---------------
Web application frameworks are a vital prerequisite to most web development projects.

You should attempt this project using a popular framework such as [Express](https://expressjs.com/) or [Django](http://djangoproject.com).

If using Express, you can use any templating language (moustache, handlebars, nunjucks) but [EJS](http://embeddedjs.com) is probably the easiest to get started with.

Every view should contain some content, with links back to the other routes. This could take the form of a navigation menu or inline hyperlinks, but neither a clean layout nor CSS wizardry are the purpose of this exercise, so don't spend too long on them.

Your 'dynamic data' can be stored as a variable in the application's code, and then rendered into a view. A database does **not** need to be incorporated at this time.
