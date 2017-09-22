#!/usr/bin/env python3

import json
import socket
import select


class Subscription(object):

    def __init__(self, client, channel):
        self.client = client
        self.channel = channel


class Broker(object):
    def __init__(self, host='localhost', port=4243):
        self.host = host
        self.port = port
        self.socket = None
        self.client_sockets = []
        self.subscriptions = []

    def run(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.setblocking(0)
        # bind the socket to a public host, and a well-known port
        self.socket.bind((self.host, self.port))
        # become a server socket
        self.socket.listen(5)

        while True:
            ready_to_read, ready_to_write, in_error = \
                select.select(
                    [self.socket] + self.client_sockets,
                    [],
                    [],
                    60)

            for s in ready_to_read:
                if s == self.socket:
                    # accept connections from outside
                    (clientsocket, address) = self.socket.accept()
                    print('Client connected: %s' % (address,))
                    clientsocket.setblocking(0)
                    # now do something with the clientsocket
                    self.client_sockets.append(clientsocket)
                else:
                    self.handle_client(s)

            # # Remove disconnected clients
            # if len(in_error) > 0:
            #     print('Sockets in error: %s' % in_error)
            # self.subscriptions = list(filter(lambda s: s.client not in in_error, self.subscriptions))


    def handle_client(self, client):
        message = self._receive(client)
        if message:
            cmd = message['command'].lower()
            arguments = message.get('args', {})
            fn = getattr(self, 'resolve_' + cmd, None)
            if not fn:
                self._send(client, {'type': 'ERROR', 'error': 'Unrecognized command %s' % cmd})
            else:
                fn(client, **arguments)

    def resolve_subscribe(self, client, channel=None):
        self.subscribe(client, channel)
        self._send(client, {
            "type": "SUBSCRIBE",
            "channel": channel,
            "count": len(self.subscribed_to(channel))
        })

    def resolve_unsubscribe(self, client, channel=None):
        self.unsubscribe(client, channel)
        self._send(client, {
            "type": "UNSUBSCRIBE",
            "channel": channel,
            "count": len(self.subscribed_to(channel))
        })

    def resolve_publish(self, client, channel, message):
        channel_subs = filter(lambda s: s.channel == channel, self.subscriptions)
        for subscription in channel_subs:
            self._send(subscription.client, {
                "type": "MESSAGE",
                "channel": channel,
                "message": message
            })
        print('Client %s published %s to %s' % (client, message, channel))

    def subscribe(self, client, channel):
        if not self.is_subscribed(client, channel):
            print('Client %s subscribed to %s' % (client, channel))
            self.subscriptions.append(Subscription(client, channel))
        else:
            print('Client %s already subscribed to %s' % (client, channel))

    def unsubscribe(self, client, channel=None):
        if not channel:
            self.subscriptions = list(filter(lambda s:
                s.client != client,
                self.subscriptions))
        else:
            self.subscriptions = list(filter(lambda s:
                s.client != client or s.channel != channel,
                self.subscriptions))

    def is_subscribed(self, client, channel):
        existing_subs = list(filter(lambda s:
            s.client == client and s.channel == channel, self.subscriptions))
        return len(existing_subs) > 0

    def subscribed_to(self, channel):
        return list(filter(lambda s: s.channel == channel, self.subscriptions))

    def _receive(self, client):
        buff = ''
        while True:
            try:
                buff += client.recv(1).decode('utf8')
                if not buff:
                    # connection has been closed
                    return None
                # messages are delimited by \n
                if buff[-1] == '\n':
                    break
            except Exception:
                self.unsubscribe(client)
                return None
        buff = buff[:-1]
        message = json.loads(buff)
        return message

    def _send(self, client, message):
        d = json.dumps(message)
        try:
            client.sendall(bytes(d + '\n', 'utf8'))
        except Exception:
            self.unsubscribe(client)


if __name__ == '__main__':
    broker = Broker()
    broker.run()
