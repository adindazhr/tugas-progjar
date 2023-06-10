import sys
import socket
import logging
from multiprocessing import Process

def kirim_request():
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
    # thread = 0
    # for i in range(0, 1000):
    #     thread += 1
    #     process = Process(target=kirim_request)
    #     process.start()
    #     print(f"Process amount: {thread}")
    threads = 0     #thread counter
    y = 1000000     #a MILLION of 'em!
    for i in range(y):
        try:
            process = Process(target=kirim_request)
            threads += 1    #thread counter
            process.start()       #start each thread
            print(f"Thread amount: {threads}")
        except (RuntimeError, OSError):    #too many throws a RuntimeError
            break
    print("{} threads created.\n".format(threads))