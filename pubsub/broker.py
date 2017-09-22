import json
import socket
import select


class Broker(object):
    def __init__(self, host='localhost', port=4243):
        self.host = host
        self.port = port
        self.socket = None
        self.db = {}
        self.client_sockets = []

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
                    self.client_sockets,
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

    def handle_client(self, client):
        message = self._receive(client)
        subscribers_key = "subscribers_of_%s" % message["args"]["channel"]
        self.db.setdefault(subscribers_key, [])
        if message["command"] == "SUBSCRIBE":
            if client not in self.db[subscribers_key]:
                self.db[subscribers_key].append(client)

            broker._send(client, {
                "type": "SUBSCRIBE",
                "channel": message["args"]["channel"],
                "count": len(self.db[subscribers_key])
            })
        elif message["command"] == "UNSUBSCRIBE":
            if client in self.db[subscribers_key]:
                self.db[subscribers_key].remove(client)

            broker._send(client, {
                "type": "UNSUBSCRIBE",
                "channel": message["args"]["channel"],
                "count": len(self.db[subscribers_key])
            })
        elif message["command"] == "PUBLISH":
            for client in self.db[subscribers_key]:
                broker._send(client, {
                    "type": "MESSAGE",
                    "channel": message["args"]["channel"],
                    "message": message["args"]["message"],
                })
        else:
            assert False

    def _receive(self, client):
        buff = ''
        while True:
            buff += client.recv(2048).decode('utf8')
            if not buff:
                # connection has been closed
                return None
            # messages are delimited by \n
            if buff[-1] == '\n':
                break
        buff = buff[:-1]
        message = json.loads(buff)
        return message

    def _send(self, client, message):
        d = json.dumps(message)
        client.sendall(bytes(d + '\n', 'utf8'))


if __name__ == '__main__':
    broker = Broker()
    broker.run()
