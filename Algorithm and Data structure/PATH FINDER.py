import copy
import math,time
from curses import A_BLINK, A_BOLD, A_DIM, A_ITALIC, A_UNDERLINE, wrapper
import curses

class pathfinder():
    def __init__(self):
        self.map=[  ['##','##','##','xx','##','  '],
                    ['##','  ','##','  ','  ','  '],
                    ['  ','  ','  ','##','  ','  '],
                    ['##','  ','##','##','  ','##'],
                    ['##','  ','  ','##','  ','##'],
                    ['  ','  ','  ','##','  ','  '],
                    ['##','##','  ','##','  ','##'],
                    ['##','##','  ','##','  ','##'],
                    ['##','##','##','##','yy','  ']]
        # self.map=[  ['##','##','##','xx','##','##'],
        #             ['##','  ','##','  ','  ','##'],
        #             ['##','  ','  ','  ','  ','##'],
        #             ['##','  ','##','  ','  ','##'],
        #             ['##','  ','  ','##','  ','##'],
        #             ['##','##','  ','  ','  ','##'],
        #             ['##','##','##','##','yy','##']]
        self.posi_x=0
        self.posi_y=3
        self.status=True
    def able_moves(self):
        able_moves=[]
        up=self.posi_x-1
        down=self.posi_x+1
        left=self.posi_y-1
        right=self.posi_y+1
        if self.posi_x<len(self.map)-1 and self.posi_y<len(self.map[0])-1:
            if self.map[up][self.posi_y]=='  ' or self.map[up][self.posi_y]=='yy':
                able_moves.append([up,self.posi_y])
            if self.map[down][self.posi_y]=='  ' or self.map[down][self.posi_y]=='yy':
                able_moves.append([down,self.posi_y])
            if self.map[self.posi_x][left]=='  ' or self.map[self.posi_x][left]=='yy':
                able_moves.append([self.posi_x,left])
            if self.map[self.posi_x][right]=='  ' or self.map[self.posi_x][right]=='yy':
                able_moves.append([self.posi_x,right])
        elif self.posi_x==len(self.map)-1 and self.posi_y<len(self.map[0])-1:
            down=-1
            if self.map[up][self.posi_y]=='  ' or self.map[up][self.posi_y]=='yy':
                able_moves.append([up,self.posi_y])
            if self.map[down][self.posi_y]=='  ' or self.map[down][self.posi_y]=='yy':
                able_moves.append([down,self.posi_y])
            if self.map[self.posi_x][left]=='  ' or self.map[self.posi_x][left]=='yy':
                able_moves.append([self.posi_x,left])
            if self.map[self.posi_x][right]=='  ' or self.map[self.posi_x][right]=='yy':
                able_moves.append([self.posi_x,right])
        elif self.posi_y==len(self.map[0])-1 and self.posi_x<len(self.map)-1:
            right=0
            if self.map[up][self.posi_y]=='  ' or self.map[up][self.posi_y]=='yy':
                able_moves.append([up,self.posi_y])
            if self.map[down][self.posi_y]=='  ' or self.map[down][self.posi_y]=='yy':
                able_moves.append([down,self.posi_y])
            if self.map[self.posi_x][left]=='  ' or self.map[self.posi_x][left]=='yy':
                able_moves.append([self.posi_x,left])
            if self.map[self.posi_x][right]=='  ' or self.map[self.posi_x][right]=='yy':
                able_moves.append([self.posi_x,right])
        return able_moves
    def check_end(self,direction):
        if self.map[direction[0]][direction[1]]=='yy':
            return False
    def mave_move(self,direction,mark):
        if self.check_end(direction)== False:
            if mark<10:
                self.map[direction[0]][direction[1]]='0' +str(mark) 
            else: 
                self.map[direction[0]][direction[1]]=str(mark)
            self.status=False
        elif mark<10:
            self.map[direction[0]][direction[1]]='0' +str(mark)
            self.posi_x=direction[0]
            self.posi_y=direction[1]
        else:
            self.map[direction[0]][direction[1]]=str(mark)
            self.posi_x=direction[0]
            self.posi_y=direction[1]
a=pathfinder()
b=[1]
def find_way(map,moves,num,best,stdscr,b):
    curses.init_pair(1,curses.COLOR_WHITE,curses.COLOR_BLUE)
    curses.init_pair(2,curses.COLOR_WHITE,curses.COLOR_RED)
    color=curses.color_pair(1)
    color2=curses.color_pair(2)
    
    stdscr.clear()
    if num%2:
        color=color2
    for move in moves:
        map1=copy.deepcopy(map)
        map1.mave_move(move,num)
        stdscr.clear()
        if map1.status:
            for row in map1.map:
                for x in row:
                    if x.isnumeric():
                        stdscr.addstr(str(x),color|curses.A_BOLD)
                    else:
                        stdscr.addstr(str(x))
                stdscr.addstr('\n')
            time.sleep(0.2)
            stdscr.refresh()
        elif map1.status is False:
            for row in map1.map:
                for x in row:
                    if x.isnumeric():
                        stdscr.addstr(str(x),color2)
                    else:
                        stdscr.addstr(str(x))
                stdscr.addstr('\n')
            stdscr.refresh()
            time.sleep(0.1)
            if num<=best:
                best=num
                b[0]=map1.map
            b.append(map1.map)
            return best
        stdscr.refresh()
        best=find_way(map1,map1.able_moves(),num+1,best,stdscr,b)
    return best
def main(stdscr):
    stdscr.clear()
    stdscr.addstr('Let\'s find out the BEST SHORTEST WAY!!!')
    stdscr.addstr('\n')
    stdscr.refresh()
    time.sleep(2)
    curses.init_pair(2,curses.COLOR_RED,curses.COLOR_RED)
    color2=curses.color_pair(2)
    print(find_way(a,a.able_moves(),0,math.inf,stdscr,b))
    stdscr.clear()
    stdscr.addstr('So the best way is: ')
    stdscr.addstr('\n')
    stdscr.refresh()
    time.sleep(1)
    showlist='2'
    if showlist=='2':
        for n,i in enumerate(b):
            stdscr.addstr('\n')
            stdscr.addstr('number '+str(n+1)+'\n')
            stdscr.addstr('\n')
            for a1 in i:
                for x in a1:
                    if x.isnumeric():
                        stdscr.addstr(str(x),color2)
                    else:
                        stdscr.addstr(str(x))
                stdscr.addstr('\n')
            stdscr.refresh()
            time.sleep(1)
            stdscr.clear()
    elif showlist=='1':
        for y in b[0]:
            for x in y:
                if x.isnumeric():
                    stdscr.addstr(str(x),color2)
                else:
                    stdscr.addstr(str(x))
            stdscr.addstr('\n')
        stdscr.refresh()
        time.sleep(1)


wrapper(main)
for i in b:
    for x in i:
        print(x)
    print('')