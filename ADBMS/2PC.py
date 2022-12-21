# SERVER

import socket
import socket
import sqlite3


def server_program():

    host = socket.gethostname()
    port = 9400
    server_socket = socket.socket()
    server_socket.bind((host, port))
    conn, address = server_socket.accept()
    message = "1. Request to prepare for commit\n2. Enter query\n"
    while True:
        data = conn.recv(1024).decode()
        if data == "1":
            dataconn = sqlite3.connect('test.db')
            message = "Prepared to commit. Press 2 for query."
            conn.send(message.encode())
        elif data == "2":
            message = "enter query"
            conn.send(message.encode())
            query = conn.recv(1024).decode()
            try:
                cur = dataconn.cursor()
                cur.execute(query)
                rows = cur.fetchall()
                for row in rows:
                    for c in row:
                        conn.send(str(c).encode())
                        conn.send(" ".encode())
                        conn.send("\n".encode())
                        message = "done"
                        dataconn.commit()
            except Exception as e:

                print(e)
                message = "something wrong in the query"
                conn.send(message.encode())
                conn.close()


if __name__ == '_main_':
    server_program()


# CLIENT
def client_program():
    host = socket.gethostname()
    port = 9400
    client_socket = socket.socket()
    client_socket.connect((host, port))
    message = ""
    data = client_socket.recv(1024).decode()
    print(data)
    while message.lower().strip() != 'bye':
        message = input()
        client_socket.send(message.encode())
        data = client_socket.recv(1024).decode()
        print(data)
    client_socket.close()


if __name__ == '_main_ ':
    client_program()
