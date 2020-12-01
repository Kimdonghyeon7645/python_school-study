import socket

s = socket.socket()
for port in range(10000, 10100):
    try:
        print(f"{port}번 포트 연결중...", end="\t")
        s.connect(('127.0.0.1', port))
    except ConnectionRefusedError as e:
        print(f"실패")
    else:
        print("성공!")
        s.close()
        s = socket.socket()
s.close()
