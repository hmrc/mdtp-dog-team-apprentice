Support Tracking
====================


**Technology:** Any

**Difficulty**: Easy

**Duration**: 8 hours then ongoing

**Relevant concepts**: crosstabs, pandas

**Prerequisites** Webscraper + Data Amalgamation

Background
----
There is currently ongoing user research into how MDTP provides support to over 70 platform teams. A great deal of the support happens in slack and via conversation, and is therefore difficult to understand. However, where a support issue is sufficiently large or onerous, it is documented on JIRA. 

Support is a vital part of the ongoing work of MDTP. However, as more and more teams and services join the platform, the total support workload continues to increase. Moreover, because support demands more time and effort, we struggle to prioritise preventative measures that would deal with multiple requests for the same kind of support.

As part of the user research, we are exploring tracking support tickets. By identifying patterns in our support tickets, it may be possible to:
More quickly identify common issues and prioritise generic solutions
Establish geographic or team-based patterns in requests, and dedicate effort towards building capacity.
Identify the frequency of intensive support requests and potentially link this to cost

Tracking is possible by attaching different labels to tickets. By default, tickets are labelled with the team that is responsible for the issue in question. 

Team Apprentice is being asked to take on three responsibilities:
1. Conduct an analysis of existing SUP tickets based on existing labels
2. Append additional labels to SUP tickets on an ongoing basis
3. Extend the analysis based on additional labelling information

Preliminary Analysis
----
Based on existing information in the SUPP JIRA board you should:
* Download the entire SUPP board as a csv file
* Identify how many SUPP tickets have team-based labels (e.g. PlatOps, Build and Deploy)
* Quarantine useful SUPP tickets in a new CSV
* Count how many for each team
* A pie graph showing request by team for all tickets in the sample
* A stacked line graph showing number of requests by team over time (weeks) for all tickets in the sample
* A bar graph showing average number of requests by team for all tickets in the sample
* A bar graph showing tickets created in a week and tickets closed in a week - over time
* A line graph showing tickets opened in week 2 minus (-) tickets closed in week 1 - over time

Labelling Framework
----
A labelling framework has been developed to facilitate analysis. There are two categories of label, each of which would need to be consistently applied to tickets. Platform teams are currently labeled, but the focus of support tickets is not. Tracking where platform problems are coming from is a good place to start. The list below is likely incomplete, but if you start seeing a few tickets with a common theme that is not captured, flag it with the other apprentices and add a new label in.

The labelling framework can be found here - https://confluence.tools.tax.service.gov.uk/display/Support/Platform+Triage+Process

The labelling framework requires documentation of the product/service that is reporting issues, and the inclusion of a macro category (e.g. metrics or the build pipeline)

An additional category of label can be derived from the ticket reporter. This would focus on the Originating Team. Three pieces of information would be useful:
* Team (or teams)
* Location
* Service

Once the labels have been applied to tickets collected for over a week:
* Design a weekly report for support tickets that highlights key issues that week
* Extend this to a monthly report


