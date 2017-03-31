
# Protocol

The protocol is JSON based. Each command is sent as a JSON object and each response is a JSON object.
Values are always set, stored, and returned as strings.

## SET
Set the value of a key, overwriting any existing value.
If optional ttl argument is provided the key will expire in ttl seconds.

### Request:
```json
{
    "command": "SET",
    "args": {
        "key": "foo",
        "value": "some string value"
    }
}
```

With a TTL of 60 seconds:
```json
{
    "status": "OK",
    "result": "some string value",
    "ttl": 60,
}
```
### Response:
```json
{
    "status": "OK",
}
```

## GET
Get the value of the key. If it does not exist returns null.

### Request:
```json
{
    "command": "GET",
    "args": {
        "key": "foo"
    }
}
```

### Response:
```json
{
    "status": "OK",
    "result": "some string value"
}
```

If key does not exist:
```json
{
    "status": "OK",
    "result": null
}
```

## DELETE
Remove the key and associated value. Succeeds even if key does not exist.

### Request:
```json
{
    "command": "DELETE",
    "args": {
        "key": "foo"
    }
}
````

### Response:
```json
{
    "status": "OK",
}
```

## INCR
Add 1 to the current value, assuming it is an integer. If it is not parsable as an integer return an error.
If the key does not exist set it to "0" before performing the operation.
Returns the new value.

### Request:
```json
{
    "command": "INCR",
    "args": {
        "key": "x"
    }
}
```

### Response:
```json
{
    "status": "OK",
    "result": "2"
}
```

### Error:
```json
{
    "status": "ERROR",
    "message": "Value is not an integer"
}
```

## DECR
Subtract 1 from the current value, assuming it is an integer. If it is not parsable as an integer return an error.
If the key does not exist set it to "0" before performing the operation.
Returns the new value.
### Request:
```json
{
    "command": "DECR",
    "args": {
        "key": "x"
    }
}
```

### Response:
```json
{
    "status": "OK",
    "result": "0"
}
```

### Error:
```json
{
    "status": "ERROR",
    "message": "Value is not an integer"
}
```


## EXPIRE
Set a TTL (time to live) in seconds for the key. The key will no longer exist after the TTL has expired.

### Request:
```json
{
    "command": "EXPIRE",
    "args": {
        "key": "foo",
        "ttl": 60
    }
}
```

### Response:
```json
{
    "status": "OK",
}
```



## TTL
Get the current TTL (time to live) for a key.
Returns the time in seconds or null if the key does not exist or does not have a TTL associated with it.

### Request:
```json
{
    "command": "TTL",
    "args": {
        "key": "foo"
    }
}
```

### Response:
```json
{
    "status": "OK",
    "result": 59
}
```
