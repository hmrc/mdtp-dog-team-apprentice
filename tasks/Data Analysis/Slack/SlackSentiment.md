Slack Sentiment Analysis
====================

**Technology:** Any

**Difficulty**: Easy

**Duration**: 16-32 hours

**Relevant concepts**: data cleaning, pandas

**Prerequisites** Data Amalgamation

Background
----
Most of the communication between digital teams occurs over slack. Over 350,000 slack messages are sent every month. 

The Platform has a set of channels regularly frequented by digital tenants. There are two core sets of channels.
1. - team channels (e.g. #team-ddcops)
2. - issue channels (e.g. #event-dev-issues)

Tennants raise issues in each channel type. However, we have limited visibility of a number of occurances within these channels.

For example:
1. Do questions get asked that platform teams don't respond on?
2. If a platform team doesn't respond, are there others who step in?
3. Where we do address questions and concerns, how is our customer service manner?

Goals
----
To answer question 1 - identify questions raised in a platform team channel or a platform event channel that are not answered by platform staff

To answer question 2 - identify questions raised in a platform team channel or platform event channel that are answered by someone outside the platform

To answer question 3 - perform a sentiment analysis on platform responses to questions/queries in a channel

Suggested Steps
----

Stage 1: Match staff to teams (and identify platform v non-platform)

* 1. Compile a staff list (e.g. by querying the UMP or by scraping the catalogue)
* 2. In a dataframe, match each staff member to a team
* 3. Where a staff member is attached to multiple teams, narrow this down to one team only

Stage 2: Parse slack data into usable format

* 1. 
* 2. 
* 3. 
* 4. 

Stage 3: Identify questions raised by platform tenants

* 1. 
* 2. 
* 3. 
* 4. 

Stage 4: Identify responses to tenant questions + attribute to platform/non-platform

* 1. 
* 2. 
* 3. 
* 4. 

Stage 5: Sentiment analysis of platform responses to tenant queries

* 1. 
* 2. 
* 3. 
* 4. 
