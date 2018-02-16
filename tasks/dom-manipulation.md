DOM manipulation
=======

**Technology:** Javascript

**Difficulty**: Intermediate

**Duration**: 1 day

**Relevant concepts**: DOM manipulation, HTTP requests and responses, JSON, event listeners, UX

**Prerequisites**: Codecademy JS course, drumkit exercise

Goal
----
Produce a functioning podcast client app using only javascript techniques. Do not use any frameworks. The end result should be HTML, CSS and JS files only.

Stretch goal
------------
* The list of podcasts should be made filterable or sortable, via a dropdown form field or similar interface component
* The podcast client app should give each content panel its own URL and update that URL as the user navigates between them. If the user copies the URL into a new browser tab, the right panel should be shown.
* Include interface components which which post data to the server, but avoid using the native HTML form functionality.

Possible approach
---------------

A Codepen template is provided for you with all HTML and CSS complete. Your task is to write only the javascript components.

Address each of the following concerns in order:

1. Change the active tab based on the footer link that the user presses.
2. Fetching data from the server and displaying a list of podcasts on initial page load.
3. On button click, the data should be refreshed from the server.
4. On clicking a podcast item, the player panel should be populated with the content of that podcast.
5. On clicking a podcast item, the view should swap automatically to the player panel.

Use this Codepen template and this [finished example](https://codepen.io/jhackett1/pen/eVeQPG) to complete this task.

Use the Audioboom API to supply your data. Documentation [is here](https://github.com/audioBoom/api).

You can get a list of podcasts for a user [here](http://api.audioboom.com/users/185399/audio_clips.json).
