from fractions import Fraction
import numpy as np

class mncln:
#инициализация
    def __init__(self, cfs):
        self.cfs = cfs

    def __add__(self, other):
#сложение
        md = max(len(self.cfs), len(other.cfs))
        result = [Fraction(0)] * md
        
        for i in range(md):
            c1 = self.cfs[i] if i < len(self.cfs) else 0
            c2 = other.cfs[i] if i < len(other.cfs) else 0
            result[i] = c1 + c2
        
        return mncln(result)
#значение в точке
    def point(self, x):
        return sum(coeff * (x ** i) for i, coeff in enumerate(self.cfs))
#производная 
    def przv(self):
        return mncln([Fraction(i * coeff) for i, coeff in enumerate(self.cfs) if i > 0])
#запись в файл
    def file(self, filename):
        terms = []
        for i, cf in enumerate(reversed(self.cfs)):
            if cf != 0:
                term = f"{cf}x^{len(self.cfs) - i - 1}" if i < len(self.cfs) - 1 else f"{cf}"
                terms.append(term)    
        with open(filename, 'w') as f:
            f.write('+'.join(terms))
#поиск корней
    def roots(self):
        if not all(isinstance(coeff, Fraction) for coeff in self.cfs):
            return "коэффициенты должны быть дробями."
        deg = len(self.cfs) - 1
        roots = []      
        for i in range(-deg, deg + 1):
            if self.point(i) == 0:
                roots.append(i)
        
        return roots
    def pf(self):
        res = len(self.cfs)-1
        for i in self.cfs:
            if i<0:
                print(str(i) + "x^%r" % res, end='')
            else:
                print('+'+str(i)+"x^%r" %res, end = '' )
            res-=1
        return ''
#поиск нод
    def gcd(self, other):

        a, b = self, other
        while b.cfs != [Fraction(0)]:

            while b.cfs and b.cfs[0] == 0:
                b.cfs.pop(0)
            if not b.cfs:
                break
            q = []
            r = a.cfs[:]
            lead_coeff_b = b.cfs[0]
            for i in range(len(a.cfs) - len(b.cfs) + 1):
                f = r[i] / lead_coeff_b
                q.append(f)
                for j in range(len(b.cfs)):
                    r[i + j] -= f * b.cfs[j]
            a, b = b, mncln([Fraction(x) for x in r if x != 0])
        return a
#пример
p1 = mncln([Fraction(4, 1), Fraction(0, 1), Fraction(-1, 1)])
p2 = mncln([Fraction(2, 1), Fraction(1, 1)])  
p3 = p1 + p2
print(p3.pf())  
#вычисление в точке
print(p3.point(1))  
#производная
print(p3.przv().pf())  
#запись в файл
p3.file('многочлен.txt')
#поиск корней
print(p1.roots())
#поиск нод
print(p1.gcd(p2).pf())  



