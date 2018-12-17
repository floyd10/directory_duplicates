import hashlib
import os

def get_files(dir):
  list = []
  files = [os.path.join(r,file) for r,d,f in os.walk(dir) for file in f]
  for file in files:
      md5 = hashlib.md5(open(file,'rb').read()).hexdigest()
      if md5 not in list:
          list.append(md5)
      else: print('Найден дубль: ', file)
  return files

dir = 'C:\\Users\\floyd\\Desktop\\Tor Browser'

get_files(dir)
