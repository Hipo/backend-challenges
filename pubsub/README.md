# Build a Pub Sub System

Pub Sub is a system architecture where clients can Subscribe to channels/topics where other clients can Publish messages. The subscribers have no knowledge of the publishers nor the publishers of the subscribers. A central broker is responsible for managing subscriptions, receiving messages from publishers and pushing messages to subscribers. Brokers can also be clients themselves, forming a hub topology.

The broker must:
  * accept multiple concurrent client connections
  * hold client-channel subscriptions
  * handle subscription messages
  * handle publish messages
  * receive messages from publishers and send to appropriate subscribers

When a client disconnects from the broker all of its subscriptions are lost. If it reconnects it must subscribe again. The client does not receive any messages that were sent on a channel before it subscribed.

See [Protocol](protocol.md) for details of the command and message format.
