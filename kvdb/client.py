import json
import socket
import time


class Client(object):
    def __init__(self, host='localhost', port=4242):
        self.host = host
        self.port = port
        self.socket = None

    def connect(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.host, self.port))

    def _send(self, message):
        d = json.dumps(message)
        self.socket.sendall(bytes(d + '\n', 'utf-8'))

    def _receive(self):
        buff = ''
        while True:
            buff += self.socket.recv(2048).decode('utf8')
            if not buff:
                return None
            if buff[-1] == '\n':
                break
        message = json.loads(buff)
        return message

    def send(self, message):
        try:
            self._send(message)
        except Exception:
            self.connect()
            self._send(message)
        result = self._receive()
        self.socket.close()
        return result

    def execute(self, command, **kwargs):
        message = {
            'command': command,
            'args': kwargs,
        }
        r = self.send(message)
        if r['status'] == 'OK':
            if r.get('result'):
                return r['result']
            else:
                return None
        else:
            raise Exception(r['message'])

    def disconnect(self):
        self.socket.close()


if __name__ == '__main__':
    client = Client()
    while True:
        r = client.send({'command': 'PING'})
        if r:
            print(r)
        time.sleep(1)
