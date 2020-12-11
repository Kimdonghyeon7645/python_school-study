import os
from pandas import read_csv
import socket


def check_file(file_path: str, scan_all: bool):
    scan_index = 0 if scan_all else int(input("검색할 시작 위치(인덱스)를 입력하세요 : "))
    with open(file_path, "r", encoding="utf-8") as file:
        target = file.read()
        for virus in virus_dict.values():
            out_index = target.find(virus, scan_index)
            if out_index is not -1:
                file.close()
                os.remove(file_path)
                print(f"파일명 : {file_path} \n바이러스명 : {virus} \n발견된 인덱스 : {out_index} \n",
                      "감염된 파일을 삭제하였습니다.", sep="")
                break


def read_file_from_socket():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 6789))
    msg = client_socket.recv(1024)    # recv(읽어올 바이트수)
    print(msg)


def virus_killer():
    pass


def read_csv_to_dict(csv_name: str):
    data_frame = read_csv(csv_name + '.csv', encoding='utf-8')
    return dict(zip(data_frame['virus_name'], data_frame['virus_value']))


if __name__ == '__main__':
    virus_dict = read_csv_to_dict("virus_db")
    # virus_killer()
    read_file_from_socket()
