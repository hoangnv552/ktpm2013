__author__ = 'hoangnongvan'

__project__ = 'TestTriangle'

import math

ep = pow(10,-9)

def detect_triangle(a,b,c):
   if (type(a) in [int, long, float]) and (type(b) in [int, long, float]) and (type(c) in [int, long, float]) and  (a < 2**32 - 1) and (b < 2**32 - 1) and (c < 2**32 - 1):
       if (a+b)>c and (a+c)>b and (b+c)>a and (a>0) and (b>0) and (c>0):
           if(a==b)and (b==c):
               return "Tam giac deu"
           elif((math.fabs(a*a+b*b-c*c)<= ep)|(math.fabs(a*a+c*c-b*b)<= ep)|(math.fabs(c*c+b*b-a*a)<= ep)):
               return "Tam giac vuong can"
           elif(a==b)or(b==c)or(a==c):
               return "Tam giac can"
           elif((math.fabs(a*a+b*b-c*c)<= ep)|(math.fabs(a*a+c*c-b*b)<= ep)|(math.fabs(c*c+b*b-a*a)<= ep)):

               return  "Tam giac vuong"
           else:
               return "Tam giac thuong"
       else:
           return "Khong phai la 3 canh cua tam giac"
   else:
       return "du lieu khong hop le"


