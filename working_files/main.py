"""
r - read (Oxumaq),
w - write (Yazmaq),
a - append (Əlavə etmək),
r+ - read and write (Oxumaq və yazmaq),
rb - read binary format (Şəkil, video və digər bu tipli faylları oxumaq üçün)
"""


# file = open("working_files/data.txt", "r")

# print(file.read(6))
# print(file.read())
# file.seek(0) # Kursoru göstərilən index-ə qaytarır.
# print(file.readlines())
# file.seek(0)
# print(file.readline())

# file.close()
# print(file.read(6)) # Close olduqdan sonra oxumağa çalışsaq xəta verəcək

# file = open("working_files/usernames.txt", "r") # Fayl olmadığına görə xəta verəcək!!!

# file = open("working_files/ips.txt", "w")
# # file.read() # w rejimdə olan faylı oxumaq olmaz. Əks halda xəta verəcək.
# file.write('192.168.1.1\n')
# file.write('127.0.0.1\n')

# all_ips = ['209.99.134.59:5755\n', '104.239.108.217:6452\n', '104.239.108.213:6448\n', '209.99.134.52:5748\n', '104.239.108.116:6351\n', '209.99.134.173:5869\n']
# file.writelines(all_ips)
# file.close()


# file = open("working_files/ips.txt", "a")
# file.write('209.99.134.59:6379\n')
# file.write('209.99.134.59:5432')
# file.close()


file = open("working_files/ips.txt", 'r+')
all_ips = file.readlines()
print(all_ips)
all_ips.append('209.99.134.59:80')
file.writelines(all_ips)
