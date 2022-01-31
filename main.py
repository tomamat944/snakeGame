import gamemod as g

def main():
    root=g.tk.Tk()
    game=g.Game(root, 400, 200, "#333333")
    game.run()
    root.mainloop()

if __name__=="__main__":
    main()
