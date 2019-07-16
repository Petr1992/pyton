
# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.


import os

def create_dir (name):
    try:
        os.makedirs(name)
    except OSError:
		if not os.path.isdir(name):
        print('{} - папка существует')

name = ['dir_1','dir_2','dir_3','dir_4','dir_5','dir_6','dir_7','dir_8','dir_9']
for i in range(len(name)):
	create_dir(name[i])
	
	
	
import os

def remove_dir (name):
    try:
        os.removedirs(name)
    except FileNotFoundError:
        print('{} - папки не существует')
		
		
name_del = ['dir_1','dir_2','dir_3','dir_4','dir_5','dir_6','dir_7','dir_8','dir_9']
for i in range(len(name_del)):
	remove_dir(name_del[i])	


	



# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

import os.path
listofdir = [f for f in os.listdir() if os.path.isdir(f)]
print(listofdir)


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.


import os
 
pathdir = os.path.abspath()
if not os.path.exists(pathdir):
    os.makedirs(pathdir) 
dirname,filename = os.path.split(__file__)
infile = open(__file__).read()
open(os.path.join(pathdir,filename),'w').write(infile)

