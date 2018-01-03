
Vizceral
=========================

This project will see apprentices build a real-time animated diagram of traffic flowing through MDTP, using the open source tool Vizceral.

Vizceral is an open-source tool built by Netflix. It is a good fit to the microservice architecture of the tax platform.


Skills developed
----------------
* Primary
  * JSON & data structures
  * Software architecture
  * Node.js
  * Docker

Delivery
--------
The project should be started via an hourly kick-off workshop, but all technical work should be done in an unsupervised team, with assistance available from mentors if needed.

Modules
-------
### 1. Get Vizceral up and running
Netflix provides a complete example version of their Vizceral tool [here](https://github.com/Netflix/vizceral-example), complete with sample data.
Download, install and run this example in a local web browser.

### 2. Understand the data
Look at the raw NGINX logs provided from MDTP and understand their format and the data available in them.
Then, compare these logs to the sample data in the Vizceral example, and note the differences.

### 3. Process MDTP data into Vizceral format
Take the 1 hour input sample provided from S3 as a local file.
Process each nginx record in the file.
Output the data structure required by Vizceral Demo.

### 4. Up and running with Docker
Use the generated sample data file and build a Docker container to be used to demo the data generated.

### 5. Using real data
Update the vizceral demo so it pulls the data file from an S3 bucket, then demo this.

### 6. Approaching real time
Update the vizceral demo so it polls for updated data file every one minute.

### 7. 
Take a second 1 hour sample file and generate a second datafile then demo using a locally running container that the updated data causes the visualization to change.

### 8. Lambda
Lambda functions are an Amazon product that allows serverless code to run in the cloud in response to events.

Convert the data generation script to run as an AWS lambda function that is driven by an AWS S3 notification event, but still pushes the data to an S3 bucket.

### 9. Lastly...
Work with the telemetry team to tune the frequency that the nginx files get pushed to S3
