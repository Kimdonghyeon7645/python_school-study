def hasDongMyeong(name_list):
    called_name_list = []
    dong_myeong_list = []
    for name in name_list:
        if name not in called_name_list:
            called_name_list.append(name)
        else:
            dong_myeong_list.append(name)
    print(dong_myeong_list)


hi_my_name_is_name_list = input("학생 이름을 입력하세요: ").rstrip().split(',')
hasDongMyeong(hi_my_name_is_name_list)
