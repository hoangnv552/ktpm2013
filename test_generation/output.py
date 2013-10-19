__author__ = 'hoangnongvan'

import unittest
import input
import itertools

array1 =[]
array2 = []

doc = input.main.__doc__

i = 0
j = -1
while(i<len(doc)):
    tmp = ''
    if(doc[i]=='['):
        k = i+1
        while(doc[k]!=';'):
            tmp += doc[k]
            k+=1
        a = int(tmp)
        tmp = ''
        k+=1
        while(doc[k]!=']'):
            tmp += doc[k]
            k+=1
        b = int(tmp)
        array1[j].append(a)
        array1[j].append(b)
        array2[j].append((a+b)/2)
        tmp = ''

    if((i+1)<len(doc) and doc[i+1]==':'):
        j+=1
        array2.append([])
        array1.append([])

    i+=1

for i in range (0, len(array1) ):
        for j in range(0, len(array1[i])-2,2):
            if (array1[i][j+2]-array1[i][j+1])*(array1[i][j+3]-array1[i][j]) < 0:
                raise Exception("wrong input")
            if len(array1[i]) > 4 and ( array1[i][4]-array1[i][1])*(array1[i][5]-array1[i][0]) < 0 :
                raise Exception("wrong input")

class TestGeneration(unittest.TestCase):
    pass

def test_generator(a, b):
    def test(self):
        self.assertEqual(a,b)
    return test

if __name__ == '__main__':
    print "\nMang gia tri : "
    print array1

    print "\nMang cac test case : "
    print array2

    for i in itertools.product(*array2):
        print i
        test_name = 'test_%s' %str(i)
        test = test_generator(input.main(*i) , 1)
        setattr(TestGeneration, test_name, test)
    unittest.main()

