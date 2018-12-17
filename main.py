import argparse
import hashlib
import os
import glob
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


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(help='Введите путь',required=True)
    args = parser.parse_args()
    return args

args = create_parser()
dir = (args.p).replace('/','\\\\')
print(dir)
