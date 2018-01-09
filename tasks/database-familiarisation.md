Database familiarisation
=======

**Technology:** Node.js, MongoDB

**Difficulty**: Hard

**Duration**: Day

**Relevant concepts**: Database structures, web application frameworks, templating

**Prerequisites**: A basic web application from a previous exercise, basic knowledge of a database

Goal
----
Integrate an existing web application with a database, so it can render dynamic data and show it to the user.

At the conclusion of this project, the application should:
* Connect to the database at startup using a **database driver** module.
* Read data from the database and render it into views using a **templating language**.
* Serve one 'list' view with a list of all entries in the database.
* Serve a 'detail' view which shows data from one entry in detail.

Stretch goal
-----------
The app should provide a form for the user to add additional entries to the database via a HTTP POST request.

Possible approach
---------------
You should complete this project using an Express app from a previous exercise. Use [MongoDB](http://mongodb.org) as your database and [Mongoose](http://mongoosejs.com/) as your database driver module. You can use any templating language, but [EJS](http://www.embeddedjs.com/) is probably simplest for beginners.

You should install a database admin tool like [Robo 3T](https://robomongo.org/) to your computer to quickly see and control your database contents.

You will need to create at least one **model** before completing the goals. This is a file which defines the data structure of each database entry.

Once you have a model and templating language set up, work on the list view.

Then, work on the detail view, passing in a **query parameter** via the URL, which Mongoose can use to find and return a single, specific database entry.

If you are using Django, you already have an SQL database set up from installation, so this exercise doesn't apply.
