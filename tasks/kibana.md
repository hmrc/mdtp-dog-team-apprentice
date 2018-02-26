KIBANA EXERCISE
====================

Technology: Any

Difficulty: Medium

Duration: 16-20 hours

Prerequisites: Kibana Workshop

Goal
----
To build a dashboard in Kibana showing the number/percentage of users of the platform, broken down by devices type - mobile phone, tablet, computer.
These can then be broken down to Linux, MacOS and Windows, or iOS and Android etc.

Stretch goals
------------
Document each step, preferably in a Google Slide deck or other for explanation purposes. 
Backup the dashboard json to the Git repository, so that the dashboard is never lost.

Possible approach
---------------
Start with a query and save this so it produces data that correlates to the task. You can use this to create a visualisation for a dashboard. 
the visualisation needs to be grouped into sections (iPhone, Samsung, Android, Microsoft, Mac OS X etc.) 

You are looking for devices that are using the 'www.tax.service.gov.uk', and they should come up with the results that are allocated to the nginx-access_json logs.

Gotchas
-------
You cannot group them in the first initial query but you can in the visualisation when you go into the buckets with the chosen graph. 

Microsoft sources will have a specific version of their software(5.1, 6.1, 10), you will need to research these versions to know exactly what version the website is being accessed on. 

