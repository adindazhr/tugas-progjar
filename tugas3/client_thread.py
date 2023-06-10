import sys
import socket
import logging
import threading

class kirim_request(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # logging.warning("Opening Socket")

        server_address = ('172.16.16.101', 45000)
        # logging.warning(f"Opening Socket {server_address}")
        sock.connect(server_address)

        try:
            # Send data
            request_time = 'TIME \r\n'
            # logging.warning(f"[CLIENT] REQUEST {request_time}")
            sock.sendall(request_time.encode('utf-8'))
            while True:
                data = sock.recv(64).decode('utf-8')
                logging.warning(f"[SERVER TIME] {data}")
        finally:
            logging.warning("closing")
            sock.close()
        return


if __name__=='__main__':
    threads = 0
    y = 1000000
    for i in range(y):
        try:
            thread = kirim_request()
            thread.daemon = True
            thread.start()
            threads += 1
            print(f"Thread amount: {threads}")
        except RuntimeError:    #too many throws a RuntimeError
            break
    print("{} threads created.\n".format(threads))