Let's build a web app
======================
This is a project intended to teach the fundamentals of user-centred design, front and back end web development, database and server administration.

Apprentices will conceptualise, design and build a simple yet working web application from scratch.

In the successor project, the existing application will be migrated over to AWS rather than Heroku.

Skills developed
----------------
* Primary
  * HTML/CSS
  * Javascript
  * Node.js
  * MongoDB
  * REST APIs
  * Bash
  * Source control
  * Code readability & maintainability
* Secondary
  * Information security
  * Test-driven development
  * Continuous integration & deployment

Delivery
--------
The project is intended to take place through weekly practical workshops of about three hours, plus around a day's time working independently on the topics covered in the workshop.

Modules
-------
### 1. User-centred design
This module introduces apprentices to the concept of **user needs** and business needs, plus the value of user research. Apprentices will "imagine" some user needs for the sake of the exercise, map out possible user journeys and eventually create several iterations of wireframes for the application.

The concept of **responsive design** is also briefly introduced.

### 2. How the web works
This module introduces the **server-client relationship**, the structure of URLs and the **HTTP protocol**, including possible response codes (2xx, 3xx, 4xx and 5xx). There is no practical component, but it is necessary background for later workshops.

### 3. HTML/CSS
In this module, apprentices will work to create prototypes of their wireframes from module 1, first using the online IDE [Codepen](http://codepen.io) and eventually with the [Atom](http://atom.io) code editor.

The development concept of **separating concerns** is introduced through the distinction between HTML and CSS. The concept of **readable, maintainable code** is introduced through asking apprentices to use well-structured, semantic HTML and avoiding the use of `!important` in CSS.

Inspecting the markup and styles of existing websites using browser dev tools is introduced.

Apprentices will end up with a HTML & CSS prototype for each screen of their application.

### 4. Source control
This module introduces the need for **source and version control**, especially for developers working in teams. Apprentices install git and learn several basic git commands (`git commit`, `git push`). They also learn the concept of remotes, and connect their local git repository to a Github repository.

At the end of this module, the prototype HTML & CSS files we have so far will live in a Github repo.

### 5. Javascript
In this module, we introduce the first *real* programming language - javascript. Using Codepen, Apprentices learn the programming concepts of types, variables, comparison operators, if and for loops.

At the end of this module, apprentices have added some simple interactivity to their application, using a click event listener to add and remove a class from some markup, and therefore change its appearance.

Outside workshops, apprentices are guided independently through adding all necessary client-side JS to their prototypes.

### 6. Node.js & test-driven development
Here, we introduce the concept of javascript running on the server, along with writing some simple unit tests for the code they write.

Apprentices will install Node, NPM and the testing framework Mocha.

The need to use a web server to proceed, rather than simply loading files into the browser using `file:///` will be discussed.

Apprentices end up with a fresh project directory initialised with NPM, and learn how to serve HTML files via a web server coded in Node. Future modules will add code and functionality to this directory.

Apprentices will be formally introduced to the concept of code **dependencies**, reusable packages/modules of code.

### 7. Frameworks and Express
The server code written in the last module will be substantially **refactored** to use Express, a Node.js web server framework, or Django, the Python equivalent.

At the end of this module, apprentices will have a simple web application with at least three routes, all serving different HTML files.

### 8. Templating and JSON
We will start to include dynamic data in our HTML files. Using a templating language like handlebars or moustache, apprentices will learn to pass dynamic data from the server into their client views.

The structure of JSON data will be outlined, and we will discuss the kind of data each project application is likely to handle and how to structure it in JSON.

### 9. Databases
We will refactor the applications to use a MongoDB database with at least one model, rather than relying on static JSON variables. For those using Node/Express, we will use the popular Mongoose module to interact with the database.

We will discuss the structure of MongoDB databases (keys, documents, collections) and their differences to relational databases.

### 10. Deploy with Heroku
We will deploy the application, which has been only running locally until now, to Heroku. We will consider ways to implement **continuous integration** and **continuous deployment**.

### 11. Getting data from APIs
We will bring external data into our application sourced from a GET request to a third-party API.

We will use the HTTP request module Axios to fetch this data, and then display it to a user via a dynamic template. Depending on each apprentices' concept, we may enrich the information in their own database with info from this third party API.

### 12. Handling user input with forms
Now we have a working web server serving dynamic templates, we will work on sending data back up to the server using POST requests and simple HTML forms. We will revisit the original user needs and ensure we are meeting them.

### 13. Authentication and authorisation
We will consider ways to secure our application to known users, and restrict user permissions to certain operations.

We will begin with a basic understanding how one-way cryptographic functions work, revisit the concept of HTTPS, and consider ways we could authenticate users of our application.

We may implement a very simple cookie-based authentication system.

### 14. Next steps
We will consider the current state of each application and how we could improve it. We will pay particular attention to the end user experience and revisit the original user needs.
