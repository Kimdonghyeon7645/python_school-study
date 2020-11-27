from os import remove


def virus_killer(filename: str, virus_db: dict):
    target_file = open(filename, "r")
    for virus in virus_db.values():
        if virus in target_file.read():
            target_file.close()
            remove(filename)
            print(f" * {virus} 바이러스가 발견되었습니다. 허락하지 않았어도 이미 삭제하였습니다 ^^7")
            return
    print(f"{len(virus_db)}건의 바이러스와 비교한 결과 일치하는 바이러스가 없습니다. 바이러스 검사를 종료합니다...")
    target_file.close()


if __name__ == '__main__':
    VirusDB = {
        1: "11759930ed472727a2cde1343ad6989:EICAR TEST",
        2: "018075b76877c90098783d3b2436d2d0:Sample TEST"
    }
    virus_killer("asdf.txt", VirusDB)
