import hashlib
import os

def get_dublicates(dir):
  list = []
  list_elements = []
  files = [os.path.join(r,file) for r,d,f in os.walk(dir) for file in f]
  for file in files:
      md5 = hashlib.md5(open(file,'rb').read()).hexdigest()
      if md5 not in list:
          list.append(md5)
      else: list_elements.append(file)
  return list_elements

dir = 'F:\\projects'
x = get_dublicates(dir)
print('Список дублей:',x)