import os

files_len = len(os.listdir('C:\\Users\\user\\Downloads\\레주메북 2-4'))
student = []
for f in os.listdir('C:\\Users\\user\\Downloads\\레주메북 2-4'):
    if '24' in f:
        student.append(f.split('24')[-1][:6])
student.sort()
print(f"총 {files_len}개 파일 존재")
print(f"총 {len(student)}명 확인")
print(*student, sep='\n')
