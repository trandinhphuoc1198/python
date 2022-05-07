from player import people,computer, supercomputer
class Tictactoe():
    def __init__(self):
        self.board=[' ' for _ in range(9)]
        self.winner=None
    def print_board(self):
        for row in [self.board[i*3:(i+1)*3]for i in range(3)]:
            print('| ' + ' | '.join(row)+' |')
    def able_move(self):
        return [i for i,y in enumerate(self.board) if y==' ']
    def make_move1(self,player,square):
        self.board[square]=player.letter
        if self.check_win(square,player) is True:
            self.winner=player.name
            return
    def make_move(self,player,square):
        self.board[square]=player.letter
        
        if self.check_win(square,player) is True:
            self.winner=player.name
            print(f'the winner is {player.name}')
            self.print_board()
            return
        self.print_board()
    def available_move(self):
        return ' ' in self.board
    def check_win(self,square,player):
        row_i=square//3
        row=self.board[row_i*3:(row_i+1)*3]
        if all(self.board[square]==i for i in row):
            self.winner=player.name
            return True
        col=square%3
        if all(self.board[square]==i for i in [self.board[a] for a in (col,col+3,col+6)]):
            self.winner=player.name
            return True
        if square%2==0:
            diag=[self.board[i] for i in (0,4,8)]
            diag2=[self.board[i] for i in (2,4,6)]
            if all(self.board[square]==i for i in diag):
                self.winner=player.name
                return True
            elif all(self.board[square]==i for i in diag2):
                self.winner=player.name
                return True
        return None
def play(game,player1,player2):
    game.print_board()
    turn=player1
    while game.available_move():
        print('')
        if game.winner!=None:
            break
        else:
            if turn==player1:
                square=player1.get_move(game)
            else:
                square=player2.get_move(player2,player1,game)
            game.make_move(turn,square)
            turn=player2 if turn==player1 else player1
            
    if game.winner==None:
        print("TIE")
game1=Tictactoe()
phuoc=people('y','phuoc')
supercomputer1=supercomputer('x')
play(game1,phuoc,supercomputer1)