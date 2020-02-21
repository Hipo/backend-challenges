# Postgresql based Task Queue

For this challenge we will design and implement a task queue that uses Postgresql to store queued up tasks. 
Workers will query the database to fetch tasks to work on and write results/status back to the database. 
We will use Django for this challenge as it is familiar to all participants and will provide a useful level of abstraction 
while not limiting access to the required Postgresql features.


## Discussion Points

* What is a Task Queue?
* What do we use Task Queues for?
* What features do we expect from a Task Queue?
* What data structures/data models are required?


## Implementation

* Create a Task model
* Write a tasks module with some sample task functions
  - A function that prints something
  - A function that saves some object to the database
  - A function that sleeps for some seconds
  - A function that raises an exception with some probability
* Write a Worker program that executes the appropriate function for each Task object created (tip: use a management command)
* Track task execution status
* Run multiple workers concurrently
* Locking
* Retries
* Task TTL (task expiry)
* Timeouts
* Task scheduler



## Post Implementation Discussion

* How well will this system scale?
* What guarantees does this system provide?
* What are the advantages of using Postgresql for a task Queue?
* What are the disadvantages of using Postgresql for a task Queue?
* When would it be useful & appropriate to use this type of system?
* When would it not be appropriate to use this type of system?

## Setup guide

You can run `source tools/run_development.sh`
