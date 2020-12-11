import os
from pandas import read_csv


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


def check_folder(folder_path: str, recursive: bool):
    for file in os.scandir(folder_path):
        if file.is_file():
            check_file(os.path.join(folder_path, file.name), scan_all=True)
        elif file.is_dir():
            check_folder(file.path, recursive)


def virus_killer():
    print("바이러스의 숙청이 다가옵니다...")
    mode = int(input("숙청 모드를 선택하세요 (1= 파일 특정 위치, 2= 파일 전체, 3= 폴더 전체) : "))

    if mode in [1, 2]:
        check_file(input("검색할 파일를 경로를 함께 입력하세요 : "),
                   scan_all=(mode is 2))
    else:
        check_folder(input("검색할 폴더를 경로를 함께 입력하세요 : "),
                     recursive=input("폴더 안의 파일을 재귀적으로 검사할까요 (y/n)? ") in ['Y', 'y', 'Yes', 'yes', 'YES'])


def read_csv_to_dict(csv_name: str):
    data_frame = read_csv(csv_name + '.csv', encoding='utf-8')
    return dict(zip(data_frame['virus_name'], data_frame['virus_value']))


if __name__ == '__main__':
    virus_dict = read_csv_to_dict("virus_db")
    # virus_killer()
