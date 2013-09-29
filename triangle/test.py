__author__ = 'hoangnongvan'

import unittest
import math
import triangle


class MyTestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(triangle.detect_triangle(2 ** 32, 6, 6), 'du lieu khong hop le')

    def test2(self):
        self.assertEqual(triangle.detect_triangle(6, 2 ** 32, 6), 'du lieu khong hop le')

    def test3(self):
        self.assertEqual(triangle.detect_triangle(6, 6, 2 ** 32), 'du lieu khong hop le')

    def test4(self):
        self.assertEqual(triangle.detect_triangle('x', 6, 6), 'du lieu khong hop le')

    def test5(self):
        self.assertEqual(triangle.detect_triangle(6, 'x', 6), 'du lieu khong hop le')

    def test6(self):
        self.assertEqual(triangle.detect_triangle(6, 6, 'x'), 'du lieu khong hop le')

    def test7(self):
        self.assertEqual(triangle.detect_triangle(0, 8, 6), 'Khong phai la 3 canh cua tam giac')

    def test8(self):
        self.assertEqual(triangle.detect_triangle(8, 0, 6), 'Khong phai la 3 canh cua tam giac')

    def test9(self):
        self.assertEqual(triangle.detect_triangle(8, 6, 0), 'Khong phai la 3 canh cua tam giac')

    def test10(self):
        self.assertEqual(triangle.detect_triangle(6.8, 6.8, 6.8), 'Tam giac deu')

    def test11(self):
        self.assertEqual(triangle.detect_triangle(6, 6, 6), 'Tam giac deu')

    def test12(self):
        self.assertEqual(triangle.detect_triangle(6, 6, 5), 'Tam giac can')

    def test13(self):
        self.assertEqual(triangle.detect_triangle(6.8, 6.8, 5.8), 'Tam giac can')

    def test14(self):
        self.assertEqual(triangle.detect_triangle(2 ** 32 - 2, 2 ** 32 - 2, 6), 'Tam giac can')

    def test15(self):
        self.assertEqual(triangle.detect_triangle(2 ** 32 - 2, 6, 2 ** 32 - 2), 'Tam giac can')


    def test16(self):
        self.assertEqual(triangle.detect_triangle(6,2 ** 32 - 2 , 2 ** 32 - 2), 'Tam giac can')

    def test17(self):
        self.assertEqual(triangle.detect_triangle(2**32-2 ,2 ** 32 - 2 , 2 ** 32 - 2), 'Tam giac deu')

    def test18(self):
        self.assertEqual(triangle.detect_triangle(6, 6, math.sqrt(72)), 'Tam giac vuong can')

    def test19(self):
        self.assertEqual(triangle.detect_triangle(6, math.sqrt(72), 6), 'Tam giac vuong can')

    def test20(self):
        self.assertEqual(triangle.detect_triangle(math.sqrt(72),6 , 6), 'Tam giac vuong can')

    def test21(self):
        self.assertEqual(triangle.detect_triangle(8,6 ,(math.sqrt(100))), 'Tam giac vuong can')

    def test22(self):
        self.assertEqual(triangle.detect_triangle(8,(math.sqrt(100)) ,6), 'Tam giac vuong can')

    def test23(self):
        self.assertEqual(triangle.detect_triangle((math.sqrt(100)),8,6), 'Tam giac vuong can')

    def test24(self):
        self.assertEqual(triangle.detect_triangle(2**32-2,8,2**32-5), 'Tam giac thuong')


if __name__ == '__main__':
    unittest.main()
