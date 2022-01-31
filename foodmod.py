import random

class Food:
    def __init__(self,board, ts, w, h):

        self.board=board
        self.tile_size=ts
        self.width=w
        self.height=h
        self.foodpos=None


    def createFood(self, snake):
        posibble_loc=[]
        snake_loc=list(map(self.board.coords, snake.body_snake))
        for i in range(int(self.width/self.tile_size)):
            for j in range(int(self.height/self.tile_size)):
                temp=[i*self.tile_size, j*self.tile_size,
                      i*self.tile_size+self.tile_size,j*self.tile_size+self.tile_size]
                if temp not in snake_loc:
                    posibble_loc.append(temp)
        if self.foodpos==None:
            self.foodpos=self.board.create_rectangle(*random.choice(posibble_loc), fill="red")
        else:
            self.board.coords(self.foodpos, *random.choice(posibble_loc))