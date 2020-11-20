def md5_hash(target: str) -> str:
    import hashlib

    md5 = hashlib.md5(target.encode("utf-8"))
    print(md5)
    return md5.hexdigest()


def get_filepath_from_sys() -> str:
    import sys

    if len(sys.argv) < 2:
        print(f"<!> 실행시 입력한 인자값이 올바르지 않습니다! \n 인자값 : {sys.argv}")
    return sys.argv[1]


def check_if_file_is_virus(filepath: str, virus_db: dict):
    import os

    file = open(filepath, "r", encoding="utf-8")
    print(file.read(), md5_hash(file.read()))
    if md5_hash(file.read()) in virus_db.values():
        file.close()
        os.remove(filepath)
        print(f"{filepath} 파일에 바이러스가 발견되어서 삭제하였습니다.")
    else:
        print("파일에 바이러스가 발견되지 않았습니다.")


if __name__ == '__main__':
    db = {
        1: md5_hash("감기"),
        2: md5_hash("후두염"),
        3: md5_hash("독감")
    }
    print(db)
    check_if_file_is_virus(get_filepath_from_sys(), db)
