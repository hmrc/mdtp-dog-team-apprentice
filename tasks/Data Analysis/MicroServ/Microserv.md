Prototype Count
====================

**Technology:** Any

**Difficulty**: Moderate

**Duration**: 16-32 hours

**Relevant concepts**: github, loops, 

**Prerequisites** Data Amalg


Background
----
MDTP is growing really quickly. We've nearly got 800 microservices with more coming online every day. But we don't have any historical perspective on how fast we are growing, or how large we have gotten (in terms of actual capacity used by our MS). 

It is possible to get a sense of this from the catalogue - we can see when a microservice repo was first created, and come up with a cumulative frequency graph from that. Unfortunately, that omits any repos that have been deleted, so it's impossible to see where microservices have been decomissioned. Moreover, just knowing absolute numbers of microservices isn't that useful on it's own. We don't know how the relative size of microservices have changed over time, and we don't know how microservices change between environments. 

Each environment has a config repo for all the microservices in that environment. Within each app-config repo, individual .yaml files represent microservices. .yaml files contain the parameters that determine the compute resources each microservice will be allocated. These are split into two units - instances, the number of machines the MS will run on, and slots, the number of containers within each machine that will host a copy of the MS. In total, slots x instances will show how many copies of the MS are running simultaneously.

*Development - https://github.com/hmrc/app-config-development
*QA - https://github.com/hmrc/app-config-qa
*External Test - https://github.com/hmrc/app-config-externaltest
*Staging - https://github.com/hmrc/app-config-staging
*Production - https://github.com/hmrc/app-config-production

Goal
----
To track number of microservices in different platform environments (and the relative size of these microservices) since the platform started.

Stage 1:

*1. Download or clone app.config.production
*2. Work out how to iterate over different git commits (gitpython should help)
*3. Make sure you’ve converted the time of each commit to a datetime object
*4. Compare the number of .yaml files (config for each microservice) between today and one week ago.
*5. Iterate over the entire commit history – compare the difference in .yaml files over time.
*6. Produce a cumulative frequency histogram that shows the total .yaml files in app-config-prod, over time.
*7. Produce a second histogram that shows the number of git commits to app-config-prod each week over time.

Stage 2:

*1. Go into a .yaml file and multiply the slots x instances
*2. Trace one .yaml file over its commit history and show how the total number of slots (slots x instances) changes over time.
*3. Extend this analysis across all .yaml files
*4. Produce a plot of the total slots (sum of all .yaml files) over time

Stage 3:

*1. Repeat the analysis above for the Dev environment
*2. Repeat the analysis above for the QA environment
*3. Repeat the analysis above for the Staging environment
*4. Repeat the analysis above for the External Test environment

Stretch goals
------------

* Come up with a way to show the evolution of a microservice through different environments (i.e. a plot (maybe with different colours for environments- think stacked area graph) that shows when and how many slots an indivdual microservice has required since its inception)
