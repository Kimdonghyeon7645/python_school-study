import os

for i in os.scandir(r"C:\Users\user\Documents\정보보안파이썬\정보보안프로그래밍\virus_search_target_folder"):
    print(i.name, i.is_file(), i.is_dir())
    if i.is_dir():
        print(i.path)
print(os.listdir(r"C:\Users\user\Documents\정보보안파이썬\정보보안프로그래밍\virus_search_target_folder"))
