import random,time,math,copy
class player():
    def __init__(self,letter,name):
        self.letter=letter
        self.name=name
class computer(player):
    def __init__(self,letter,name='computer'):
        super().__init__(letter,name)
    def get_move(self,game):
        square=random.choice(game.able_move())
        time.sleep(2)
        return square
class people(player):
    def __init__(self,letter,name):
        super().__init__(letter,name)
    def get_move(self,game):
        while True:
            try:
                square=int(input('Input the number 0~9: '))
                if game.board[square] ==' ':
                    return square
                else:
                    print('choose the empty pls!!')
            except:
                print('PICK THE NUMBER IDIOT!!!')
class supercomputer(player):
    def __init__(self,letter,name='supercomputer'):
        super().__init__(letter,name)
    def get_move(self,player1,player2,game):
        square=self.minimax(player1,player2,game)[1]
        print(square)
        time.sleep(1)
        return square
    def minimax(self,player1,player2,game,maxplayer=True):
        
        if game.winner!=None:
            if game.winner==self.name:
                return [1*len(game.able_move())+1,None]
            else:
                return [-1*(len(game.able_move())+1),None]
        elif not game.available_move():
            return [0,None]
        if maxplayer:
            maxvalue=-math.inf
            for move in game.able_move():
                game.make_move1(player1,move)
                score=self.minimax(player1,player2,game,False)[0]
                if score>maxvalue:
                    maxvalue=score
                    bestmove=move
                game.board[move]=' '
                game.winner=None
            return [maxvalue,bestmove]
        else:
            minvalue=math.inf
            for move in game.able_move():
                game.make_move1(player2,move)
                score=self.minimax(player1,player2,game,True)[0]
                if score<minvalue:  
                    minvalue=score
                    bestmove=move
                game.board[move]=' '
                game.winner=None
            return [minvalue,bestmove]