import json
import socket


class Server(object):
    def __init__(self, host='localhost', port=4242):
        self.host = host
        self.port = port
        self.socket = None

    def run(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # bind the socket to a public host, and a well-known port
        self.socket.bind((self.host, self.port))
        # become a server socket
        self.socket.listen(5)

        while True:
            # accept connections from outside
            (clientsocket, address) = self.socket.accept()
            print('Client connected: %s' % (address,))
            # now do something with the clientsocket
            self.handle_client(clientsocket)

    def handle_client(self, client):
        message = self._receive(client)
        result = self.handle_message(message)
        d = json.dumps(result)
        client.sendall(bytes(d + '\n', 'utf8'))

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
        print(buff)
        message = json.loads(buff)
        return message

    def handle_message(self, message):
        if message['command'] == 'PING':
            return {'result': 'PONG', 'status': 'OK'}
        return {'message': 'Unknown command', 'status': 'ERROR'}


if __name__ == '__main__':
    server = Server()
    server.run()
