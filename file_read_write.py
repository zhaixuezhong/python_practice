__author__ = 'zxz'

file_abs = "D:\\tmp\\a.txt"
# try:
#     f = open(file_abs,"r")
#     print(f.read())
# finally:
#     if f:
#         f.close()
with open(file_abs,"r") as f:
    print(f.read())

print("python start writting something...")

f = open(file_abs,"a")
f.write("\n你好，我是python")

print("python stop  writting something...")


with open(file_abs,"r") as f:
    print(f.read())