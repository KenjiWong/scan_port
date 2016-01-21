from threading import Thread, activeCount
import socket
import os
import pdb
from time import sleep
import time


def test_port(dst,port):
    conn = socket.socket()
    try:
         conn.connect((dst, port))
    except IOError:
        conn.close()
        exit()
    print port

if __name__ == '__main__':
    print time.time()
    dst = '210.209.70.90'
    # threads = []
    # for i in range(1, 8889):
    #     threads.append(Thread(target=test_port, args=(dst, i)))

    i = 1
    while i < 10000:
        if activeCount() < 850:
            Thread(target=test_port, args=(dst, i)).start()
            i+=1
    while True:
        if activeCount() == 1:
            print 'over'
            break
    print time.time()
