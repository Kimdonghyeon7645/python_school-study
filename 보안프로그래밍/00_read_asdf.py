with open("asdf.txt", "w") as f:    f.writelines(map(lambda x: str(x) + "\n", range(1, 11)))
with open("asdf.txt", "r") as f:    print(*f.readlines(), sep="")
