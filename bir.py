import os
import shutil

if os.path.exists(r"D:\Men_Bekorchiman"):
    print('true')
else:
    print('false')
# 1
"""
    for i in range(1, 5):
    f = open(f"D:/Men_bekorchiman/file{i}.txt", "w")
    f.close()
"""
# 2
"""
Men_bekorchiman2 = "D:/Git_link"
shutil.copytree(Men_bekorchiman2, "D:/Men_bekorchiman/Git_link", dirs_exist_ok=True)
"""

# 3
"""
folder = "D:\del folder"
shutil.rmtree(folder)
"""
# papka o'chdi

# 4
"""
adres = "D:/Men_bekorchiman/file1.txt"
os.remove(adres)
"""

# 5
"""
empty = "D:/empty"
if not os.listdir(empty ):
    os.rmdir(empty)
"""

# 6
"""
adres = "D:/Men_bekorchiman"
n = len(adres)
print(n,"ta")
"""
# xamma fayl va papkalar soni chiqdi