# Build a Key-Value Database Server from scratch

Key-Value stores like Redis or MemCached are simple databases used for storing unstructured data associated with a unique key.
They have a client server architecture with multiple clients accessing a single server.
Usually the data is kept fully in memory but may be persisted to disk to allow recovery after a restart.
They are often used for caching and thus support setting expiration time for keys and purging in LRU (least recently used) order.

We will build a database server supporting the following commands:
  * GET key, value
  * SET key, value
  * DELETE key
  * INCR key
  * DECR key
  * EXPIRE key, seconds
  * TTL key
  * PING

We will agree a protocol and create a client beforehand.
The challenge is to create a database server that appropriately responds to the client.
The client will be responsible for serialising the data to be stored into a suitable text based format (e.g. json or pickle).

In addition to correctly implementing the above commands the server should:
  * support multiple concurrent clients
  * persist its datastore to disk every N seconds
  * ensure a maximum of N MB of memory is used
