import hashlib
import os
from collections import Counter

def get_files(dir):
  files = [os.path.join(r,file) for r,d,f in os.walk(dir) for file in f]
  return files

def get_md5(dir):
    files = get_files(dir)
    md5_list = []
    for file in files:
      md5 = hashlib.md5(open(file,'rb').read()).hexdigest()
      md5_list.append(md5)
    return md5_list

def find_duplicates(dir):
    md5_sums = get_md5(dir)
    counter = Counter(md5_sums)
    return print('Найдены следующие дубли по md5: ', counter)

print('введите путь для поиска дубликатов файлов по md5: ')
dir = input()
find_duplicates(dir)