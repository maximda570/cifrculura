import math

class solution:
    def __init__(self):
        self.s = []
#чтение файла
    def file(self, filename):
        with open(filename, 'r') as file:
            for line in file:
                c = list(map(float, line.split()[:4]))
                sn = int(line.split()[-1])
                self.s.append((c, sn))
#поиск площадей
    def sq(self, s):
        x1, y1, x2, y2 = s[0]
        if x1 == x2:  
            return (x1, 1 - x1)  
        elif y1 == y2:
            return (1 - y1, y1)  
        else:
            up = 0.5 * abs((x2 - x1) * (1 - y1) - (1 - x1) * (y2 - y1))
            down= 1-up 
            return (up ,down )
#поиск пересеений
    def cross(self):

        cr = []
        for i, (s1, id1) in enumerate(self.s):
            for j, (s2, id2) in enumerate(self.s):
                if i >= j: 
                    continue
                x1, y1, x2, y2 = s1
                x3, y3, x4, y4 = s2
                
                denom = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
                if denom != 0:
                    t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / denom
                    u = -((x1 - x2) * (y1 - y3) - (y1 - y2) * (x1 - x3)) / denom
                    if 0 <= t <= 1 and 0 <= u <= 1: 
                        px = x1 + t * (x2 - x1)
                        py = y1 + t * (y2 - y1)
                        if 0 <= px <= 1 and 0 <= py <= 1:  
                            cr.append((px, py, id1, id2))
        return cr
#поиск пересечений 3 и более точек
    def tnm(self):

        cr = self.cross()
        tp = []
        pc = {}
        for p in cr:
            c = (p[0], p[1])  
            pc[c] = pc.get(c, 0) + 1
        
        for p, i in pc.items():
            if i >= 3:
                tp.append(p)
        
        if not tp:
            print("нет пересечений 3 и более точек")
        return tp

#пример
solution = solution()
solution.file('отрезки.txt')
#площади
for s in solution.s:
    print(f" {s[1]} {solution.sq(s)}")
#пересечения
print(solution.cross())
#3 и больше отрезков
print(solution.tnm())


