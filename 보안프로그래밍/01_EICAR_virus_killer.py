from os import remove
target_path = "eicar_virus.txt"

if __name__ == '__main__':
    eicar_file, target_file = open("EICAR.txt", "r"), open(target_path, "r")
    if eicar_file.read() in target_file.read():
        target_file.close()
        remove(target_path)
        print(" * EICAR 바이러스가 발견되었습니다. 허락하지 않았어도 이미 삭제하였습니다 ^^7")
    else:
        target_file.close()
    eicar_file.close()
