Backend Team Challenges

The aim of these challenges is to learn more about the software systems we use everyday. One of the best ways to learn how something works is to implement it yourself. We will attempt to implement our own versions of systems like Redis, Memcached, Postgresql, Celery, Flask, etc. By thinking about and implementing our own version of these systems the internals will become transparent to us, allowing us to better understand the real versions. 

We do not of course plan to use anything we implement in these challenges in production. We are not pretending we can reimplement such systems in a single day. Our implementations will be optimised for readability and simplicity over performance. They will support a minimal feature set, dealing with (some of) the most common use cases rather than edge cases.

These challenges are NOT competitions! We will each write our own code but we will solve the problem together. We will discuss the challenge together before we write any code and at intervals during the coding session. When we get stuck we will discuss as a group and help each other out. The aim of these challenges is for everyone to learn something, whether you have never used the the system we are implementing or you wrote the original! 


# General Rules
  * The implementation must be in Python 3 and use only the standard library.
  * The implementation should be optimised for readability first, then efficiency.
  * The implementation must support the agreed protocol and client.
  * Ask each other for help before asking google/stackoverflow (except for simple syntax things that you don't keep in your head because you know they are on the internet!)
  * Please do not copy/paste any code from StackOverflow etc. Research and discuss until you understand and then write your own code!



# Challenge 1 - Build a Key-Value Database Server from scratch

Key-Value stores like Redis or MemCached are simple databases used for storing unstructured data associated with a unique key. They have a client server architecture with multiple clients accessing a single server. Usually the data is kept fully in memory but may be persisted to disk to allow recovery after a restart. They are often used for caching and thus support setting expiration time for keys and purging in LRU (least recently used) order.

We will build a database server supporting the following commands:
  * GET key, value
  * SET key, value
  * DELETE key
  * INCR key
  * DECR key
  * EXPIRE key, seconds

We will agree a protocol and create a client beforehand. The challenge is to create a database server that appropriately responds to the client. The client will be responsible for serialising the data to be stored into a suitable text based format (e.g. json or pickle).

In addition to correctly implementing the above commands the server should:
  * support multiple concurrent clients
  * persist its datastore to disk every N seconds
  * ensure a maximum of N MB of memory is used



# Challenge 2 - Build a Document Oriented Database Server from scratch

A MongoDB/CouchDb/Dynamodb 'clone'.


# Challenge 3 - Build a Relational Database Server from scratch

A Postgresql/Mysql 'clone'.


# Challenge 4 - Build a PubSub Server from scratch

Like Redis PubSub / RabbitMQ PubSub


# Challenge 5 - Build a Task Queue from scratch

Like Celery/Kuyruk/Resque/Fifo


# Challenge 6 - Build a Micro Web Framework from scratch

Like Flask/Pico/Bottle/WebPy


# Challenge N+1 - Make a suggestion!

