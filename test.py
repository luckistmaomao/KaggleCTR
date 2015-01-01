#coding:utf-8

from csv import DictReader
import os

train = 'data/train.csv'

def show_partdata():
    for t,row in enumerate(DictReader(open(train))):
        print row
        if t>100:
            break

def show_types():
    with open(train) as f:
        print f.readline()
        print f.readline()


def test():
    if not os.path.exists('test/'):
        os.mkdir('test')
    with open('test/tmp.txt','a+') as f:
        f.write('1\n')

if __name__ == "__main__":
    test()
