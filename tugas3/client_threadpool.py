import sys
import socket
import logging
from time import perf_counter
from concurrent.futures import ThreadPoolExecutor

def kirim_request():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    logging.warning("Opening Socket")

    server_address = ('172.16.16.101', 45000)
    logging.warning(f"Opening Socket {server_address}")
    sock.connect(server_address)

    try:
        # Send data
        request_time = 'TIME \r\n'
        logging.warning(f"[CLIENT] REQUEST {request_time}")
        sock.sendall(request_time.encode('utf-8'))
        while True:
            data = sock.recv(64).decode('utf-8')
            logging.warning(f"[SERVER TIME] {data}")
    finally:
        logging.warning("closing")
        sock.close()
    return


if __name__=='__main__':
    start = perf_counter()
    threads = 0
    y = 1000000
    with ThreadPoolExecutor() as executor:
        for i in range(y):
            try:
                resp = executor.submit(kirim_request)
                threads += 1
                # print(resp.result())
                print(f"Thread amount: {threads}")
            except RuntimeError:    #too many throws a RuntimeError
                break
        finish = perf_counter()

        print(f"It took {finish-start} second(s) to finish.")
        print("{} threads created.\n".format(threads))