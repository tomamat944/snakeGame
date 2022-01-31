class Snake:
    def __init__(self, board, ts, w, h):
        self.width=w
        self.height=h
        self.board=board
        self.tile_size=ts
        self.head_snake=None
        self.body_snake=[]
        self.direction="left"

    def collideSides(self):
        pos=self.board.coords(self.head_snake)
        if pos[0]<0 or pos[0]>self.width or pos[1]<0 or pos[1]>self.height:
            return True

    def collideSelf(self):
        pos_snake=self.board.coords(self.head_snake)
        pos_body=list(map(self.board.coords, self.body_snake))
        if pos_snake in pos_body:
            return True

    def growSnake(self):
        lasttile=self.board.coords(self.body_snake[-1])
        newtile=self.board.create_rectangle(*lasttile, fill="green")
        self.body_snake.append(newtile)

    def isEaten(self, food):
        return self.board.coords(self.head_snake) == self.board.coords(food.foodpos)

    def moveSnake(self):
        current = self.board.coords(self.head_snake)
        if self.direction=='up':
            self.board.move(self.head_snake,0 , -self.tile_size)
        if self.direction=='down':
            self.board.move(self.head_snake,0,self.tile_size)
        if self.direction=='left':
            self.board.move(self.head_snake, -self.tile_size,0)
        if self.direction=='right':
            self.board.move(self.head_snake,self.tile_size,0)

        for i in self.body_snake:
            temp=self.board.coords(i)
            self.board.coords(i, *current)
            current=temp


    def setDirection(self, event):
        if event.char=="w" and self.direction!="down":
            self.direction="up"
        if event.char=="s" and self.direction!="up":
            self.direction="down"
        if event.char=="a" and self.direction!="right":
            self.direction="left"
        if event.char=="d" and self.direction!="left":
            self.direction="right"

    def createSnake(self):
        w=self.width
        h=self.height
        tw=int(w/(self.tile_size*2))*self.tile_size
        th=int(h/(self.tile_size*2))*self.tile_size
        self.head_snake=self.board.create_rectangle(tw, th,
                                                    tw+self.tile_size, th+self.tile_size,fill="blue")
        self.body_snake.append(self.board.create_rectangle(w/2+self.tile_size, h/2,
                                                    w/2+self.tile_size*2, h/2+self.tile_size,fill="green"))
        self.body_snake.append(self.board.create_rectangle(w / 2+self.tile_size*2, h / 2,
                                   w / 2 + self.tile_size*3, h / 2 + self.tile_size, fill="green"))