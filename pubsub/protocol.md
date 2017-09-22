
# Protocol

The protocol is JSON based. Each message is sent as a JSON object and each response is a JSON object.


## Commands

Commands are sent by clients to the broker. 

### SUBSCRIBE
Subscribe a client to a channel

```json
{
    "command": "SUBSCRIBE",
    "args": {
        "channel": "foo"
    }
}
```


### UNSUBSCRIBE
Unsubscribe a client from a channel

```json
{
    "command": "UNSUBSCRIBE",
    "args": {
        "channel": "foo"
    }
}
```


### PUBLISH
Publish a message on a channel

```json
{
    "command": "PUBLISH",
    "args": {
        "channel": "foo",
        "message": "hello world"
    }
}
```


## Messages

Messages are sent by the broker to the client.

### Subscribe

```json
{
    "type": "SUBSCRIBE",
    "channel": "foo",
    "count": 1
}
```


### Unsubscribe

```json
{
    "type": "UNSUBSCRIBE",
    "channel": "foo",
    "count": 0
}
```

### Message

```json
{
    "type": "MESSAGE",
    "channel": "foo",
    "message": "hello world"
}
```
