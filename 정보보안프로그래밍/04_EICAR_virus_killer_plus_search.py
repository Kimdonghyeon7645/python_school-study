import os


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




if __name__ == '__main__':
    virus_dict = {
        1: "감기",
        2: "후두염",
        3: "독감"
    }
