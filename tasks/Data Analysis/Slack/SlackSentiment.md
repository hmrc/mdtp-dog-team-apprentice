Slack Sentiment Analysis
====================

**Technology:** Any

**Difficulty**: Hard

**Duration**: 1-2 weeks

**Relevant concepts**: data cleaning, pandas, regex, algorithms

**Prerequisites** Data Amalgamation

Background
----
Most of the communication between digital teams occurs over slack. Over 350,000 slack messages are sent every month. 

The Platform has a set of channels regularly frequented by digital tenants. There are two core sets of channels.
- team channels (e.g. #team-ddcops)
- issue channels (e.g. #event-dev-issues)

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

* 1. Export 3 months of data from a slack channel (the easiest way is just to copy the channel history manually, you can also figure out formal exporting)
* 2. Within a dataframe, create separate columns for name, team, time, and message
* 3. You may need to use regex to identify which messages belong to which user

Stage 3: Identify questions raised by platform tenants

* 1. Define a list of possible words attached to a problem a tenant may have (e.g. 'help','broken', 'won't work'...)
* 2. Iterate over messages (using regex) reported by users attached to non-platform teams using your query indicator list
* 3. You will need to compare your output to the dataset to see how well your algorithm is performing

Stage 4: Identify responses to tenant questions + attribute to platform/non-platform

* 1. Within a specific time and for a specific question by defining a list of possible response words (e.g. @reporter, 'have you tried', 'have you raised a ticket?')
* 2. Iterate over tenant questions (using regex) to identify messages that respond to that question. 
* 3. For the set of responses to a single question, identify _who_ participated in the exchange *and* the team each participant is on (platform/non-platform)
* 4. Create a stacked bar chart showing a typical response to a tenant question (how many messages, how many from questioner, from platform staff, from non-platform helpers)

Stage 5: Sentiment analysis of platform responses to tenant queries (sentiment of responses)

* 1. You've now got a set of responses to questions. Define two lists - one with positive words, one with negative words
* 2. Isolate only those responses from platform staff.
* 3. Compute the probability that the responses from platform staff are positive
* 4. Display the average satisfaction/sentiment of a platform responses to a query in the channel
* 5. Display the average satisfaction/sentiment by week over the sample.

Stage 6: Satisfaction with platform responses

* 1. Still using the set of responses to questions created in stages 3/4, define two lists for user satisfaction - one with positive words (thanks, really helpful, I'll try that) , one with negative words (I'll keep looking, I'm still confused)
* 2. Narrow down the set of responses to the final message from the initial questioner (post response)
* 3. Compute the probability that a final response from the initial questioner is positive
* 4. Display the average satisfaction/sentiment of a final response to a query in the channel
* 5. Display the average satisfaction/sentiment by week over the sample.

Resources
----
A quick intro to basic sentiment analysis is here: https://marcobonzanini.com/2015/05/17/mining-twitter-data-with-python-part-6-sentiment-analysis-basics/
