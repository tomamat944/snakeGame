import tkinter as tk
import snakemod as s
import foodmod as f
class Game:
    def __init__(self, root, w, h, c):
        self.width=w
        self.height=h
        self.tile_size=20
        self.speed=250
        self.root = root
        self.board=tk.Canvas(master=self.root, width=w, height=h, bg=c)
        self.board.pack()
        self.label=tk.Label(master=self.root, text="Use wsad to move")
        self.label.pack()
        self.snake=s.Snake(self.board, self.tile_size, self.width, self.height)
        self.food=f.Food(self.board, self.tile_size,self.width, self.height)
        self.root.bind("<KeyPress>", self.snake.setDirection)
        self.counter=0
        self.score=None
        self.inititalizeGame()


    def inititalizeGame(self):
        self.snake.createSnake()
        self.food.createFood(self.snake)


    def restart(self):
        self.snake=s.Snake(self.board, self.tile_size, self.width, self.height)
        self.food=f.Food(self.board, self.tile_size,self.width, self.height)
        self.board.delete("all")
        self.root.bind("<KeyPress>", self.snake.setDirection)
        self.counter=0
        self.inititalizeGame()

    def updateGame(self):
        if self.score is None:
            self.score=self.board.create_text(self.width/2, 10, text=f'Score: {self.counter}', fill="white")
        else:
            self.board.delete(self.score)
            self.score = self.board.create_text(self.width / 2, 10, text=f'Score: {self.counter}', fill="white")
        self.snake.moveSnake()
        if self.snake.collideSides() or self.snake.collideSelf():
            self.restart()
        if self.snake.isEaten(self.food):
            self.counter+=1
            self.snake.growSnake()
            self.food.createFood(self.snake)

    def run(self):
        self.updateGame()
        self.root.after(self.speed, self.run)

