import socket
# https://seolin.tistory.com/97

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('', 6789))      # bind((ip, port))  # '' 는 INADDR_ANY 를 의미 (모든 인터페이스와 연결 가능)
server_socket.listen(1)    # listen(동시접속허용수)

connection_socket, address = server_socket.accept()     # 연결할 때까지 기달
connection_socket.send("연결 잘했어용 *^^*".encode('utf-8'))
if connection_socket.recv(1024).decode('utf-8') == "바이러스 파일 내놔":
    f = open("i_am_virus.txt", "r", encoding='utf-8')
    content = f.read()
    connection_socket.send(content.encode('utf-8'))
    f.close()
else:
    print("바이러스 파일을 요구하지 않네요...")
