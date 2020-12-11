import os
from pandas import read_csv
import socket


def check_file(file_content: str):
    for id, virus in virus_dict.items():
        if virus in file_content:
            print(f"[!] 바이러스가 검출되었습니다!", f"파일 내용 : {file_content}", f"검출된 바이러스 명 : {id}", sep="\n")
            return 1
    print(f"[?] 바이러스가 검출되지 않았습니다!")
    return 0


def read_file_from_socket():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 6789))
    msg = client_socket.recv(1024)    # recv(읽어올 바이트수)
    if msg.decode("utf-8") == "연결 잘했어용 *^^*":
        client_socket.send("바이러스 파일 내놔".encode('utf-8'))
        file_content = client_socket.recv(2048)
        return file_content.decode('utf-8')
    else:
        print("[!] 연결에 실패했습니다 ㅃㅃ...")
        return -1


def virus_killer():
    content = read_file_from_socket()
    print(content)
    check_file(content)


def read_csv_to_dict(csv_name: str):
    data_frame = read_csv(csv_name + '.csv', encoding='utf-8')
    return dict(zip(data_frame['virus_name'], data_frame['virus_value']))


if __name__ == '__main__':
    virus_dict = read_csv_to_dict("virus_db")
    virus_killer()
