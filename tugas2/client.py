import sys
import socket
import logging



def kirim_data():
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
    for i in range(1,10):
        kirim_data()
