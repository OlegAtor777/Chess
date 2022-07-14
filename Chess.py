import copy
import sys
import traceback
global Table1
Table1 = [['8 ', ' ', 'r ','n ','b ','q ','k ','b ','n ','r ','\n'],
         ['7 ', ' ', 'p ','p ','p ','p ','p ','p ','p ','p ','\n'],
         ['6 ', ' ', '. ','. ','. ','. ','. ','. ','. ','. ','\n'],
         ['5 ', ' ', '. ','. ','. ','. ','. ','. ','. ','. ','\n'],
         ['4 ', ' ', '. ','. ','. ','. ','. ','. ','. ','. ','\n'],
         ['3 ', ' ', '. ','. ','. ','. ','. ','. ','. ','. ','\n'],
         ['2 ', ' ', 'P ','P ','P ','P ','P ','P ','P ','P ','\n'],
         ['1 ', ' ', 'R ','N ','B ','Q ','K ','B ','N ','R ','\n'],
         ['', '', '','','','','','','','','\n'],
         ['  ', ' ', 'A ','В ','C ','D ','E ','F ','G ','H ', '\n\n']]
global TableMn
global count
count = 1
TableMn = copy.deepcopy(Table1)
lit = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8}



class pole(object):
    def __init__(self):
        pass
    def draw(self):
        for i in range(len(Table1)):
            for j in range((len(Table1[i]))):
                print(Table1[i][j], end = '')
    def rewrite(self):
        for i in range(len(TableMn)):
            for j in range(len(TableMn[i])):
                if type(TableMn[i][j]) is figure:
                    Table1[i][j] = 'f '
                    
                if type(TableMn[i][j]) is pawn:
                    if TableMn[i][j].color == 'bl':
                        Table1[i][j] = 'p '
                    elif TableMn[i][j].color == 'wh':
                        Table1[i][j] = 'P '
                        
                if type(TableMn[i][j]) is rook:
                    if TableMn[i][j].color == 'bl':
                        Table1[i][j] = 'r '
                    elif TableMn[i][j].color == 'wh':
                        Table1[i][j] = 'R '
                        
                if type(TableMn[i][j]) is knight:
                    if TableMn[i][j].color == 'bl':
                        Table1[i][j] = 'n '
                    elif TableMn[i][j].color == 'wh':
                        Table1[i][j] = 'N '
                        
                if type(TableMn[i][j]) is bishop:
                    if TableMn[i][j].color == 'bl':
                        Table1[i][j] = 'b '
                    elif TableMn[i][j].color == 'wh':
                        Table1[i][j] = 'B '
                        
                if type(TableMn[i][j]) is king:
                    if TableMn[i][j].color == 'bl':
                        Table1[i][j] = 'k '
                    elif TableMn[i][j].color == 'wh':
                        Table1[i][j] = 'K '
                        
                if type(TableMn[i][j]) is queen:
                    if TableMn[i][j].color == 'bl':
                        Table1[i][j] = 'q '
                    elif TableMn[i][j].color == 'wh':
                        Table1[i][j] = 'Q '
                        
                if type(TableMn[i][j]) is str:
                    Table1[i][j] = TableMn[i][j]
    def prov(self):
        kincount = 0
        for i in range(len(TableMn)):
            for j in range(len(TableMn[i])):
                if type(TableMn[i][j]) is king:
                    kincount += 1
        if kincount == 2:
            return 'ok'
        elif kincount == 1:
            for i in range(len(TableMn)):
                for j in range(len(TableMn[i])):
                    if type(TableMn[i][j]) is king:
                        if TableMn[i][j].color == 'bl':
                            Pol.rewrite()
                            Pol.draw()
                            print('Победа чёрных!')
                            return sys.exit()
                        if TableMn[i][j].color == 'bl':
                            Pol.rewrite()
                            Pol.draw()
                            print('Победа белых!')
                            return sys.exit()
                        
                
class figure(object):
    def __init__(self):
        pass
    def move(self, x1,y1,x2,y2):
        TableMn[x2][y2] = figure()
        TableMn[x1][y1] = '. '
        
    
class pawn(figure):
    def __init__(self):
        pass
    color = ''
    hod = 0
    def move(self,x1,y1,x2,y2):
        if x1 == x2 and y1 == y2:
            return 'неверно'
        if TableMn[x1][y1].color == 'wh':
            if TableMn[x1][y1].hod == 0:
                if (y1-y2 == 0) and ((x2-x1 == -2) or (x2-x1 == -1)):
                     if x2-x1 == -2:
                         if TableMn[x2+1][y1] != '. ':
                             return 'препятствие'
                     if TableMn[x2][y2] == '. ':
                         TableMn[x2][y2] = TableMn[x1][y1]
                         TableMn[x1][y1] = '. '
                         TableMn[x2][y2].hod = 1
                         return 'ok'
                     else:
                        return 'неверно'
            elif TableMn[x1][y1].hod == 1:
                if (y1-y2 == 0) and (x2-x1 == -1):
                     if TableMn[x2][y2] == '. ':
                         TableMn[x2][y2] = TableMn[x1][y1]
                         TableMn[x1][y1] = '. '
                         TableMn[x2][y2].hod = 1
                         return 'ok'
                     else:
                         return 'неверно'
            if abs(y1-y2) == 1 and x2-x1 == -1:
                if TableMn[x2][y2] != '. ':
                         TableMn[x2][y2] = TableMn[x1][y1]
                         TableMn[x1][y1] = '. '
                         TableMn[x2][y2].hod = 1
                         return 'ok'
                else:
                    return 'неверно'
        if TableMn[x1][y1].color == 'bl':
            if TableMn[x1][y1].hod == 0:
                if (y1-y2 == 0) and ((x2-x1 == 2) or (x2-x1 == 1)):
                     if x2-x1 == 2:
                         if TableMn[x2-1][y1] != '. ':
                             return 'препятствие'
                     if TableMn[x2][y2] == '. ':
                         TableMn[x2][y2] = TableMn[x1][y1]
                         TableMn[x1][y1] = '. '
                         TableMn[x2][y2].hod = 1
                         return 'ok'
                     else:
                         return 'неверно'
            elif TableMn[x1][y1].hod == 1:
                if (y1-y2 == 0) and (x2-x1 == 1):
                     if TableMn[x2][y2] == '. ':
                         TableMn[x2][y2] = TableMn[x1][y1]
                         TableMn[x1][y1] = '. '
                         TableMn[x2][y2].hod = 1
                         return 'ok'
                     else:
                         return 'неверно'
            if abs(y1-y2) == 1 and x2-x1 == 1:
                if TableMn[x2][y2] != '. ':
                         TableMn[x2][y2] = TableMn[x1][y1]
                         TableMn[x1][y1] = '. '
                         TableMn[x2][y2].hod = 1
                         return 'ok'
                else:
                    return 'неверно'
    def prov(self,x1,y1):
        if TableMn[x1][y1].color == 'wh' and (count+1)%2 == 1:
            return 'notokbl'
        elif TableMn[x1][y1].color == 'bl' and (count+1)%2 == 0:
            return 'notokwh'
        else:
            return 'ok'
            
    
class knight(figure):
    def __init__(self):
        pass
    color = ''
    
    def move(self,x1,y1,x2,y2):
        if x1 == x2 and y1 == y2:
            return 'неверно'
        var = [(1,2),(-1,2),(1,-2),(-1,-2),(2,1),(-2,1),(2,-1),(-2,-1)]
        if ((x1-x2),(y1-y2)) in var:
            if TableMn[x2][y2] == '. ' or TableMn[x2][y2].color != TableMn[x1][y1].color:
                TableMn[x2][y2] = TableMn[x1][y1]
                TableMn[x1][y1] = '. '
                return 'ok'
            else:
                return 'неверно'
        else:
            return 'неверно'
    def prov(self,x1,y1):
        if TableMn[x1][y1].color == 'wh' and (count+1)%2 == 1:
            return 'notokbl'
        elif TableMn[x1][y1].color == 'bl' and (count+1)%2 == 0:
            return 'notokwh'
        else:
            return 'ok'
class bishop(figure):
    def __init__(self):
        pass
    color = ''
    def move(self,x1,y1,x2,y2):
        if x1 == x2 and y1 == y2:
            return 'неверно'
        if abs(x1-x2) == abs(y1-y2):
            
            if x1-x2 < 0 and y1-y2 < 0:
                for i in range(1,(abs(x2-x1))):
                    if TableMn[x1+i][y1+i] != '. ':
                        return 'препятствие'
            
            if x1-x2 > 0 and y1-y2 < 0:
                for i in range(1,(abs(y2-y1))):
                    if TableMn[x1-i][y1+i] != '. ':
                        return 'препятствие'
            
            if x1-x2 < 0 and y1-y2 > 0:
                for i in range(1,(abs(y1-y2))):
                    if TableMn[x1+i][y1-i] != '. ':
                        return 'препятствие'
            
            if x1-x2 > 0 and y1-y2 > 0:
                for i in range(1,(abs(x1-x2))):
                    if TableMn[x1-i][y1-i] != '. ':
                        return 'препятствие'
            
            
            if TableMn[x2][y2] == '. ' or TableMn[x2][y2].color != TableMn[x1][y1].color:
                TableMn[x2][y2] = TableMn[x1][y1]
                TableMn[x1][y1] = '. '
                return 'ok'
            else:
                return 'неверно'
        else:
            return 'неверно'
    def prov(self,x1,y1):
        if TableMn[x1][y1].color == 'wh' and (count+1)%2 == 1:
            return 'notokbl'
        elif TableMn[x1][y1].color == 'bl' and (count+1)%2 == 0:
            return 'notokwh'
        else:
            return 'ok'
class rook(figure):
    def __init__(self):
        pass
    color = ''
    def move(self, x1,y1,x2,y2):
        if x1 == x2 and y1 == y2:
            return 'неверно'
        if (x1-x2 == 0 and y1-y2 != 0) or (x1-x2 != 0 and y1-y2 == 0):
            
            if x1-x2 != 0:
                if x1 > x2:
                   for i in range(1, (abs(x1-x2))):
                       if TableMn[x1-i][y1] != '. ':
                           return 'препятствие'
                if x1 < x2:
                   for i in range(1, (abs(x1-x2))):
                       if TableMn[x1+i][y1] != '. ':
                           return 'препятствие'
            if y1-y2 != 0:
                if y1 > y2:
                   for i in range(1, (abs(y1-y2))):
                       if TableMn[x1][y1-i] != '. ':
                           return 'препятствие'
                if y1 < y2:
                   for i in range(1, (abs(y1-y2))):
                       if TableMn[x1][y1+i] != '. ':
                           return 'препятствие'
                      
            
            if TableMn[x2][y2] == '. ' or TableMn[x2][y2].color != TableMn[x1][y1].color:
                TableMn[x2][y2] = TableMn[x1][y1]
                TableMn[x1][y1] = '. '
                return 'ok'
            else:
                return 'неверно'
    def prov(self,x1,y1):
        if TableMn[x1][y1].color == 'wh' and (count+1)%2 == 1:
            return 'notokbl'
        elif TableMn[x1][y1].color == 'bl' and (count+1)%2 == 0:
            return 'notokwh'
        else:
            return 'ok'    
class king(figure):
    def __init__(self):
        pass
    color = ''
    def move(self, x1,y1,x2,y2):
        if x1 == x2 and y1 == y2:
            return 'неверно'
        var = [(0,1),(1,1),(1,0),(1,-1),(-1,0),(-1,-1),(0,-1),(-1,1)]
        if ((x1-x2),(y1-y2)) in var:
            if TableMn[x2][y2] == '. ' or TableMn[x2][y2].color != TableMn[x1][y1].color:
                TableMn[x2][y2] = TableMn[x1][y1]
                TableMn[x1][y1] = '. '
                return 'ok'
            else:
                return 'неверно'
        else:
            return 'неверно'
    def prov(self,x1,y1):
        if TableMn[x1][y1].color == 'wh' and (count+1)%2 == 1:
            return 'notokbl'
        elif TableMn[x1][y1].color == 'bl' and (count+1)%2 == 0:
            return 'notokwh'
        else:
            return 'ok'
class queen(figure):
    def __init__(self):
        pass
    color = ''
    def move(self,x1,y1,x2,y2):
        if x1 == x2 and y1 == y2:
            return 'неверно'
        if (x1-x2 == 0 and y1-y2 != 0) or (x1-x2 != 0 and y1-y2 == 0):
            
            if x1-x2 != 0:
                if x1 > x2:
                   for i in range(1, (abs(x1-x2))):
                       if TableMn[x1-i][y1] != '. ':
                           return 'препятствие'
                if x1 < x2:
                   for i in range(1, (abs(x1-x2))):
                       if TableMn[x1+i][y1] != '. ':
                           return 'препятствие'
            if y1-y2 != 0:
                if y1 > y2:
                   for i in range(1, (abs(y1-y2))):
                       if TableMn[x1][y1-i] != '. ':
                           return 'препятствие'
                if y1 < y2:
                   for i in range(1, (abs(y1-y2))):
                       if TableMn[x1][y1+i] != '. ':
                           return 'препятствие'
                      
            
            if TableMn[x2][y2] == '. ' or TableMn[x2][y2].color != TableMn[x1][y1].color:
                TableMn[x2][y2] = TableMn[x1][y1]
                TableMn[x1][y1] = '. '
                return 'ok'
            else:
                return 'неверно'
                
        if abs(x1-x2) == abs(y1-y2):
            
            if x1-x2 < 0 and y1-y2 < 0:
                for i in range(1,(abs(x2-x1))):
                    if TableMn[x1+i][y1+i] != '. ':
                        return 'препятствие'
            
            if x1-x2 > 0 and y1-y2 < 0:
                for i in range(1,(abs(y2-y1))):
                    if TableMn[x1-i][y1+i] != '. ':
                        return 'препятствие'
            
            if x1-x2 < 0 and y1-y2 > 0:
                for i in range(1,(abs(y1-y2))):
                    if TableMn[x1+i][y1-i] != '. ':
                        return 'препятствие'
            
            if x1-x2 > 0 and y1-y2 > 0:
                for i in range(1,(abs(x1-x2))):
                    if TableMn[x1-i][y1-i] != '. ':
                        return 'препятствие'
            
            
            if TableMn[x2][y2] == '. ' or TableMn[x2][y2].color != TableMn[x1][y1].color:
                TableMn[x2][y2] = TableMn[x1][y1]
                TableMn[x1][y1] = '. '
                return 'ok'
            else:
                return 'неверно'
        else:
            return 'неверно'
    def prov(self,x1,y1):
        if TableMn[x1][y1].color == 'wh' and (count+1)%2 == 1:
            return 'notokbl'
        elif TableMn[x1][y1].color == 'bl' and (count+1)%2 == 0:
            return 'notokwh'
        else:
            return 'ok'
        
for i in range(len(Table1)):
    for j in range((len(Table1[i]))):
        if Table1[i][j] == 'p ' or Table1[i][j] == 'P ':
            TableMn[i][j] = pawn()
            if Table1[i][j] == 'p ':
                TableMn[i][j].color = 'bl'
            elif Table1[i][j] == 'P ':
                TableMn[i][j].color = 'wh'
                
        if Table1[i][j] == 'f ':
            TableMn[i][j] = figure()
            
        if Table1[i][j] == 'r ' or Table1[i][j] == 'R ':
            TableMn[i][j] = rook()
            if Table1[i][j] == 'r ':
                TableMn[i][j].color = 'bl'
            elif Table1[i][j] == 'R ':
                TableMn[i][j].color = 'wh'
                
        if Table1[i][j] == 'n ' or Table1[i][j] == 'N ':
            TableMn[i][j] = knight()
            if Table1[i][j] == 'n ':
                TableMn[i][j].color = 'bl'
            elif Table1[i][j] == 'N ':
                TableMn[i][j].color = 'wh'
                
        if Table1[i][j] == 'b ' or Table1[i][j] == 'B ':
            TableMn[i][j] = bishop()
            if Table1[i][j] == 'b ':
                TableMn[i][j].color = 'bl'
            elif Table1[i][j] == 'B ':
                TableMn[i][j].color = 'wh'
                
        if Table1[i][j] == 'k ' or Table1[i][j] == 'K ':
            TableMn[i][j] = king()
            if Table1[i][j] == 'k ':
                TableMn[i][j].color = 'bl'
            elif Table1[i][j] == 'K ':
                TableMn[i][j].color = 'wh'
                
        if Table1[i][j] == 'q ' or Table1[i][j] == 'Q ':
            TableMn[i][j] = queen()
            if Table1[i][j] == 'q ':
                TableMn[i][j].color = 'bl'
            elif Table1[i][j] == 'Q ':
                TableMn[i][j].color = 'wh'
                    
Pol = pole()
Pol.draw()
print('Через пробел введите поле фигуры и поле хода (Например: "D2 D3"), чтобы закончить введите "Конец игры"\nБелые - большие, черные - маленькие ')


global a, b

def game():
    global count
    try:
        a,b = input('Ход: ').split()
    except ValueError:
        Pol.draw()
        print('Некорректный ввод!')
        game()
        return
    if a.upper() == 'КОНЕЦ' and b.upper() == 'ИГРЫ':
        print('Завершение работы программы...')
        sys.exit()
    try:
        x1 = 8-int(a[1])
        y1 = lit[a[0]]+1
        x2 = 8-int(b[1])
        y2 = lit[b[0]]+1
    except KeyError:
        Pol.draw()
        print('Некорректный ввод!')
        game()
        return
    try:
        check1 = TableMn[x1][y1].prov(x1,y1)
        if check1 == 'notokbl':
            Pol.draw()
            print('Сейчас ходят черные!')
            game()
            return
        if check1 == 'notokwh':
            Pol.draw()
            print('Сейчас ходят белые!')
            game()
            return
        check2 = TableMn[x1][y1].move(x1,y1, x2,y2)
        
        if check2 == 'неверно' or check2 == 'препятствие':
            #Pol.draw()
            print('Неправильный ход!')
            game()
            return
        check3 = Pol.prov()
        if check1 == 'ok' and check2 == 'ok' and check3 == 'ok':
            count += 1
            Pol.rewrite()
            Pol.draw()
            game()
            return
    except AttributeError:
        print('\n',traceback.format_exc())
        Pol.draw()
        print('Неправильный ход!!!')
        game()
        return
game()