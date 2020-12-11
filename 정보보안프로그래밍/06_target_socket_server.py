import socket
# https://seolin.tistory.com/97

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('', 6789))      # bind((ip, port))  # '' 는 INADDR_ANY 를 의미 (모든 인터페이스와 연결 가능)
server_socket.listen(1)    # listen(동시접속허용수)

client_socket, address = server_socket.accept()     # 연결할 때까지 기달
