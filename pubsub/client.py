import json
import socket
import time


class Client(object):
    def __init__(self, host='localhost', port=4243):
        self.host = host
        self.port = port
        self.socket = None
        self.buff = ''

    def connect(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.host, self.port))

    def _send(self, message):
        d = json.dumps(message)
        self.socket.sendall(bytes(d + '\n', 'utf-8'))

    def _receive(self):
        while True:
            if '\n' in self.buff:
                message = json.loads(self.buff.split('\n')[0])
                self.buff = self.buff.split('\n', 1)[-1]
                return message
            self.buff += self.socket.recv(2048).decode('utf8')
            if not self.buff:
                return None

    def subscribe(self, channel):
        return self._send({
            "command": "SUBSCRIBE",
            "args": {
                "channel": channel
            }
        })

    def unsubscribe(self, channel):
        return self._send({
            "command": "UNSUBSCRIBE",
            "args": {
                "channel": channel
            }
        })

    def publish(self, channel, message):
        return self._send({
            "command": "PUBLISH",
            "args": {
                "channel": channel,
                "message": message
            }
        })

    def disconnect(self):
        self.socket.close()


if __name__ == '__main__':
    client = Client()
    client.connect()
    client.subscribe("foo")
    client.publish("foo", "bar")
    while True:
        r = client._receive()
        if r:
            print(r)
        time.sleep(0.1)
