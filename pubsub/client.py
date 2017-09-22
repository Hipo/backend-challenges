#!/usr/bin/env python3

import json
import socket
import time
import random
import threading


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
            self.buff += self.socket.recv(1).decode('utf8')
            if not self.buff:
                return None

    def disconnect(self):
        self.socket.close()


def run_client():
    client = Client()
    client.connect()
    channel = str(random.randint(0, 3))
    client._send({'command': 'SUBSCRIBE', 'args': {'channel': channel}})
    while True:
        msg = str(random.randint(1000, 9999))
        time.sleep(random.randint(0, 3))
        client._send({'command': 'PUBLISH', 'args': {'channel': channel, 'message': msg}})
        response = client._receive()
        if response:
            print(response)
        time.sleep(random.randint(0, 3))



if __name__ == '__main__':
    threads = []
    for i in range(10):
        t = threading.Thread(target=run_client)
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
