from sympy import *
import sympy as sy
x = Symbol('x')
f1 = 6 * x ** 3 # مشتق از روش دوم یا سوم
f2 =  sy.tan(sy.cos(3*x)) ** -1 # نمونه برای بدست آوردن مشتق توابع مثلثاتی
f3 = (5*x + 3) / (6-2*x) # تابع کسری
f4 = sy.sqrt(x) # رادیکالی
f_prime = f4.diff(x)
print(f_prime)
