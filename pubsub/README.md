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


## Steps:
 1. Run `python3 broker.py`
 1. Run `python3 client.py`
 1. Verify that both work and the broker prints the message from the client.
 1. Modify `Broker.handle_client` to process the message based on the `command` key of the  message.
  1. For now the broker can just write to the client socket with the appropriate message ( defined in the [Protocol](protocol.md)). Later we will implement the actual  functionality for subscribe, unsubscribe, publish.
 1. Restart both broker and client and verify that the client prints the acknowledgement  message after sending the `subscribe` command.
 1. Implement higher level functions for `subscribe`, `unsubscribe` and `publish` in ` client.py`.
  1. `subscribe(channel)`
  1. `unsubscribe(channel)`
  1. `publish(channel, message)`
 1. Modify the client main to use these higher level functions.
 1. Implement a separate publisher script that creates a client object that publishes to one  or more channels in a loop every second. This is useful for testing the client.
 1. Go back to `broker.py` and modify it to keep track of client channel subscriptions.  Remember that socket objects are hashable so they can be used as keys in a `dict` and as  elements of a `set`.
 1. Modify `Broker.handle_client` to correctly handle messages with the `PUBLISH` command.  The broker should iterate through all client sockets that are subscribed to the given  channel and send a `MESSAGE` message to them.
 1. Run the broker, client and publisher and verify that the client receives all the  messages it should, but none for other channels.
 1. Run multiple clients/publishers and see if things still work.

## Bonus Steps:
 1. Implement a 2 way chat script that listens on channels and publishes user input to some channels. Ideally it should use threads so the listening is not interrupted to send commands.
 1. Optimise the socket handling code to be more efficient.
 1. Measure how many simultaneous clients your broker can support. What are the limits? Why?
